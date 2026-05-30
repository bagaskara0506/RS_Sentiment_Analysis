# Proyek Analisis Sentimen Rumah Sakit di Tangerang (Kota & Kabupaten Tangerang)

Proyek ini bertujuan untuk mengekstraksi, membersihkan, dan menganalisis ulasan pasien dari Google Maps (Google Reviews/ Ulasan Google Maps) terhadap 5 rumah sakit di wilayah Kota Tangerang dan Kabupaten Tangerang. Melalui analisis sentimen dan pemrosesan bahasa alami (NLP), proyek ini memvisualisasikan tingkat kepuasan pasien dan mengidentifikasi akar masalah dari keluhan pasien terhadap rumah sakit.

## Business Insights (Wawasan Bisnis)

### Key Insight :

Berdasarkan dashboard visualisasi yang telah dibangun menggunakan 780 ulasan, berikut adalah wawasan utama yang didapatkan :

- Pemimpin Kepuasan (Top Performers) : Mayapada Hospital Tangerang (MHTG) memimpin mutlak dengan rata-rata rating 4.8 / 5.0 dan mendominasi proporsi sentimen positif hingga 94.94%.

- RS Sari Asih Karawaci menyusul di posisi kedua dengan rating 4.6 dan sentimen positif sebesar 87.34%.

- Area Perbaikan Kritis (Bottleneck): Tiga rumah sakit lainnya memerlukan perhatian serius terkait kepuasan pasien, di mana tingkat sentimen negatif menembus angka di atas 30%:

- Ciputra Hospital CitraRaya & Primaya Hospital Tangerang : Rata-rata rating terendah (3.6) dengan tingkat keluhan tertinggi (Ciputra Hospital CitraRaya : 32.91% & Primaya Hospital Tangerang : 31.76%).

- RS EMC Tangerang : Rata-rata rating 3.7 dengan keluhan sebesar 31.65%.

- Akar Masalah (Root Cause Analysis) : Berdasarkan visualisasi WordCloud dan eksplorasi data pada ulasan berlabel Negatif (Bintang 1 & 2), keluhan pasien terpusat pada Manajemen Waktu, Pelayanan Administrasi, Bad Hospitality frontliner. Kata kunci utama yang mendominasi keluhan adalah: "jam", "Pelayanan", "dokter", "perawat","tunggu", "antrian", "farmasi", "Pendaftaran" dan "BPJS".

### Business Recommendations :

Rekomendasi tindakan strategis yang dapat diambil oleh pihak manajemen Rumah Sakit (terutama Ciputra, Primaya, dan EMC) adalah :

- Optimalisasi Waktu Tunggu (Queue Management): Mengevaluasi SLA (Service Level Agreement) untuk pendaftaran poli, pengambilan obat di farmasi, serta ketepatan waktu kedatangan dokter sesuai jadwal.

- Evaluasi Alur Pasien BPJS: Tingginya kemunculan kata "BPJS" pada ulasan berating rendah mengindikasikan adanya kendala atau penumpukan pada loket administrasi asuransi sosial pemerintah "BPJS". Diperlukan penambahan loket atau digitalisasi pendaftaran agar pasien BPJS tidak merasa prosesnya diperlambat atau diabaikan.

- Peningkatan Komunikasi Petugas (Frontliner): Banyak keluhan menyoroti petugas kasir, pendaftaran, dan tenaga medis dokter serta perawat yang dinilai kurang tanggap. Pelatihan komunikasi (hospitality training) untuk garda terdepan sangat disarankan.

## Proses Analisis

1. Data Extraction (Web Scraping)
   Tahap ini mengambil data mentah dari Google Maps menggunakan bot otomatis dengan proses berikut :
   - Membuat folder RS_Sentiment_Analysis.
   - Menginstal library Python yang dibutuhkan: pip install selenium pandas beautifulsoup4 webdriver-manager.
   - Membuat skrip ekstraksi data (scraper_gmaps.py) untuk mengambil ulasan secara otomatis.
   - Menjalankan skrip otomatisasi.
   - Menyimpan data hasil scraping dalam format CSV dengan nama Data_Review_5_RS_Tangerang.csv.

2. Data Cleaning & NLP (Natural Language Processing)
   Pada tahap ini, data teks mentah dibersihkan dan diproses menggunakan teknik NLP :
   - Text Cleansing : Menghapus emoji, tanda baca, angka, tautan (URL), dan mengubah semua teks menjadi huruf kecil (lowercase).
   - Sentiment Labeling : Melabeli setiap baris ulasan secara otomatis berdasarkan rating bintang. Skema: Bintang 4 & 5 = Positif, Bintang 3 = Netral, Bintang 1 & 2 = Negatif.
   - stopwords Removal : Menghapus kata hubung bahasa Indonesia (seperti dan, di, ke, yang, dari). Tujuannya adalah untuk mengekstraksi kata kunci keluhan pasien pada ulasan negatif untuk divisualisasikan dalam WordCloud.
   - Library yang digunakan : nltk, wordcloud, matplotlib.
   - Output : Dataset bersih yang disimpan sebagai Data_Review_Clean_Sentiment.csv.

3. Data Visualization (Dashboarding)
   Tahap akhir adalah mengubah data bersih menjadi informasi visual interaktif menggunakan Tableau. Dengan proses berikut :
   - Mengimpor sumber data Data_Review_Clean_Sentiment.csv ke Tableau.
   - Membuat Sheet "Avg Rating per RS" (Bar Chart) untuk menampilkan rata-rata rating per rumah sakit.
   - Membuat Sheet "Distribusi Sentimen" (100% Stacked Bar Chart) untuk membandingkan persentase kepuasan.
   - Membuat Sheet "Review Details Table" untuk menampilkan teks ulasan asli (Original Review) sebagai bukti pendukung, dilengkapi dengan fitur penyaringan (filtering).
   - Merakit seluruh komponen menjadi Interactive Dashboard final berjudul "HOSPITAL PATIENT SENTIMENT ANALYSIS", yang juga dilengkapi dengan gambar WordCloud.

## Struktur Folder

Berikut adalah struktur direktori dari proyek analisis sentimen ini :

- README.md : File dokumentasi utama proyek.
- dashboards/ : Berisi aset gambar hasil visualisasi.
- HOSPITAL PATIENT SENTIMENT ANALYSIS.png : Hasil ekspor dashboard sentimen pasien dari visualisasi dashboard di tableau.
- WordCloud.png : Visualisasi word cloud dari teks ulasan negatif.
- data_processing/ : Direktori penyimpanan dataset.
- Data_Review_5_RS_Tangerang.csv : Dataset mentah (raw data) review dari 5 Rumah Sakit.
- Data_Review_Clean_Sentiment.csv : Dataset yang sudah melalui tahap cleaning dan pelabelan sentimen.
- notebooks/ : Folder berisi skrip Python dan file workbook visualisasi.
- Data Cleaning&NLP/ : Folder skrip untuk pemrosesan teks.
- nlp_processing.py : Skrip utama untuk proses pembersihan data dan NLP.
- Data_Extraction/ : Folder skrip untuk proses scraping ekstraksi/pengambilan data.
- scraper_gmaps.py : Skrip untuk melakukan scraping review dari Google Maps.
- Visualisasi Tableau/ : Folder file tableau pembuatan dashboard.
- RS_Sentiment_Analysis.twbx : File workbook Tableau.

## Teknologi yang Digunakan

**Bahasa Pemrograman :** Python 3.13.2

**Library Data Extraction (Web Scraping) :**

- Selenium (`from selenium import webdriver`)
- BeautifulSoup4 (`from bs4 import BeautifulSoup`)
- WebDriver Manager (`from webdriver_manager.chrome import ChromeDriverManager`)

**Library Data Manipulation & Cleaning :**

- Pandas (`import pandas as pd`)
- Regex/Regular Expressions (`import re`)

**Library Natural Language Processing (NLP) :**

- NLTK (`import nltk` dan `from nltk.corpus import stopwords`)

**Library Exploratory Data Analysis (EDA) & Visualisasi :**

- Matplotlib (`import matplotlib.pyplot as plt`)
- WordCloud (`from wordcloud import WordCloud`)

**Data Visualization & Dashboarding :** Tableau Public

**Code Editor / IDE :** Visual Studio Code (VS Code)

**Version Control :** Git & GitHub

## Tautan :

**Lihat Dashboard Interaktif HOSPITAL PATIENT SENTIMENT ANALYSIS :** [View on Tableau Public](https://public.tableau.com/app/profile/satria.bagaskara4685/viz/RS_Sentiment_Analysis/HOSPITALPATIENTSENTIMENTANALYSIS)

**Lihat Artikel :** [Medium](https://medium.com/@satriadevopsindonesia/hospital-patient-sentiment-analysis-using-the-google-maps-review-data-scraping-method-de76755d8c2e)

**Lihat Profesional Karir :** [linkedin](https://www.linkedin.com/in/satria-bagaskara/)
