import os, glob, sys
from playwright.sync_api import sync_playwright
F='/home/claude/fonts/node_modules/@fontsource'
css=[]
def face(fam, pkg, w, style):
    for sub,rng in [('latin',None),('latin-ext',None)]:
        p=f'{F}/{pkg}/files/{pkg}-{sub}-{w}-{style}.woff2'
        if os.path.exists(p):
            css.append(f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};src:url('file://{p}') format('woff2');}}")
for w in (400,500,600,700,800,900): face('Inter','inter',w,'normal')
for w in (400,500,600):
    for s in ('normal','italic'): face('Fraunces','fraunces',w,s)
for w in (500,700): face('Caveat','caveat',w,'normal')
FONTCSS='\n'.join(css)
SRC='/home/claude/canvas/project'; OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
jobs={'Main':'2026-11-26-terazi','K1':'2026-11-27-kontrol-1','K2':'2026-11-27-kontrol-2','K3':'2026-11-27-kontrol-3','K4':'2026-11-27-kontrol-4','K5':'2026-11-27-kontrol-5','K6':'2026-11-27-kontrol-6','K7':'2026-11-27-kontrol-7','Reel':'2026-11-28-reels-kapak','S1':'2026-11-29-story-1','S2':'2026-11-29-story-2','S3':'2026-11-29-story-3','Defter':'2026-11-30-defter','Otuz':'2026-12-01-otuz-saniye','Ibre':'2026-12-02-iki-ibre'}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--allow-file-access-from-files'])
    for src,name in jobs.items():
        tall=src in ('Reel','S1','S2','S3')
        pg=b.new_page(viewport={'width':1080,'height':1920 if tall else 1350})
        html=open(f'{SRC}/{src}.dc.html',encoding='utf-8').read()
        extra='<style>'+FONTCSS+('[style*="dashed"]{visibility:hidden}' if src.startswith('S') else '')+'</style>'
        html=html.replace('<head>','<head>'+extra,1)
        tmp=f'/tmp/r_{src}.html'; open(tmp,'w',encoding='utf-8').write(html)
        pg.goto('file://'+tmp); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(600)
        ok=pg.evaluate("[document.fonts.check('600 40px Fraunces'),document.fonts.check('700 40px Caveat'),document.fonts.check('900 40px Inter')]")
        pg.screenshot(path=f'{OUT}/{name}.png'); print(name, ok)
    b.close()
