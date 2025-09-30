# Import Libraries
import streamlit as st
import pandas as pd
import os
import requests
import zipfile
import io
from io import BytesIO

# === Setup Halaman ===
st.set_page_config(
    page_title="Atlas Iklim Digital",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# === Fungsi Download dan Ekstrak Peta ===
@st.cache_resource
def download_and_extract_zip():
    url = "https://github.com/adityoAJA/Atlas/releases/download/v1.0.0/peta.zip"
    output_folder = "data/peta"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)
        response = requests.get(url)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(output_folder)

    return output_folder

# === Load Folder Peta ===
with st.spinner("Sedang mengunduh dan mengekstrak data peta..."):
    folder_path = download_and_extract_zip()

# === Judul Halaman ===
st.title('Atlas Curah Hujan')
st.divider()

# === Sidebar Menu ===
# with st.sidebar:
submenu = st.selectbox("🌏 Pilih Gambar:", (
        "Curah Hujan Tahunan",
        "Curah Hujan Bulanan",
        "Curah Hujan Tahunan Tertinggi",
        "Curah Hujan Harian Maksimum Tahunan",
        "Curah Hujan Harian Maksimum Absolut",
        "Curah Hujan Harian Maksimum Absolut Bulanan",
        "Jumlah Hari Hujan Tahunan",
        "Jumlah Hari Hujan Bulanan",
        "Jumlah Hari Hujan dengan Curah Hujan >50 mm/hari Tahunan",
        "Jumlah Hari Hujan dengan Curah Hujan >100 mm/hari",
        "Jumlah Hari Tanpa Hujan Berurutan Terpanjang",
        "Jumlah Hari Hujan Berurutan Terpanjang"
    ))

# Fungsi menampilkan gambar
def tampilkan_gambar(full_path, caption):
    st.image(full_path, caption=caption, use_container_width=True)

if submenu == "Curah Hujan Tahunan":
    file_path = os.path.join(folder_path, "RTOT.png")
    caption = "Peta Rata-Rata Total Curah Hujan Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Curah Hujan Bulanan":
    # Dictionary bulan dan path peta
    ch_dict = {
        "Januari": "CH_bln_Jan.png",
        "Februari": "CH_bln_Feb.png",
        "Maret": "CH_bln_Mar.png",
        "April": "CH_bln_Apr.png",
        "Mei": "CH_bln_May.png",
        "Juni": "CH_bln_Jun.png",
        "Juli": "CH_bln_Jul.png",
        "Agustus": "CH_bln_Aug.png",
        "September": "CH_bln_Sep.png",
        "Oktober": "CH_bln_Oct.png",
        "November": "CH_bln_Nov.png",
        "Desember": "CH_bln_Dec.png"
    }
    bulan_ch = st.selectbox("Pilih Bulan", list(ch_dict.keys()))
    file_path = os.path.join(folder_path, ch_dict[bulan_ch])
    caption = f"Peta Rata-Rata Curah Hujan Bulan {bulan_ch} Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Curah Hujan Tahunan Tertinggi":
    file_path = os.path.join(folder_path, "RTOTMAX.png")
    caption = "Peta Total Curah Hujan Tertinggi Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Curah Hujan Harian Maksimum Tahunan":
    file_path = os.path.join(folder_path, "RX1d.png")
    caption = "Peta Rata-Rata Curah Hujan Harian Maksimum Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Curah Hujan Harian Maksimum Absolut":
    file_path = os.path.join(folder_path, "RX1dmax.png")
    caption = "Peta Rata-Rata Curah Hujan Harian Maksimum Absolut Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Curah Hujan Harian Maksimum Absolut Bulanan":
    # Dictionary bulan dan path peta
    abs_dict = {
        "Januari": "RX1day_bln_Jan.png",
        "Februari": "RX1day_bln_Feb.png",
        "Maret": "RX1day_bln_Mar.png",
        "April": "RX1day_bln_Apr.png",
        "Mei": "RX1day_bln_May.png",
        "Juni": "RX1day_bln_Jun.png",
        "Juli": "RX1day_bln_Jul.png",
        "Agustus": "RX1day_bln_Aug.png",
        "September": "RX1day_bln_Sep.png",
        "Oktober": "RX1day_bln_Oct.png",
        "November": "RX1day_bln_Nov.png",
        "Desember": "RX1day_bln_Dec.png"
    }
    bulan_abs = st.selectbox("Pilih Bulan", list(abs_dict.keys()))
    file_path = os.path.join(folder_path, abs_dict[bulan_abs])
    caption = f"Peta Rata-Rata Curah Hujan Harian Maksimum Absolut Bulan {bulan_abs} Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Hujan Tahunan":
    file_path = os.path.join(folder_path, "RWD.png")
    caption = "Peta Rata-Rata Jumlah Hari Hujan Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Hujan Bulanan":
    # Dictionary bulan dan path peta
    hh_dict = {
        "Januari": "HH_bln_Jan.png",
        "Februari": "HH_bln_Feb.png",
        "Maret": "HH_bln_Mar.png",
        "April": "HH_bln_Apr.png",
        "Mei": "HH_bln_May.png",
        "Juni": "HH_bln_Jun.png",
        "Juli": "HH_bln_Jul.png",
        "Agustus": "HH_bln_Aug.png",
        "September": "HH_bln_Sep.png",
        "Oktober": "HH_bln_Oct.png",
        "November": "HH_bln_Nov.png",
        "Desember": "HH_bln_Dec.png"
    }
    bulan_hh = st.selectbox("Pilih Bulan", list(hh_dict.keys()))
    file_path = os.path.join(folder_path, hh_dict[bulan_hh])
    caption = f"Peta Rata-Rata Jumlah Hari Hujan Bulan {bulan_hh} Periode 1991–2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Hujan dengan Curah Hujan >50 mm/hari Tahunan":
    file_path = os.path.join(folder_path, "R50.png")
    caption = "Peta Rata-Rata Jumlah Hari Hujan >50 mm/hari Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Hujan dengan Curah Hujan >100 mm/hari":
    file_path = os.path.join(folder_path, "R100max.png")
    caption = "Peta Rata-Rata Jumlah Hari Hujan >100 mm/hari Tahunan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Tanpa Hujan Berurutan Terpanjang":
    file_path = os.path.join(folder_path, "CDDmax.png")
    caption = "Peta Rata-Rata Jumlah Hari Tanpa Hujan Berurutan Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

elif submenu == "Jumlah Hari Hujan Berurutan Terpanjang":
    file_path = os.path.join(folder_path, "CWDmax.png")
    caption = "Peta Rata-Rata Jumlah Hari Hujan Berurutan Terpanjang Periode 1991-2020"
    tampilkan_gambar(file_path, caption)

# Narasi/keterangan gambar
with st.expander(":blue-background[Keterangan Gambar :]"):
    st.caption("**Penjelasan/Definisi**")
    st.caption("**1. Rata-rata Total Curah Hujan Tahunan (1991-2020) (mm/tahun):**")
    st.caption("Rata-rata dari total curah hujan tahunan dari tahun 1991-2020. Sesuai ketentuan WMO dan BMKG, jumlah tahun yang ada (non-missing data) minimal 80% dari 30 tahun, yaitu 24 tahun")
    st.caption("**2. Rata-rata Curah Hujan Bulanan (1991-2020) (mm/bulan):**")
    st.caption("Rata-rata dari jumlah curah hujan bulanan (Januari sampai Desember) selama 30 tahun (1991-2020). Untuk setiap jumlah bulanan yang ada minimal 80% dari 30 tahun.")
    st.caption("**3. Total Curah Hujan Tahunan Tertinggi (1991-2020) (mm/tahun):**")
    st.caption("Total curah hujan tahunan tertinggi yang terjadi selama tahun 1991-2020 di setiap stasiun pengamatan.")
    st.caption("**4. Curah Hujan Harian Maksimum Absolut (Rx1day) (mm/hari):**")
    st.caption("Jumlah curah harian (24 jam) tertinggi yang terjadi di sebuah stasiun pengamatan selama tahun 1991-2020.")
    st.caption("**5. Curah hujan harian Maksimum Absolut bulanan (mm/hari):**")
    st.caption("Jumlah curah harian (24 jam) tertinggi yang terjadi di sebuah stasiun pengamatan pada masing-masing bulan selama tahun 1991-2020.")
    st.caption("**6. Rata-rata Curah Hujan Harian Maksimum Tahunan (mm/hari):**")
    st.caption("Rata-rata dari curah hujan harian (24 jam) tertinggi di sebuah stasiun pengamatan per tahun selama tahun 1991-2020.")
    st.caption("**7. Rata-rata Jumlah Hari Hujan Bulanan (1991-2020) (hari/bulan):**")
    st.caption("Rata-rata selama tahun 1991-2020 dari jumlah hari dalam sebulan di mana pada hari tersebut terjadi hujan. (kejadian hujan ditandai dengan pengukuran curah hujan minimal 1 mm).")
    st.caption("**8. Rata-rata Jumlah Hari Hujan dengan Curah Hujan > 50 mm/hari (Tahunan):**")
    st.caption("Rata-rata selama tahun 1991-2020 dari jumlah hari dalam satu tahun dimana pada hari tersebut terjadi hujan di atas 50 mm per hari.")
    st.caption("**9. Rata-rata Jumlah Hari Hujan dengan Curah Hujan > 100 mm/hari (Tahunan):**")
    st.caption("Rata-rata selama tahun 1991-2020 dari jumlah hari dalam satu tahun dimana pada hari tersebut terjadi hujan di atas 100 mm per hari.")
    st.caption("**10. Jumlah Hari Tanpa Hujan Berurutan Terpanjang (Consecutive Dry Days):**")
    st.caption("Jumlah hari terpanjang berturut-turut selama 30 tahun, dimana pada hari tersebut di stasiun pengamatan tidak terjadi hujan (hujan kurang dari 1 mm).")
    st.caption("**11. Peta Jumlah Hari Hujan Berurutan Terpanjang (Consecutive Wet Days):**")
    st.caption("Jumlah hari terpanjang berturut-turut selama 30 tahun, dimana pada hari tersebut di stasiun pengamatan terjadi hujan (hujan lebih besar sama dengan 1 mm).")
    
# membuat tabel
st.subheader("📊 Statistik Klimatologi")

# Link ke file Excel dari repo kamu
url = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Data_ready_new.xlsx"

# Download file dan load ke pandas
response = requests.get(url)
xls = pd.ExcelFile(BytesIO(response.content))

# Load semua sheet ke dalam dictionary
sheets = {
    "Curah Hujan Bulanan": xls.parse('CH_bln'),
    "Curah Hujan Harian Maksimum Bulanan": xls.parse('RX1day_bln'),
    "Hari Hujan Bulanan": xls.parse('HH_bln'),
    "Curah Hujan Tahunan": xls.parse('CH_thn'),
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
