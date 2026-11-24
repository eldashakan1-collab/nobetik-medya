# Reels dizileri — rehber

## Seri planı (kullanıcı kararı, 24 Kasım)
- **Bölüm 1–4 (28 Kas – 19 Ara 2026): yalnızca "Gece 03:17".** Takip alışkanlığı kurmak için.
- **26 Aralık 2026'dan itibaren dönüşümlü:** her cumartesi sıradaki seri, şu döngüyle:
  1. "Gece 03:17" (gece nöbeti hikâyesi — aşağıdaki rehber)
  2. "Hemşire Sözlüğü" — sadece hemşirelerin bildiği bir cümle/kelime ("Bir bakıverir misin?", "Sakin geçsin", "Devirde bir şey yok"): büyük kinetik tipografi ile sözlük maddesi (kelime · okunuş · "gerçek anlamı") + aynı karakterlerle 2–3 saniyelik mini sahne. Mizahi, etiketlemeye uygun.
  3. "Gündüz 08:00" — aynı karakterler, gün içi bir an: nöbet devri, vizit, ilaç saati, hasta yakını, servis koşturması. Mekân aynı istasyon, gündüz ışığı (açık gökyüzü, tint yok).
  4. "POV" — üstte "POV:" ile başlayan tek cümle ("POV: Nöbet devrinde 'bir şey yok' dendi") + kısa, hızlı kurgulu sahne; trend formatın meslek versiyonu (trend ses yok).
- **Özel gün önceliği:** o hafta bir özel gün varsa (26 Ara haftası Yılbaşı, Hemşireler Haftası 12–18 Mayıs, bayramlar) döngü yerine o güne özel bölüm yapılır; seri adı döngüdeki sıradaki seri olur.
- Her seri ayrı numaralanır (ör. "HEMŞİRE SÖZLÜĞÜ · NO 1"); açılış kartı ve kapanış sorusu her seride var; karakterler (Defne, Can) ve çizim stili her seride aynı.
- Performans: dört haftada bir Metricool Reels verilerine (izlenme, izlenme süresi, paylaşım, kaydetme) bak; en zayıf seriyi döngüden çıkarıp yerine yeni bir seri fikri dene ve bu dosyaya not düş.

# "Gece 03:17" — dizi rehberi

Haftalık 30 saniyelik animasyon Reels. Amaç tanıtım değil: hemşirelerin kendini gördüğü, paylaştığı, yorum yazdığı bir dizi. Nöbetik yalnızca son karede küçük logo.

## Sabitler
- Açılış (0–2,5 sn): lacivert zemin, "GECE NÖBETİ · BÖLÜM N", kehribar dev saat "03:17", altında Fraunces italik alt başlık (bölüm adı). Saat tıkırtısı.
- Mekân: hemşire istasyonu — pencere (gece ay, sabah güneş), "HASTA ÇAĞRI" paneli (12 zil), monitör (EKG), masa, çay.
- Hikâye yazıyla anlatılır (sesi kapalı izleyen anlasın): üstte kısa altyazı kutusu, karakter konuşmaları beyaz baloncuk.
- Kapanış (son 1,5 sn): "GECE 03:17" + izleyiciye soru (yorum/etiket) + küçük soluk logo.
- Ton: pozitif mizah, dayanışma, meslek gururu. Hasta mahremiyeti, kötü haber, şiddet, kurum eleştirisi yok.
- Ses: `tools/sfx.py` ile sentez efektler (tik, bip, zil, akor, whoosh). Kullanıcı Instagram'da trend ses ekleyebilir.

## Karakterler (görünüşleri sabit kalır)
Görsel stil (yapay zekâ görsel aracı için): yarı gerçekçi dijital illüstrasyon, sinematik yumuşak ışık, 9:16 dikey, hastane hemşire istasyonu gece mavi tonlar + sıcak masa lambası, temiz ve pozitif; marka/logo/yazı içermesin.
(Aşağıdaki gerçekçi tarifler yalnızca kullanıcı yapay zekâ görseli üretirse kullanılır. Otomatik bölümlerde karakterler `reels/gece-0317-bolum-1.html`'deki çizim haliyle aynen kalır: Defne lacivert forma #1E3A8A, koyu kahve topuz #3B2A20, ten #F2C6A0; Can açık mavi forma #60A5FA, kısa siyah saç #1F2937, ten #E8B48C, "ST" kartı.)
- **Defne** — 30'lu yaşlarda deneyimli servis hemşiresi. Lacivert hemşire forması, koyu kahverengi saç topuz, sıcak kahve gözler, hafif yorgun ama gülümseyen yüz, boynunda steteskop. Sakin, esprili, ekibin ablası.
- **Can** — 20'li yaşların başında stajyer erkek hemşire. Açık mavi forma, kısa siyah dağınık saç, buğday ten, göğsünde "Stajyer" kartı, heyecanlı ve biraz şaşkın ifade. Hevesli, her bölüm bir şey öğrenir.
- Gerekirse yeni yan karakterler eklenebilir; tasarım `reels/gece-0317-bolum-1.html`'deki düz vektör stilinde.

## Yayınlanan bölümler
KURAL: Bu tabloda tarihi o haftanın cumartesisine denk gelen bir bölüm varsa (Metricool'da olmasa bile) o hafta yeni Reels ÜRETME. Sıradaki bölüm numarası = tablodaki en büyük numara + 1.
| No | Tarih | Seri · Ad | Konu | Kapanış sorusu | Dosya |
| --- | --- | --- | --- | --- | --- |
| 1 | 28 Kas 2026 | Sakin bir gece | Stajyer "Ne sakin bir gece" der, tüm ziller çalar | Senin servisinde yasaklı kelime ne? | reels/gece-0317-bolum-1-sesli.mp4 |
| 2 | 5 Ara 2026 (kullanıcıya önceden gönderildi; Metricool'a KONMADI, kullanıcı kendisi paylaşacak) | Gece yemeği | 03:17'de yemek molası; her ilk lokmada bir zil; 06:52'de soğuk sarma, sıcak muhabbet | Senin serviste gece yemeği saat kaçta? | reels/gece-0317-bolum-2-sesli.mp4 |

## Fikir havuzu (kullanıldıkça listeden düş)
- Nöbet devri: "Bir şey yok" denen servis
- "Bir bakıverir misin?" — bir dakikalık iş, kırk dakika
- 12 saat sonra ayakkabıyı çıkarma anı
- Sabaha karşı 05:00 sessizliği ve ilk kuş sesi
- Yeni yatış saat 07:55'te gelir
- Yılbaşı gecesi 00:00 — serviste bir dilim pasta, bir dakikalık kutlama (31 Aralık haftası)
- Stajyer ilk kez damar yolunu tek seferde açar — tüm istasyon alkışlar
- Hasta yakınından gelen küçük bir teşekkür notu
