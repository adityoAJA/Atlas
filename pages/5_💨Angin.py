# import libraries
import streamlit as st
import pandas as pd
import requests
import zipfile
import io
import os
from io import BytesIO

# Setting halaman
st.set_page_config(
    page_title="Atlas Iklim Digital",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Judul utama
st.title("Atlas Angin")
st.divider()

@st.cache_resource
def download_and_extract_zip():
    url = "https://github.com/adityoAJA/Atlas/releases/download/v1.0.0/peta.zip"
    output_folder = "data/peta"  # Folder target

    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)
        response = requests.get(url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(output_folder)

    return output_folder

# jalankan fungsi
with st.spinner("Sedang mengunduh dan mengekstrak data peta..."):
    folder_path = download_and_extract_zip()

# Sidebar submenu
# with st.sidebar:
    submenu = st.selectbox("🌏 Pilih Gambar:", (
        "Kecepatan Angin Tertinggi",
        "Hari dengan Kecepataan Angin >25 Knots Tahunan",
        "Hari dengan Kecepataan Angin >25 Knots Bulanan"
    ))

# Fungsi tampilkan gambar
def tampilkan_gambar(full_path, caption):
    st.image(full_path, caption=caption, use_container_width=True)

# Dictionary bulan dan path peta angin >25 knots bulanan
angin_dict = {
    "Januari": "Wind_25_bln_Jan.png",
    "Februari": "Wind_25_bln_Feb.png",
    "Maret": "Wind_25_bln_Mar.png",
    "April": "Wind_25_bln_Apr.png",
    "Mei": "Wind_25_bln_May.png",
    "Juni": "Wind_25_bln_Jun.png",
    "Juli": "Wind_25_bln_Jul.png",
    "Agustus": "Wind_25_bln_Aug.png",
    "September": "Wind_25_bln_Sep.png",
    "Oktober": "Wind_25_bln_Oct.png",
    "November": "Wind_25_bln_Nov.png",
    "Desember": "Wind_25_bln_Dec.png"
}

# Konten berdasarkan submenu
if submenu == "Kecepatan Angin Tertinggi":
    file_path = os.path.join(folder_path, "Wind_max.png")
    caption = "Peta Kecepatan Angin Tertinggi (Knots) Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Hari dengan Kecepataan Angin >25 Knots Tahunan":
    file_path = os.path.join(folder_path, "Wind_25.png")
    caption = "Peta Rata-Rata Jumlah Hari dengan Kecepataan Angin >25 Knots Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Hari dengan Kecepataan Angin >25 Knots Bulanan":
    bulan_angin = st.selectbox("Pilih Bulan", list(angin_dict.keys()))
    file_path = os.path.join(folder_path, angin_dict[bulan_angin])
    caption = f"Peta Jumlah Hari dengan Kecepatan Angin >25 Knots Bulan {bulan_angin} Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

# Narasi/keterangan gambar
with st.expander(":blue-background[Keterangan Gambar :]"):
    st.caption("**Penjelasan/Definisi**")
    st.caption("**1. Kecepatan Angin Tertinggi (Knots):**")
    st.caption("Kecepatan angin  tertinggi sepanjang tahun 1999 - 2020 (dalam knots).")
    st.caption("**2. Rata-rata Jumlah hari dengan Kecepatan Angin > 25 Knots Tahunan:**")
    st.caption("Rata-rata jumlah hari dengan kecepatan angin lebih besar dari 25 Knots pertahun sepanjang tahun 1999 - 2020. Sesuai dengan peraturan BMKG No. 9 tahun 2022 tentang Penyediaan dan Penyebarluasan Peringatan Dini Cuaca Ekstrem untuk variabel angin dikategorikan angin kencang saat kecepatan diatas 25 knot atau 45 km/jam.")
    st.caption("**3. Jumlah Hari Terbanyak Dengan Kecepatan Angin >  25 Knots Bulanan:**")
    st.caption("Jumlah hari terbanyak dengan kecepatan angin > 25 Knots dalam setiap bulan sepanjang tahun 1999 - 2020.")

# membuat tabel
st.subheader("📊 Statistik Klimatologi")

# Link ke file Excel dari repo kamu
url = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Data_ready_new.xlsx"

# Download file dan load ke pandas
response = requests.get(url)
xls = pd.ExcelFile(BytesIO(response.content))

# Load semua sheet ke dalam dictionary
sheets = {
    "Rata-Rata Jumlah Hari dengan Kecepatan Angin >25 Knot Bulanan": xls.parse('Wind_25_bln'),
    "Rata-Rata Jumlah Hari dengan Kecepatan Angin >25 Knot Tahunan": xls.parse('Wind_25_thn'),
}

# Dropdown untuk pilih data
selected_name = st.selectbox("📂 Pilih Parameter:", list(sheets.keys()))
df = sheets[selected_name]

# Bersihkan nilai koma jadi titik, dan konversi ke float
df.replace(",", ".", regex=True, inplace=True)

# Coba pastikan hanya kolom numerik bulan yang dikonversi
try:
    month_cols = df.columns[3:]  # Asumsi kolom ke-4 dst adalah bulanan
    df[month_cols] = df[month_cols].astype(float)

    # Hitung statistik per bulan
    stats_df = pd.DataFrame({
        'Mean': df[month_cols].mean(),
        'Median': df[month_cols].median(),
        'Minimum': df[month_cols].min(),
        'Maximum': df[month_cols].max(),
        'Std_Dev': df[month_cols].std(),
        'Range': df[month_cols].max() - df[month_cols].min(),
        'Count': df[month_cols].count(),
        'Percentile_5': df[month_cols].quantile(0.05),
        'Percentile_95': df[month_cols].quantile(0.95),
        'Coef_Var(%)': (df[month_cols].std() / df[month_cols].mean()) * 100
    })
    # Ambil jumlah stasiun dari kolom 'Count', diasumsikan semua bulan punya count sama
    jumlah_stasiun = int(stats_df.loc[:, 'Count'].mean())

    # Hapus kolom 'Count' dari dataframe untuk ditampilkan dan digrafikkan
    stats_df_display = stats_df.drop(columns=['Count'])
    st.dataframe(stats_df_display.style.format("{:.2f}"))
    # st.dataframe(stats_df.style.format("{:.2f}"))

except Exception as e:
    st.warning(f"Tidak bisa menghitung statistik: {e}")

# membuat narasi tabel dalam keterangan
with st.expander(":blue-background[Keterangan Tabel :]"):
    st.caption("**Penjelasan/Definisi**")
    st.caption(('''**Mean         :** **Rata-rata** dari nilai suhu per bulan di seluruh stasiun. Ini adalah pusat kecenderungan data.'''))
    st.caption(('''**Median       :** Nilai **tengah** dari data yang telah diurutkan per bulan. Lebih tahan terhadap pencilan (outlier).'''))
    st.caption(('''**Minimum      :** Nilai **terendah** yang tercatat pada bulan tersebut.'''))
    st.caption(('''**Maximum      :** Nilai **tertinggi** yang tercatat pada bulan tersebut.'''))
    st.caption(('''**Std_Dev      :** **Standar deviasi**, Mengukur seberapa menyebar data dari rata-rata (variabilitas data).'''))
    st.caption(('''**Range        :** Selisih antara nilai maksimum dan minimum **Max - Min**. Menunjukkan sebaran nilai ekstrem.'''))
    st.caption(('''**Count        :** Jumlah nilai **valid** (tidak NaN) yang dihitung per bulan. Biasanya setara dengan jumlah stasiun.'''))
    st.caption(('''**Percentile_5 :** **Persentil ke-5** Nilai di bawahnya terdapat 5% data. Menunjukkan suhu yang lebih ekstrem rendah.'''))
    st.caption(('''**Percentile_95:** **Persentil ke-95** Nilai di atasnya hanya terdapat 5% data. Menunjukkan suhu yang ekstrem tinggi.'''))
    st.caption(('''**Coef_Var(%)  :** **Koefisien variasi dalam persen**, Menunjukkan keragaman relatif dibanding rata-rata. Nilai tinggi = fluktuasi besar.'''))

# Plot menggunakan Plotly
import plotly.express as px

try:
    # Cek apakah ini data bulanan (berdasarkan nama sheet yang mengandung 'Bulanan')
    if "Bulanan" in selected_name:
        # Pilihan statistik untuk divisualisasikan
        stat_options = stats_df_display.columns.tolist()
        selected_stat = st.selectbox("📈 Pilih Nilai Statistik:", stat_options)
        # Grafik
        fig = px.line(
        x=stats_df.index, 
        y=stats_df[selected_stat], 
        labels={'x': 'Bulan', 'y': selected_stat},
        title=f"Nilai {selected_stat} untuk parameter {selected_name} dari {jumlah_stasiun} Stasiun BMKG",
        markers=True  # Ini menambahkan titik di tiap bulan
        )
        # Pastikan garis tidak smooth (default-nya sudah lurus, tapi ini bisa diatur juga lewat mode)
        fig.update_traces(mode='lines+markers')

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Tidak bisa menampilkan grafik selain parameter Bulanan")
        
except Exception as e:
    st.warning(f"Gagal membuat grafik: {e}")

