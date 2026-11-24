# Nöbetik Instagram — Kalıcı çalışma prensipleri

Kaynak: kullanıcının kreatif brief'i (24 Kasım 2026) ve onaylanan strateji dokümanı
https://claude.ai/artifact/NqAaBupVgsZD4CkNzSgzvi

## Haftalık ritim (onaylı)
| İçerik | Gün | Saat (Europe/Istanbul) | Metricool |
| --- | --- | --- | --- |
| 2 gönderi (tek görsel ya da karusel; biri tercihen karusel) | Salı ve Cuma | 10:00 | POST, draft:false, autoPublish:true |
| 1 Story (1–3 kare, çıkartmasız) | Perşembe | 19:00 | STORY, draft:false, autoPublish:true |
| 1 Reels — "Gece 03:17" dizisi (çizim animasyon) | Cumartesi | 10:00 | REEL, draft:false, autoPublish:true |

SIFIR ONAY (kullanıcı kararı, 24 Kasım): her şey otomatik yayınlanır. Kullanıcıya yalnızca paylaşım bildirimi gider ("Nöbetik yayın bildirimi" görevi). Bu yüzden kalite kontrolü ve yalnızca doğrulanmış bilgi kuralı her zamankinden sıkı uygulanır. Story'lerde çıkartma (anket, soru, link) kullanılmaz; çağrı metinle yapılır ("mesaj olarak gönder", "link profilde").

## Marka
- Ad yalnızca **Nöbetik**. "NöbetiX" asla kullanılmaz.
- Logo: `tasarim/nobetik-logo.png` (şeffaf). Küçük ve geri planda: açık zeminde yükseklik ~32 px, opaklık 0.9; mavi/koyu zeminde yarı saydam beyaz küçük kart içinde ~24 px. Logo bozulmaz, renkleri değiştirilmez.
- Renkler: ana mavi #1D4ED8 (#2563EB); zemin beyaz / #EFF6FF; metin #1F2937; vurgu yeşil #10B981 (otomatik planlayıcı), kehribar #F59E0B (gündüz, kontrollü çizelge), mor #7C3AED (dijital kura); gece temaları #0B1430–#1E3A8A.
- Yazı: başlık Inter 800–900, gövde Inter; editorial ikinci ses Fraunces (italik). El yazısı gerekirse Caveat.
- Ses tonu: "Meslektaşın gibi konuşur, çözüm gibi davranır." Empati evet; öfke, korku, suçluluk, küçümseme, rakip kötüleme, siyaset/sendika/şiddet gündemi hayır.

## Doğrulanmış ürün iddiaları (yalnızca bunlar)
Ücretsiz · kayıtlı bilgilerle liste ~30 saniyede (kayıtlı kullanıcılar) · en az 50 liste dener, 40'tan fazla kurala göre puanlar, en iyi 3 listeyi sunar · Otomatik Planlayıcı ve Kontrollü Çizelge · gündüz/gece dengesi, mesai adaleti · eş durumu (uyum %90 altına düşerse uyarı) · dijital kura · nöbet çıkışı · izin/rapor/boş gün istekleri · istek toplama (telefondan, hatırlatma) · nöbet değişimi ve boşa çıkar · liste revize · analiz (1/3/6/12 ay) · yayınla + çalışan paneli, Excel/WhatsApp · bir hemşirenin kurduğu hikâye ("Nöbet listesi sadece bir plan değildir. Bir servisin huzurudur."). Başka rakam, özellik, yorum, hastane adı uydurulmaz.

## Yaratıcı kurallar
- Her görsel bir reklam fikri taşır; metafor mesajın kendisidir.
- Metafor kütüphanesi (yenilerini geliştir): terazi (denge), iki ibre (eş durumu), şeffaf kavanoz/zarf (kura), yapboz (40+ kural), kronometre (30 sn), trafik ışığı (uyarılar), defter → tablo (kuruluş hikâyesi), pil/sıra (analiz).
- Görsel dil rotasyonu, aynı hafta tekrar yok: minimalist → editorial → tipografik → sürrealist → hikâye → pozitif mizah. Zemin, başlık konumu, renk dağılımı her seferinde değişir.
- Yeni görsel üretmeden önce `gorseller/` ve `tasarim/` arşiviyle karşılaştır; benzerse yeni konsept.
- Kalite kontrol: özgün mü, önceki işlerden farklı mı, metafor anlamlı mı, marka korunuyor mu, ilk bakışta dikkat çekiyor mu, başlık-görsel uyumlu mu, kaydedilir/paylaşılır mı; Türkçe karakter ve yazım; taşma yok.
- Gerçekçi fotoğraf/sinematik görüntü üretilemez; bunlar için yalnızca brif yazılır.

## Açıklama (caption) kuralları
- Türkçe, kanca cümleyle başla; aranan kelimeler doğal geçsin (nöbet listesi, nöbet çizelgesi, sorumlu hemşire, gece nöbeti).
- Sonda soru ya da "meslektaşını etiketle / gönder" çağrısı.
- **En fazla 5 hashtag** (Instagram sınırı), boşluksuz.
- Reels'te ürün tanıtımı yok; gönderi ve Story'de yumuşak yönlendirme: "nobetik.com (link profilde)".

## Teknik
- Görseller: 1080×1350 (gönderi), 1080×1920 (Story/Reels). HTML/SVG ile tasarla, `tools/render_final.py` mantığıyla Playwright + gerçek fontlarla PNG'ye çevir (fontlar: `npm i @fontsource/inter @fontsource/fraunces @fontsource/caveat`).
- Barındırma: bu depo herkese açık; Metricool'a `https://raw.githubusercontent.com/eldashakan1-collab/nobetik-medya/main/<yol>` verilir. Değişen dosyaya yeni ad ver (önbellek).
- Reels: `tools/reel_build.py` (HTML + setT(t) → 30 fps kare → ffmpeg), ses `tools/sfx.py` (yalnızca sentez, telifsiz).

## Reels üretim akışı (tam otomatik — kullanıcı kararı, 24 Kasım)
- Trend ses yok. Ses: `tools/sfx.py` ile sentez efektler (oda sesi, bip, zil, tik, akor, whoosh). Doğal Türkçe seslendirme bu ortamda üretilemediği için konuşmalar altyazı ve konuşma balonlarıyla verilir.
- Görsel: düz vektör çizim animasyon, şablon `reels/gece-0317-bolum-1.html` (aynı karakterler, aynı mekân, aynı açılış/kapanış). Her bölüm yeni hikâye; sahneler, hareketler ve yeni küçük nesneler eklenebilir.
- Üretim: HTML + setT(t) → `tools/reel_build.py <html> video <çıktı.mp4>` (30 fps, 30 sn, 1080×1920) → cue.json + `tools/sfx.py` → ffmpeg ile birleştir (volume=1.9, alimiter). Önizleme kareleriyle kontrol et.
- Kullanıcı ileride gerçekçi görsel ve ses dosyası gönderirse o bölüm bunlarla yeniden kurgulanır.
