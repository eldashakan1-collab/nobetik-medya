# Nöbetik — Günlük onaylı üretim akışı (26 Kasım 2026'dan itibaren)

Kullanıcı kararı (26 Kas 2026): Her içerik **yayından tam 1 hafta önce** kullanıcının onayına sunulur. Onaylanınca sıraya alınır. Örnek: Perşembe 26 Kasım'da, 3 Aralık Perşembe'nin içeriği onaya gelir.

Sıfır onay dönemi bitti. Daha önce onaylanıp sıraya alınmış içerikler (2 Aralık'a kadar olanlar) olduğu gibi kalır.

## Haftalık ritim (Europe/Istanbul)
| Gün | İçerik | Saat |
|---|---|---|
| Salı | Gönderi (tek görsel ya da karusel; Cuma'dakinden farklı tür) | 10:00 |
| Perşembe | Story, 1–3 kare, 5'er dk arayla | 19:00 |
| Cuma | Gönderi | 10:00 |
| Cumartesi | Reels, 30 sn çizim animasyon, seslendirmeli | 10:00 |
Pazartesi, Çarşamba ve Pazar'ın hedef günü boş: o günler üretim yok, kullanıcıya mesaj yok.

## Her gün 05:00'te
1. HEDEF = bugün + 7 gün. Hedefin haftanın hangi günü olduğuna bak; tabloda slot yoksa sessizce bitir.
2. Metricool getScheduledPosts (brandId "8333739", timezone Europe/Istanbul) ile hedef günü kontrol et. O slot için zaten bir içerik (taslak ya da zamanlanmış) varsa yeniden üretme; yalnızca hâlâ taslaksa onu tekrar onaya sun.
3. Repo: add_repo (eldashakan1-collab/nobetik-medya, push), `git clone --depth 1` → /home/claude/nobetik-medya. Önce STRATEJI.md, reels/BOLUMLER.md ve bu dosyayı oku, harfiyen uy.
4. Gündem ve trend: web aramasıyla Türkiye hemşirelik gündemi, hedef haftanın özel günleri, ay sonu/ay başı liste dönemi; güncel Instagram Reels trend listeleri (ör. later.com/blog/instagram-reels-trends). Uygun akımı hemşirelik diline uyarla; telifli müzik ekleme; siyaset/alay/hasta mahremiyeti/şiddet yok.
5. Üret:
   - Gönderi/Story: HTML/SVG + Playwright (/usr/bin/google-chrome) + Fontsource fontları (Inter, Fraunces, Caveat; `npm i @fontsource/inter @fontsource/fraunces @fontsource/caveat` /home/claude/fonts altında). Gönderi 1080×1350 (karusel 5–8 slayt), Story 1080×1920 (üst 200 px, alt 260 px güvenli alan, ÇIKARTMA YOK). Logo küçük: açık zeminde ~32 px, koyu zeminde yarı saydam beyaz küçük kartta ~24 px. Örnek: tasarim/onay/2026-12-03-story-*.html. Her PNG'yi Read ile aç; taşma, kesilme, Türkçe karakter, yazım, kontrast kontrolü.
   - Reels: reels/BOLUMLER.md seri planı ve istisnaları. Hedef Cumartesi için BOLUMLER.md "Yayınlanan bölümler"de hazır bir bölüm varsa (ör. 5 Aralık = Bölüm 2, reels/gece-0317-bolum-2-sesli.mp4) yeni üretme, onu onaya sun. Yoksa şablon reels/gece-0317-bolum-2.html; tools/reel_build.py ile önizleme ve video; tools/sfx.py ile efekt sesi.
   - Seslendirme sırası: (a) ElevenLabs (eleven_v4; Can = Duygu "Rnbz9MZgX4nkmTzXgezp", Defne = Esin "vevaMEPHZ5tHlFtS3YPm", anlatıcı = Nergis "hALSUJsnqdqp1bY0quM2"; aynı çağrıyı tekrar etme; full_res_url'yi curl ile indir) → indirilemez/yoksa/meşgulse (b) Speko audio_synthesize (tr, cartesia; Can = Aykut "91e91d74-8eb4-43cd-97d3-7466c21db00d", Defne = Azra "0f95596c-09c4-4418-99fe-5c107e0713c0", anlatıcı = Aylin "bb2347fe-69e9-4810-873f-ffd759fe8420"; WAV yerel yoldan kopyalanır) → (c) yalnızca efekt sesi ve kullanıcıya not. Bölüm içinde tek sağlayıcı. Miks: loudnorm I=-17, adelay, sidechaincompress, alimiter 0.95.
   - Yalnızca doğrulanmış ürün özellikleri; "NöbetiX" asla; en fazla 5 hashtag.
6. Yükle: benzersiz adlarla gorseller/ ya da reels/, commit (sonunda "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"), push, her raw URL için curl 200.
7. Metricool'a **TASLAK** olarak ekle: createScheduledPost, date = hedef gün ve saat (+03:00), info: **draft TRUE**, autoPublish TRUE, providers instagram, media raw URL'ler, mediaAltText, publicationDate, descendants [], firstCommentText "", shortener false, smartLinkData {ids:[]}; instagramData POST/STORY/REEL (REEL'de showReelOnFeed true + videoCoverMilliseconds 1500; STORY'de text ""), isAiGenerated false. (Metricool ücretsiz plan "onaya gönder" özelliğini desteklemiyor; taslak yayınlanmaz.)
8. Kullanıcıya ONAY MESAJI gönder (SendUserFile ile görseller/video, sonra SendUserMessage):
   "📅 Onay: <gün tarih saat> · <tür>" + kısa konsept + açıklama metninin tamamı + "Onaylıyorsan 'onay' yaz; değişiklik istiyorsan ne değişsin yaz. İstersen Metricool'da taslağı açıp 'Zamanla'ya basarak da onaylayabilirsin." Aynı gün daha önce onaylanmamış taslak varsa onları da listele.
9. Kullanıcı bu oturumda "onay" derse: getScheduledPosts ile taslağı bul, updateScheduledPost ile **draft FALSE** yap (geri kalan her alan aynı), doğrula ve "✅ Sıraya alındı" de. Değişiklik isterse düzelt, yeniden yükle, taslağı güncelle, tekrar onaya sun.
10. Hata olursa kısa Türkçe mesajla bildir; yine de onaylanmamış hiçbir şeyi yayına alma.
