import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup data target ulasan RS
# Copy dan paste url tab ulasan di google maps pada url di bawah ini
rumah_sakit_list = [
  {
    "nama": "RS EMC Tangerang",
    "url": "https://www.google.com/maps/place/RS+EMC+Tangerang/@-6.1842138,106.6452307,17z/data=!4m8!3m7!1s0x2e69f9beaae8a477:0x501739509e5f571a!8m2!3d-6.1842138!4d106.6478056!9m1!1b1!16s%2Fg%2F11hm47hblj?entry=ttu&g_ep=EgoyMDI2MDUyMC4wIKXMDSoASAFQAw%3D%3D"
  },
  {
    "nama": "PRIMAYA HOSPITAL TANGERANG",
    "url": "https://www.google.com/maps/place/PRIMAYA+HOSPITAL+TANGERANG/@-6.214776,106.6280243,17z/data=!4m8!3m7!1s0x2e69f952ea1924c1:0xdac9e6180310b952!8m2!3d-6.214776!4d106.6305992!9m1!1b1!16s%2Fg%2F1vgl5cjv?entry=ttu&g_ep=EgoyMDI2MDUyMC4wIKXMDSoASAFQAw%3D%3D"
  },
  {
    "nama": "RS Sari Asih Karawaci",
    "url": "https://www.google.com/maps/place/RS+Sari+Asih+Karawaci/@-6.179311,106.6236518,17z/data=!4m8!3m7!1s0x2e69ff2ba76d32d3:0xd533af97acf7dac3!8m2!3d-6.179311!4d106.6262267!9m1!1b1!16s%2Fg%2F1tfswh9x?entry=ttu&g_ep=EgoyMDI2MDUyMC4wIKXMDSoASAFQAw%3D%3D"
  },
  {
    "nama": "Mayapada Hospital Tangerang (MHTG)",
    "url": "https://www.google.com/maps/place/Mayapada+Hospital+Tangerang+(MHTG)/@-6.2050294,106.6389436,17z/data=!4m8!3m7!1s0x2e69f947ce8c007b:0x7d0c6bb6ecab2153!8m2!3d-6.2050294!4d106.6415185!9m1!1b1!16s%2Fg%2F11f1212042?entry=ttu&g_ep=EgoyMDI2MDUyMC4wIKXMDSoASAFQAw%3D%3D"
  },
  {
    "nama": "Ciputra Hospital CitraRaya",
    "url": "https://www.google.com/maps/place/Ciputra+Hospital+CitraRaya/@-6.2493903,106.5189375,17z/data=!4m8!3m7!1s0x2e69ff2c6b78112d:0xc9462b4f04dc25ca!8m2!3d-6.2493903!4d106.5215124!9m1!1b1!16s%2Fg%2F1pzvbht09?entry=ttu&g_ep=EgoyMDI2MDUyMC4wIKXMDSoASAFQAw%3D%3D"
  }
]

# Tempat menyimpan hasil scraping
semua_ulasan = []

# Inisialisasi browser
print("Menyiapkan browser otomatis...")
options = webdriver.ChromeOptions()
options.add_argument('--lang=id') # Memaksa bahasa ke Indonesia
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15) #Bot menunggu proses maksimal 15 detik


# Proses Scraping (Looping setiap data rumah sakit)
for rs in rumah_sakit_list:
    print(f"\n========================================")
    print(f"Mulai mengambil data dari: {rs['nama']}...")
    driver.get(rs['url'])

    try:
        # Bot menunggu kotak scroll ulasan muncul dilayar
        print("Menunggu panel ulasan muncul...")
        scrollable_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde')))

        # Mulai proses scroll
        print("Mulai scrolling ke bawah untuk memuat lebih banyak ulasan...")
        for _ in range(15): #Scroll 15 kali
          driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
          time.sleep(2.5) #jeda loading agar data sempat masuk

    except Exception as e:
        print(f"Gagal memuat panel scroll utama. Mencoba metode alternatif...")
        try:
            for _ in range(15):
                ulasan_terlihat = driver.find_elements(By.CSS_SELECTOR, 'div.jftiEf')
                if ulasan_terlihat:
                    driver.execute_script('arguments[0].scrollIntoView(true);', ulasan_terlihat[-1])
                time.sleep(2.5)
        except:
            print("Metode alternatif juga gagal. Akan menarik ulasan yang terlihat saja.")

    # Ekstraksi Teks
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all('div', class_='jftiEf')

    jumlah_ditarik = 0
    for review in reviews:
        try:
            reviewer_name = review.find('div', class_='d4r55').text.strip()
            review_text_elem = review.find('span', class_='wiI7pd')
            review_text = review_text_elem.text.strip() if review_text_elem else ""

            review_time = review.find('span', class_='rsqaWe').text.strip()

            rating_elem = review.find('span', class_='kvMYJc')
            rating = rating_elem['aria-label'] if rating_elem else ""

            if review_text != "":
                semua_ulasan.append({
                "Rumah Sakit": rs['nama'],
                "Reviewer": reviewer_name,
                "Waktu": review_time,
                "Rating": rating,
                "Ulasan": review_text
                })
                jumlah_ditarik += 1
        except Exception as e:
            continue
    print(f"Selesai! Berhasil menarik {jumlah_ditarik} ulasan dari {rs['nama']}.")
driver.quit()

# Simpan dalam format CSV
if len(semua_ulasan) > 0:
    df = pd.DataFrame(semua_ulasan)
    df['Rating']=df['Rating'].str.extract(r'(\d+)').astype(float)

    file_name = "data_processing/Data_Review_5_RS_Tangerang.csv"
    df.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f"\n=== SUKSES! Total {len(df)} data berhasil disimpan dalam {file_name} ===")
else:
    print("\nGAGAL: Tidak ada data ulasan yang berhasil ditarik. Struktur HTML mungkin berubah")