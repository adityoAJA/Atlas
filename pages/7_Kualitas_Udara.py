# Import Libraries
import streamlit as st
import pandas as pd
import requests
import zipfile
import io
import os
from io import BytesIO

# Konfigurasi halaman
st.set_page_config(
    page_title="Atlas Iklim Digital",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Judul halaman
st.title('Atlas Kualitas Udara')
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

# Sidebar
with st.sidebar:
    submenu = st.selectbox(
        "Parameter Kualitas Udara",
        (
            "pH Air Hujan Tahunan",
            "pH Air Hujan Bulanan",
            "Rata-Rata SPM",
            "SPM Maksimum",
            "SPM Minimum"
        )
    )

# Dictionary bulan dan path peta
ph_dict = {
    "Januari": "ph_bln_Jan.png",
    "Februari": "ph_bln_Feb.png",
    "Maret": "ph_bln_Mar.png",
    "April": "ph_bln_Apr.png",
    "Mei": "ph_bln_May.png",
    "Juni": "ph_bln_Jun.png",
    "Juli": "ph_bln_Jul.png",
    "Agustus": "ph_bln_Aug.png",
    "September": "ph_bln_Sep.png",
    "Oktober": "ph_bln_Oct.png",
    "November": "ph_bln_Nov.png",
    "Desember": "ph_bln_Dec.png"
}

# Fungsi tampilkan gambar
def tampilkan_gambar(full_path, caption):
    st.image(full_path, caption=caption, use_container_width=True)

# Konten berdasarkan submenu
if submenu == "pH Air Hujan Tahunan":
    file_path = os.path.join(folder_path, "PH.png")
    caption = "Peta Rata-Rata PH Air Hujan Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "pH Air Hujan Bulanan":
    bulan_ph = st.selectbox("Pilih Bulan", list(ph_dict.keys()))
    file_path = os.path.join(folder_path, ph_dict[bulan_ph])
    caption = f"Peta Rata-Rata PH Air Hujan Bulan {bulan_ph} Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Rata-Rata SPM":
    file_path = os.path.join(folder_path, "SPM_ave.png")
    caption = "Peta Rata-Rata Suspended Particulate Matters (SPM) Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "SPM Maksimum":
    file_path = os.path.join(folder_path, "SPM_max.png")
    caption = "Peta Suspended Particulate Matters (SPM) Maksimum Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "SPM Minimum":
    file_path = os.path.join(folder_path, "SPM_min.png")
    caption = "Peta Suspended Particulate Matters (SPM) Minimum Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

# membuat tabel
st.subheader("📊 Statistik Klimatologi")

# Link ke file Excel dari repo kamu
url = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Data_ready.xlsx"

# Download file dan load ke pandas
response = requests.get(url)
xls = pd.ExcelFile(BytesIO(response.content))

# Load semua sheet ke dalam dictionary
sheets = {
    "PH Air Hujan Bulanan": xls.parse('ph_bln'),
    "PH Air Hujan Tahunan": xls.parse('ph_thn'),
    "Suspended Particulate Matters (SPM) Tahunan": xls.parse('SPM_thn'),
}

# Dropdown untuk pilih data
selected_name = st.selectbox("📂 Pilih Dataset:", list(sheets.keys()))
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
        'Min': df[month_cols].min(),
        'Max': df[month_cols].max(),
        'Std_Dev': df[month_cols].std(),
        'Range': df[month_cols].max() - df[month_cols].min(),
        'Count': df[month_cols].count(),
        'Percentile5': df[month_cols].quantile(0.05),
        'Percentile95': df[month_cols].quantile(0.95),
        'Coef_Var(%)': (df[month_cols].std() / df[month_cols].mean()) * 100
    })

    st.dataframe(stats_df.style.format("{:.2f}"))

except Exception as e:
    st.warning(f"Tidak bisa menghitung statistik: {e}")

# membuat narasi tabel dalam keterangan
with st.expander(":blue-background[Keterangan Tabel :]"):
    st.caption("**Penjelasan/Definisi**")
    st.caption(('''**Mean        :** **Rata-rata** dari nilai suhu per bulan di seluruh stasiun. Ini adalah pusat kecenderungan data.'''))
    st.caption(('''**Median      :** Nilai **tengah** dari data yang telah diurutkan per bulan. Lebih tahan terhadap pencilan (outlier).'''))
    st.caption(('''**Min         :** Nilai **terendah** yang tercatat pada bulan tersebut.'''))
    st.caption(('''**Max         :** Nilai **tertinggi** yang tercatat pada bulan tersebut.'''))
    st.caption(('''**Std_Dev     :** **Standar deviasi**, Mengukur seberapa menyebar data dari rata-rata (variabilitas data).'''))
    st.caption(('''**Range       :** Selisih antara nilai maksimum dan minimum **Max - Min**. Menunjukkan sebaran nilai ekstrem.'''))
    st.caption(('''**Count       :** Jumlah nilai **valid** (tidak NaN) yang dihitung per bulan. Biasanya setara dengan jumlah stasiun.'''))
    st.caption(('''**Percentile5 :** **Persentil ke-5** Nilai di bawahnya terdapat 5% data. Menunjukkan suhu yang lebih ekstrem rendah.'''))
    st.caption(('''**Percentile95:** **Persentil ke-95** Nilai di atasnya hanya terdapat 5% data. Menunjukkan suhu yang ekstrem tinggi.'''))
    st.caption(('''**Coef_Var(%) :** **Koefisien variasi dalam persen**, Menunjukkan keragaman relatif dibanding rata-rata. Nilai tinggi = fluktuasi besar.'''))