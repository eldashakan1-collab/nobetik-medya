import sys,os,subprocess
sys.path.insert(0,'/home/claude')
src=open('/home/claude/render_final.py').read()
# reuse font css builder
ns={}; exec(src.split("FONTCSS='\\n'.join(css)")[0]+"FONTCSS='\\n'.join(css)",ns)
from playwright.sync_api import sync_playwright
html=open(sys.argv[1],encoding='utf-8').read().replace('FONTCSS',ns['FONTCSS']).replace('href="LOGO"','href="file:///home/claude/brand/logo.png"')
open('/tmp/reel_build.html','w',encoding='utf-8').write(html)
mode=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1920}); pg.goto('file:///tmp/reel_build.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
    if mode=='preview':
        ts=[float(x) for x in sys.argv[3].split(',')]
        for t in ts: pg.evaluate(f'setT({t})'); pg.screenshot(path=f'/tmp/pv_{t:05.1f}.png')
    else:
        out=sys.argv[3]; os.makedirs('/tmp/frames',exist_ok=True)
        for f in range(900):
            pg.evaluate(f'setT({f/30})'); pg.screenshot(path=f'/tmp/frames/{f:04d}.jpg',type='jpeg',quality=92)
        b.close()
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i','/tmp/frames/%04d.jpg','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',out],check=True)
