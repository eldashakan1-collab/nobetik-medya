"""Nobetik Instagram görsel üretici.

Kullanım: python3 tools/render.py posts/2026-11-25.json
JSON alanları:
  slug      : çıktı dosya adı (gorseller/<slug>.png)
  layout    : "hook" (büyük soru + cevap) veya "list" (başlık + madde listesi)
  eyebrow   : üstteki küçük etiket
  title     : ana başlık (\n ile satır kırılabilir)
  highlight : başlıkta vurgulanacak kelime(ler) (isteğe bağlı)
  body      : hook düzeninde alt metin
  items     : list düzeninde maddeler
  cta       : alttaki çağrı metni
Çıktı: 1080x1350 PNG (Instagram 4:5 portre).
"""
import html
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "gorseller"

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1080px; height:1350px; font-family:'Poppins','Inter',sans-serif;
  background:#0B2545; color:#fff; position:relative; overflow:hidden; }
.bg1 { position:absolute; width:900px; height:900px; border-radius:50%;
  background:radial-gradient(circle,#13C4A3 0%,rgba(19,196,163,0) 70%);
  opacity:.28; top:-300px; right:-320px; }
.bg2 { position:absolute; width:700px; height:700px; border-radius:50%;
  background:radial-gradient(circle,#3E7CB1 0%,rgba(62,124,177,0) 70%);
  opacity:.35; bottom:-260px; left:-260px; }
.grid { position:absolute; inset:0; opacity:.06;
  background-image:linear-gradient(#fff 1px,transparent 1px),linear-gradient(90deg,#fff 1px,transparent 1px);
  background-size:90px 90px; }
.wrap { position:absolute; inset:0; padding:96px 90px; display:flex; flex-direction:column; }
.brand { display:flex; align-items:center; gap:18px; font-weight:700; font-size:38px; letter-spacing:.5px; }
.logo { width:64px; height:64px; border-radius:18px; background:#13C4A3; display:flex;
  align-items:center; justify-content:center; font-size:40px; color:#0B2545; font-weight:800; }
.brand span { color:#13C4A3; }
.eyebrow { margin-top:110px; display:inline-block; align-self:flex-start; padding:12px 26px;
  border-radius:40px; background:rgba(19,196,163,.15); border:2px solid rgba(19,196,163,.55);
  color:#7FF0D8; font-size:28px; font-weight:600; letter-spacing:1px; text-transform:uppercase; }
h1 { margin-top:44px; font-size:84px; line-height:1.12; font-weight:800; letter-spacing:-1px; }
h1 em { font-style:normal; color:#13C4A3; }
.body { margin-top:44px; font-family:'Inter',sans-serif; font-size:38px; line-height:1.5;
  color:#C9D6E8; font-weight:400; max-width:880px; }
ul { margin-top:56px; list-style:none; display:flex; flex-direction:column; gap:30px; }
li { display:flex; align-items:flex-start; gap:26px; font-family:'Inter',sans-serif;
  font-size:38px; line-height:1.35; color:#E6EEF8; }
.tick { flex:none; width:54px; height:54px; border-radius:50%; background:#13C4A3; color:#0B2545;
  display:flex; align-items:center; justify-content:center; font-size:32px; font-weight:800; margin-top:-2px; }
.spacer { flex:1; }
.cta { display:flex; align-items:center; justify-content:space-between; padding:34px 44px;
  border-radius:28px; background:#fff; color:#0B2545; }
.cta b { font-size:36px; font-weight:700; }
.cta i { font-style:normal; font-size:32px; font-weight:700; color:#fff; background:#0B2545;
  padding:14px 28px; border-radius:18px; }
"""


def esc_title(title: str, highlight: str | None) -> str:
    t = html.escape(title)
    if highlight:
        h = html.escape(highlight)
        t = t.replace(h, f"<em>{h}</em>", 1)
    return t.replace("\n", "<br>")


def build(spec: dict) -> str:
    title = esc_title(spec["title"], spec.get("highlight"))
    if spec["layout"] == "list":
        items = "".join(
            f'<li><div class="tick">✓</div><div>{html.escape(i)}</div></li>' for i in spec["items"]
        )
        middle = f"<ul>{items}</ul>"
    else:
        middle = f'<p class="body">{html.escape(spec["body"])}</p>'
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="bg1"></div><div class="bg2"></div><div class="grid"></div>
<div class="wrap">
  <div class="brand"><div class="logo">N</div><div>nobetik<span>.com</span></div></div>
  <div class="eyebrow">{html.escape(spec["eyebrow"])}</div>
  <h1>{title}</h1>
  {middle}
  <div class="spacer"></div>
  <div class="cta"><b>{html.escape(spec["cta"])}</b><i>nobetik.com</i></div>
</div></body></html>"""


def main(paths: list[str]) -> None:
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        for path in paths:
            spec = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
            page.set_content(build(spec), wait_until="networkidle")
            page.wait_for_timeout(300)
            out = OUT / f'{spec["slug"]}.png'
            page.screenshot(path=str(out), full_page=False)
            print(out)
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1:])
