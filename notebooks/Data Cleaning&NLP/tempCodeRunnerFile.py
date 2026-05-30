import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download kamus kata hubung (stopwords) bahasa indonesia
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

# Tambahkan beberapa kata hubung tambahan yang sering muncul di ulasan RS
kata_tambahan = ['yg', 'dan', 'di', 'ke', 'dari', 'ini', 'itu', 'nya', 'untuk', 'dengan', 
                 'saya', 'rs', 'rumah', 'sakit', 'karena', 'sudah', 'ada', 'tidak', 'ga']
stop_words.update(kata_tambahan)

# Load data CSV
print("Membaca data CSV...")
df = pd.read_csv('Data_Review_5_RS_Tangerang.csv')

# Text Cleansing
def bersihkan_teks(teks):
    teks = str(teks).lower()
    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE) #hapus Link
    teks = re.sub(r'[^\w\s]', '', teks) #hapus tanda baca & emoji
    teks = re.sub(r'\d+', '', teks) #hapus angka

    # Hapus stopwords(kata hubung)
    kata_kunci = [word for word in teks.split() if word not in stop_words]
    return ' '.join(kata_kunci)

print("Membersihkan teks ulasan dan menghapus emoji/tanda baca...")
df['Ulasan_Bersih'] = df['Ulasan'].apply(bersihkan_teks)

# Sentiment labeling (Aturan Bintang)
def tentukan_sentimen(rating):
    if rating >= 4.0:
        return "Positif"
    elif rating == 3.0:
        return "Netral"
    else:
        return "Negatif"

df['Sentimen'] = df['Rating'].apply(tentukan_sentimen)

# Simpan data yang sudah bersih dan telabel
df.to_csv('Data_Revies_Clean_Sentiment.csv', index=False)
print("Data bersih berhasil disimpan ke 'Data_Review_Clean_Sentiment.csv'")

# Membuat WordCloud (Awan kata) untuk ulasan negatif
print("Membuat visualisasi wordcloud untuk keluhan (Sentimen Negatif)...")
ulasan_negatif = df[df['Sentimen'] == 'Negatif']['Ulasan_Bersih']
teks_negatif_gabungan = " ".join(ulasan_negatif)

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Reds', max_words=50).generate(teks_negatif_gabungan)

# Tampilkan Gambarnya
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Kata Paling Sering Muncul di Ulasan Negatif', fontsize=16)
plt.tight_layout()
plt.show()