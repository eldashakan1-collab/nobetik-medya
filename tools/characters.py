"""Gece 03:17 karakterlerini (Defne, Can) detaylı çizimle değiştirir.

Kullanım: python3 tools/characters.py reels/<bolum>.html
- <g id="defne"> ve <g id="can"> gruplarını yeni detaylı sürümle değiştirir (id'ler ve animasyon bağları korunur).
- Can'ı masanın arkasına alır (masa gövdeyi kapatır), gradyan tanımlarını ve ortam ışığını ekler.
"""
import re
import sys

DEFS = '''
    <radialGradient id="skinD" cx="0.45" cy="0.4" r="0.7"><stop offset="0" stop-color="#F8D6B4"/><stop offset="0.75" stop-color="#EDBE96"/><stop offset="1" stop-color="#D9A07A"/></radialGradient>
    <radialGradient id="skinC" cx="0.45" cy="0.4" r="0.7"><stop offset="0" stop-color="#EBC29B"/><stop offset="0.75" stop-color="#D6A57C"/><stop offset="1" stop-color="#BF8962"/></radialGradient>
    <linearGradient id="hairD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#57402F"/><stop offset="1" stop-color="#2A1B12"/></linearGradient>
    <linearGradient id="hairC" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#34343D"/><stop offset="1" stop-color="#0E0E12"/></linearGradient>
    <linearGradient id="dScrub" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2D4FA8"/><stop offset="1" stop-color="#16245A"/></linearGradient>
    <linearGradient id="cScrub" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8CC0FC"/><stop offset="1" stop-color="#4A87E0"/></linearGradient>
    <radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FCD34D" stop-opacity="0.22"/><stop offset="1" stop-color="#FCD34D" stop-opacity="0"/></radialGradient>
'''

DEFNE = '''<g id="defne">
      <rect x="212" y="1035" width="236" height="210" rx="44" fill="#0B1226" opacity="0.6"/>
      <path d="M232 1250 Q230 1088 300 1068 L360 1068 Q430 1088 428 1250 Z" fill="url(#dScrub)"/>
      <path d="M262 1110 Q258 1180 268 1250" stroke="#132158" stroke-width="4" fill="none" opacity="0.7"/>
      <path d="M398 1110 Q402 1180 392 1250" stroke="#132158" stroke-width="4" fill="none" opacity="0.7"/>
      <path d="M307 1038 L353 1038 L357 1082 Q330 1096 303 1082 Z" fill="url(#skinD)"/>
      <path d="M303 1060 Q330 1076 357 1060 L357 1072 Q330 1090 303 1072 Z" fill="#B97C58" opacity="0.45"/>
      <path d="M298 1070 L330 1118 L362 1070 Z" fill="url(#skinD)"/>
      <path d="M294 1068 L330 1124 L366 1068" fill="none" stroke="#101C47" stroke-width="5" stroke-linejoin="round"/>
      <path d="M291 1074 Q276 1150 309 1180 M369 1074 Q384 1150 351 1180" stroke="#475569" stroke-width="6" fill="none" stroke-linecap="round"/>
      <path d="M309 1180 Q330 1198 351 1180" stroke="#475569" stroke-width="6" fill="none"/>
      <circle cx="330" cy="1198" r="12" fill="#CBD5E1" stroke="#64748B" stroke-width="3"/>
      <rect x="372" y="1152" width="36" height="42" rx="5" fill="none" stroke="#101C47" stroke-width="3"/>
      <rect x="381" y="1134" width="6" height="30" rx="2" fill="#E5E7EB"/><rect x="391" y="1138" width="5" height="26" rx="2" fill="#F59E0B"/>
      <rect x="252" y="1140" width="42" height="54" rx="6" fill="#F8FAFC"/><rect x="258" y="1149" width="30" height="11" rx="2" fill="#1D4ED8"/><rect x="258" y="1166" width="22" height="5" rx="2" fill="#94A3B8"/><rect x="258" y="1176" width="26" height="5" rx="2" fill="#94A3B8"/>
      <circle cx="330" cy="893" r="37" fill="url(#hairD)"/>
      <path d="M306 880 Q330 862 354 880" stroke="#7A5A42" stroke-width="3" fill="none" opacity="0.8"/>
      <ellipse cx="264" cy="996" rx="11" ry="17" fill="url(#skinD)"/><ellipse cx="396" cy="996" rx="11" ry="17" fill="url(#skinD)"/>
      <circle cx="264" cy="1012" r="3" fill="#F1F5F9"/><circle cx="396" cy="1012" r="3" fill="#F1F5F9"/>
      <ellipse cx="330" cy="992" rx="66" ry="78" fill="url(#skinD)"/>
      <rect x="311" y="921" width="38" height="10" rx="5" fill="#1D4ED8"/>
      <path d="M262 996 Q256 912 330 906 Q404 912 398 996 Q393 954 362 942 Q342 962 300 950 Q272 960 262 996 Z" fill="url(#hairD)"/>
      <path d="M298 926 Q330 914 374 930" stroke="#7A5A42" stroke-width="3" fill="none" opacity="0.8"/>
      <path d="M268 986 Q262 1030 278 1052" stroke="#3B2A20" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M291 962 Q305 954 320 961" stroke="#3B2A20" stroke-width="5" fill="none" stroke-linecap="round"/>
      <path d="M340 961 Q355 954 369 962" stroke="#3B2A20" stroke-width="5" fill="none" stroke-linecap="round"/>
      <ellipse id="dWl" cx="305" cy="990" rx="14" ry="10" fill="#FFFFFF"/><ellipse id="dWr" cx="355" cy="990" rx="14" ry="10" fill="#FFFFFF"/>
      <g id="dEyes"><ellipse id="dEl" cx="305" cy="991" rx="6.5" ry="7.5" fill="#4A2C17"/><ellipse id="dEr" cx="355" cy="991" rx="6.5" ry="7.5" fill="#4A2C17"/></g>
      <circle cx="307.5" cy="988" r="2.2" fill="#FFFFFF"/><circle cx="357.5" cy="988" r="2.2" fill="#FFFFFF"/>
      <path d="M290 985 Q305 975 320 984" stroke="#1F2937" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <path d="M340 984 Q355 975 370 985" stroke="#1F2937" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <path d="M330 998 Q325 1016 335 1020" stroke="#C08460" stroke-width="3" fill="none" stroke-linecap="round"/>
      <ellipse cx="286" cy="1020" rx="13" ry="8" fill="#F28B82" opacity="0.28"/><ellipse cx="374" cy="1020" rx="13" ry="8" fill="#F28B82" opacity="0.28"/>
      <path id="dMouth" d="M312 1034 Q330 1044 348 1034" stroke="#B4535A" stroke-width="5" fill="none" stroke-linecap="round"/>
    </g>'''

CAN = '''<g id="can">
      <path d="M-100 300 Q-102 42 -40 14 L40 14 Q102 42 100 300 Z" fill="url(#cScrub)"/>
      <path d="M-66 80 Q-72 180 -62 300 M66 80 Q72 180 62 300" stroke="#3F7AD1" stroke-width="4" fill="none" opacity="0.7"/>
      <path d="M-25 -16 L25 -16 L27 24 Q0 40 -27 24 Z" fill="url(#skinC)"/>
      <path d="M-27 4 Q0 20 27 4 L27 16 Q0 34 -27 16 Z" fill="#A9714C" opacity="0.45"/>
      <path d="M-34 16 L0 66 L34 16 Z" fill="url(#skinC)"/>
      <path d="M-37 14 L0 72 L37 14" stroke="#3B82F6" stroke-width="5" fill="none" stroke-linejoin="round"/>
      <path d="M-30 20 L-12 140 M30 20 L12 140" stroke="#1D4ED8" stroke-width="5" stroke-linecap="round"/>
      <rect x="-32" y="138" width="64" height="74" rx="8" fill="#F8FAFC"/><rect x="-24" y="148" width="48" height="14" rx="3" fill="#1D4ED8"/>
      <text x="0" y="192" text-anchor="middle" font-family="Inter" font-weight="800" font-size="14" fill="#1E3A8A">STAJYER</text>
      <ellipse cx="-66" cy="-64" rx="11" ry="17" fill="url(#skinC)"/><ellipse cx="66" cy="-64" rx="11" ry="17" fill="url(#skinC)"/>
      <ellipse cx="0" cy="-66" rx="64" ry="76" fill="url(#skinC)"/>
      <path d="M-68 -78 Q-76 -150 -8 -154 Q62 -162 70 -94 Q64 -112 52 -108 L58 -126 Q36 -116 30 -134 Q14 -114 0 -134 Q-12 -112 -30 -128 Q-34 -106 -52 -120 Q-52 -98 -68 -78 Z" fill="url(#hairC)"/>
      <path d="M-34 -138 Q-6 -150 30 -140" stroke="#4B4B57" stroke-width="3" fill="none" opacity="0.8"/>
      <path d="M-43 -92 Q-27 -101 -10 -93" stroke="#111827" stroke-width="6" fill="none" stroke-linecap="round"/>
      <path d="M10 -93 Q27 -101 43 -92" stroke="#111827" stroke-width="6" fill="none" stroke-linecap="round"/>
      <ellipse cx="-25" cy="-66" rx="13" ry="9.5" fill="#FFFFFF"/><ellipse cx="25" cy="-66" rx="13" ry="9.5" fill="#FFFFFF"/>
      <circle cx="-25" cy="-65" r="6.5" fill="#2B1A10"/><circle cx="25" cy="-65" r="6.5" fill="#2B1A10"/>
      <circle cx="-23" cy="-68" r="2" fill="#FFFFFF"/><circle cx="27" cy="-68" r="2" fill="#FFFFFF"/>
      <path d="M-39 -71 Q-25 -80 -11 -71" stroke="#111827" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <path d="M11 -71 Q25 -80 39 -71" stroke="#111827" stroke-width="3.5" fill="none" stroke-linecap="round"/>
      <path d="M0 -58 Q-6 -40 5 -36" stroke="#A9714C" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path id="cMouth" d="M-20 -30 Q0 -14 20 -30" stroke="#8A3B2E" stroke-width="5" fill="none" stroke-linecap="round"/>
    </g>'''


def cut_group(s, gid):
    start = s.index(f'<g id="{gid}"')
    i, depth = start, 0
    while True:
        o = s.find('<g', i); c = s.find('</g>', i)
        if o != -1 and o < c:
            depth += 1; i = o + 2
        else:
            depth -= 1; i = c + 4
            if depth == 0:
                return start, i


def main(path):
    s = open(path, encoding='utf-8').read()
    if 'id="skinD"' not in s:
        s = s.replace('</defs>', DEFS + '  </defs>', 1)
    a, b = cut_group(s, 'defne'); s = s[:a] + DEFNE + s[b:]
    a, b = cut_group(s, 'can'); s = s[:a] + CAN + s[b:]
    # Can masanın arkasında olsun
    a, b = cut_group(s, 'can'); can = s[a:b]; s = s[:a] + s[b:]
    d = s.index('    <!-- desk -->'); s = s[:d] + '    ' + can + '\n' + s[d:]
    # ortam: lamba ışığı ve nesne gölgeleri
    if 'url(#lamp)' not in s:
        s = s.replace('<rect x="0" y="1450" width="1080" height="470" fill="#0A1228"/>',
                      '<rect x="0" y="1450" width="1080" height="470" fill="#0A1228"/>\n    <circle cx="470" cy="1090" r="460" fill="url(#lamp)"/>', 1)
        s = s.replace('<g id="tea">', '<ellipse cx="485" cy="1162" rx="46" ry="7" fill="#020617" opacity="0.35"/>\n    <g id="tea">', 1)
    # göz animasyonu: iris küçük, şaşkınlıkta göz akı da büyüsün
    s = s.replace("const ry=wide?16:8, rx=wide?12:7;", "const ry=wide?9.5:7.5, rx=wide?8.5:6.5;")
    s = s.replace("['dEl','dEr'].forEach(e=>{$(e).setAttribute('ry',ry);$(e).setAttribute('rx',rx)});",
                  "['dEl','dEr'].forEach(e=>{$(e).setAttribute('ry',ry);$(e).setAttribute('rx',rx)});['dWl','dWr'].forEach(e=>{$(e).setAttribute('ry',wide?15:10);$(e).setAttribute('rx',wide?16:14)});")
    s = s.replace("$(e).setAttribute('ry',startled?14:8);$(e).setAttribute('rx',startled?11:7);$(e).setAttribute('cy',look?984:992)",
                  "$(e).setAttribute('ry',startled?9.5:7.5);$(e).setAttribute('rx',startled?8.5:6.5);$(e).setAttribute('cy',look?986:991)});['dWl','dWr'].forEach(e=>{$(e).setAttribute('ry',startled?15:10);$(e).setAttribute('rx',startled?16:14)")
    open(path, 'w', encoding='utf-8').write(s)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
        print('ok', p)
