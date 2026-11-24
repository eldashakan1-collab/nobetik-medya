# Nöbetik Instagram — Kalıcı çalışma prensipleri

Kaynak: kullanıcının kreatif brief'i (24 Kasım 2026) ve onaylanan strateji dokümanı
https://claude.ai/artifact/NqAaBupVgsZD4CkNzSgzvi

## Haftalık ritim (onaylı)
| İçerik | Gün | Saat (Europe/Istanbul) | Metricool |
| --- | --- | --- | --- |
| 1 gönderi (tek görsel ya da karusel) | Salı | 10:00 | POST, draft:true, autoPublish:true |
| 1 Story (1–3 kare) | Perşembe | 19:00 | STORY, draft:true, autoPublish:false |
| 1 Reels — "Gece 03:17" dizisi | Cumartesi | 10:00 | REEL, draft:true, autoPublish:false (yarı otomatik, aşağıya bak) |

Hiçbir şey kullanıcı onayı olmadan yayınlanmaz: her zaman `draft: true`.

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

## Reels üretim akışı (yarı otomatik — kullanıcı kararı, 24 Kasım)
- Trend ses EKLENMEZ. Ses = Türkçe seslendirme (anlatıcı) + karakter konuşmaları + sentez efektler. Tüm konuşmalar altyazıda da yazılı.
- Karakterler eski @nobetik videolarındaki gibi daha gerçekçi (yarı gerçekçi dijital illüstrasyon). Bu görseller bir yapay zekâ görsel aracında KULLANICI tarafından üretilir.
- Sesler KULLANICI tarafından kaydedilir (telefonla) ya da bir yapay zekâ ses aracıyla üretilir. Bu ortamda doğal Türkçe TTS yok.
- Haftalık görev her pazar: bir sonraki bölümün "üretim paketini" hazırlar — senaryo (saniye saniye), seslendirme ve diyalog metinleri (satır satır, kim söylüyor, kaç saniye), her sahne için görsel üretim prompt'ları (karakter tarifleri sabit), kapak fikri; `reels/paket-bolum-N.md` olarak depoya koyar ve kullanıcıya gönderir.
- Kullanıcı görselleri (`reels/varliklar/bolum-N/sahne-*.png`) ve sesleri (`.../ses-*.m4a|mp3`) gönderince montaj yapılır: Ken Burns/parallax hareket, altyazı, ses miksajı, son kare, Metricool REEL taslağı.
