# Import Libraries
import streamlit as st
import pandas as pd
import requests
import zipfile
import io
import os
from io import BytesIO

st.set_page_config(
    page_title="Atlas Iklim Digital",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

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

st.title("Atlas Suhu Udara")
st.divider()

# === Sidebar Menu ===
with st.sidebar:
    submenu = st.selectbox("Parameter Suhu Udara", (
        "Suhu Udara Rata-Rata Bulanan",
        "Suhu Udara Rata-Rata Tahunan",
        "Suhu Udara Maksimum Bulanan",
        "Suhu Udara Maksimum Tahunan",
        "Suhu Udara Minimum Bulanan",
        "Suhu Udara Minimum Tahunan",
        "Laju Perubahan Suhu Udara Rata-Rata Tahunan",
        "Laju Perubahan Suhu Udara Maksimum Tahunan",
        "Laju Perubahan Suhu Udara Minimum Tahunan",
        "Suhu Maksimum Absolut Harian",
        "Suhu Minimum Absolut Harian",
        "Selisih Suhu Maksimum dengan Suhu Minimum",
        "Jumlah Hari Suhu Udara Maksimum >35°C",
        "Jumlah Hari Suhu Udara Minimum <15°C"
    ))

# Fungsi Menampilkan Peta Bulanan
def tampilkan_peta(prefix_file, judul_keterangan):
    bulan_dict = {
        "Januari": "Jan", "Februari": "Feb", "Maret": "Mar", "April": "Apr",
        "Mei": "May", "Juni": "Jun", "Juli": "Jul", "Agustus": "Aug",
        "September": "Sep", "Oktober": "Oct", "November": "Nov", "Desember": "Dec"
    }

    opsi = st.selectbox("Pilih Bulan", list(bulan_dict.keys()))
    kode_bulan = bulan_dict[opsi]
    file_path = os.path.join(folder_path, f"{prefix_file}_bln_{kode_bulan}.png")

    if os.path.exists(file_path):
        st.image(file_path, caption=f"Peta {judul_keterangan} Bulan {opsi} Periode 1991-2020", use_container_width=True)
    else:
        st.warning("Gambar tidak ditemukan.")
        st.write(f"Path dicari: {file_path}")
        st.write("Daftar file di folder:", os.listdir(folder_path))
        # Tambahkan setelah os.listdir(output_folder)
        files = os.listdir(folder_path)
        st.write("Contoh isi folder peta:")
        st.write(files[:5])  # tampilkan 10 file pertama

# === Routing Menu berdasarkan submenu ===
if submenu == "Suhu Udara Rata-Rata Bulanan":
    tampilkan_peta("Trata", "Suhu Udara Rata-Rata")

elif submenu == "Suhu Udara Rata-Rata Tahunan":
    file_path = os.path.join(folder_path, "Trata_tahun.png")
    caption = "Peta Suhu Udara Rata-Rata Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Suhu Udara Maksimum Bulanan":
    tampilkan_peta("Tmax", "Suhu Udara Maksimum")

elif submenu == "Suhu Udara Maksimum Tahunan":
    file_path = os.path.join(folder_path, "Tmax_tahun.png")
    caption = "Peta Suhu Udara Maksimum Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Suhu Udara Minimum Bulanan":
    tampilkan_peta("Tmin", "Suhu Udara Minimum")

elif submenu == "Suhu Udara Minimum Tahunan":
    file_path = os.path.join(folder_path, "Tmin_tahun.png")
    caption = "Peta Suhu Udara Minimum Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Laju Perubahan Suhu Udara Rata-Rata Tahunan":
    file_path = os.path.join(folder_path, "Trend_trata.png")
    caption = "Peta Laju Perubahan Suhu Udara Rata-Rata Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Laju Perubahan Suhu Udara Maksimum Tahunan":
    file_path = os.path.join(folder_path, "Trend_tmax.png")
    caption = "Peta Laju Perubahan Suhu Udara Maksimum Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Laju Perubahan Suhu Udara Minimum Tahunan":
    file_path = os.path.join(folder_path, "Trend_tmin.png")
    caption = "Peta Laju Perubahan Suhu Udara Minimum Tahunan Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Suhu Maksimum Absolut Harian":
    file_path = os.path.join(folder_path, "Tmax_abs.png")
    caption = "Peta Suhu Maksimum Absolut Harian Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Suhu Minimum Absolut Harian":
    file_path = os.path.join(folder_path, "Tmin_abs.png")
    caption = "Peta Suhu Minimum Absolut Harian Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Selisih Suhu Maksimum dengan Suhu Minimum":
    file_path = os.path.join(folder_path, "DTR.png")
    caption = "Peta Selisih Suhu Maksimum dengan Suhu Minimum Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Jumlah Hari Suhu Udara Maksimum >35°C":
    file_path = os.path.join(folder_path, "Hari_Tmax_35.png")
    caption = "Peta Jumlah Hari Suhu Udara Maksimum >35°C Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)

elif submenu == "Jumlah Hari Suhu Udara Minimum <15°C":
    file_path = os.path.join(folder_path, "Hari_Tmin_15.png")
    caption = "Peta Jumlah Hari Suhu Udara Minimum <15°C Periode 1991-2020"
    st.image(file_path, caption, use_container_width=True)
else:
    st.info("Peta untuk kategori ini belum tersedia di versi ini.")

# membuat narasi dalam keterangan
with st.expander(":blue-background[Keterangan Gambar :]"):
    st.caption("**Penjelasan/Definisi**")
    st.caption(('''**Suhu udara rata-rata Tahunan (1991-2020) :**
                Suhu udara rata-rata tahunan adalah rata-rata dari suhu udara  rata-rata harian selama satu tahun dari tahun 1991 hingga 2020.
                '''))
    st.caption(('''**Suhu udara rata-rata Bulanan (1991-2020) :**
                Suhu udara rata-rata bulanan adalah rata-rata dari suhu rata-rata harian selama satu bulan dari tahun 1991 hingga 2020. Data suhu rata-rata harian diperoleh rumus sebagai berikut :
                '''))
    st.caption(('''*Suhu rata-rata harian = [(2 x T07)+T13+T18]/4*'''))
    st.caption(('''*T07 : data pengamatan suhu udara yang diamati pada jam 07 waktu setempat*'''))
    st.caption(('''*T13 : data pengamatan suhu udara yang diamati pada jam 13 waktu setempat*'''))
    st.caption(('''*T18 : data pengamatan suhu udara yang diamati pada jam 18 waktu setempat*'''))
    st.caption(('''**Suhu udara maksimum tahunan (1991-2020) :**
                Suhu udara maksimum rata-rata tahunan adalah rata-rata suhu udara maksimum harian selama satu tahun dari tahun 1991 hingga 2020.
                Pengukuran suhu udara maksimum harian dilakukan menggunakan termometer suhu udara maksimum pengamatan jam 18 waktu setempat.
                '''))
    st.caption(('''**Suhu udara maksimum bulanan (1991-2020) :**
                Suhu udara maksimum rata-rata bulanan adalah rata-rata suhu udara maksimum harian selama satu bulan dari tahun 1991 hingga 2020.'''))
    st.caption(('''**Suhu udara minimum tahunan (1991-2020) :**
                Suhu udara minimum rata-rata tahunan adalah rata-rata  suhu udara minimum harian selama satu tahun dari tahun 1991 hingga 2020.
                Pengukuran suhu udara minimum harian dilakukan menggunakan termometer suhu udara minimum pengamatan jam 13 waktu setempat.
                '''))
    st.caption(('''**Suhu udara minimum bulanan (1991-2020) :**
                Suhu udara minimum rata-rata bulanan adalah rata-rata suhu udara minimum harian selama satu bulan dari tahun 1991 hingga 2020.'''))
    st.caption(('''**Laju perubahan suhu udara rata-rata (°C/10 tahun) tahunan (1991-2020) :**
                Laju perubahan suhu udara rata-rata tahunan adalah kecenderungan atau tren perubahan suhu rata-rata tahunan dari tahun 1991 hingga 2020.
                Contoh : 0.5°C/10 tahun artinya dalam kurun waktu 30 tahun dari tahun 1991 sampai 2020 terjadi perubahan suhu rata-rata sebesar 0.5°C selama 10 tahun.'''))
    st.caption(('''**Laju perubahan suhu udara maksimum (°C/10 tahun) tahunan (1991-2020) :**
                Laju perubahan suhu udara  maksimum tahunan adalah kecenderungan atau tren perubahan suhu udara maksimum tahunan dari tahun 1991 hingga 2020.
                Contoh : 0.5°C/10 tahun artinya dalam kurun waktu 30 tahun dari tahun 1991 sampai 2020 terjadi perubahan suhu maksimum sebesar 0.5°C selama 10 tahun.'''))
    st.caption(('''**Laju perubahan suhu udara minimum (°C/10 tahun) tahunan (1991-2020) :**
                Laju perubahan suhu udara minimum  tahunan adalah kecenderungan atau tren perubahan suhu udara  minimum  tahunan dari tahun 1991 hingga 2020.
                Contoh : 0.5°C/10 tahun artinya dalam kurun waktu 30 tahun dari tahun 1991 sampai 2020 terjadi perubahan suhu minimum sebesar 0.5°C selama 10 tahun.'''))
    st.caption(('''**Suhu Udara Maksimum Absolut Harian (1991-2020) :**
                Suhu udara maksimum absolut harian adalah suhu udara maksimum harian tertinggi selama periode tahun 1991 hingga 2020.'''))
    st.caption(('''**Suhu Udara Minimum Absolut Harian (1991-2020) :**
                Suhu udara minimum absolut harian adalah suhu udara minimum harian tertinggi selama periode tahun 1991 hingga 2020.'''))
    st.caption(('''**Selisih Suhu Udara maksimum dengan Suhu Udara Minimum (DTR) (1991-2020) :**
                Selisih suhu udara maksimum dengan suhu udara minimum adalah rata-rata suhu udara maksimum dikurangi suhu udara minimum dari tahun 1991 hingga 2020.'''))
    st.caption(('''**Rata-rata Jumlah Hari dengan Suhu Udara Maksimum > 35°C :**
                Rata-rata jumlah Hari dengan Suhu Udara Maksimum > 35°C adalah Jumlah hari kejadian suhu udara maksimum  > 35°C dalam setahun yang dirata-ratakan selama tahun 1991 hingga 2020.'''))
    st.caption(('''**Rata-rata Jumlah Hari Suhu Udara Minimum < 15°C :**
                Rata-rata jumlah Hari Suhu Udara Minimum < 15°C adalah Jumlah hari kejadian suhu udara Minimum < 15°C dalam setahun yang dirata-ratakan selama tahun 1991 hingga 2020.'''))
    
# membuat tabel
st.subheader("📊 Statistik Klimatologi")

# Link ke file Excel dari repo kamu
url = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Data_ready.xlsx"

# Download file dan load ke pandas
response = requests.get(url)
xls = pd.ExcelFile(BytesIO(response.content))

# Load semua sheet ke dalam dictionary
sheets = {
    "Suhu Udara Rata-Rata Bulanan": xls.parse('Trata_bln'),
    "Suhu Udara Minimun Bulanan": xls.parse('Tmin_bln'),
    "Suhu Udara Maksimum Bulanan": xls.parse('Tmax_bln'),
    "Suhu Udara Tahunan": xls.parse('Suhu_thn'),
    "Suhu Udara Maksimum Absolut Tahunan": xls.parse('Tmax_abs_thn'),
    "Suhu Udara Minimum Absolut Tahunan": xls.parse('Tmin_abs_thn'),
    "Trend Suhu Udara Maksimum Tahunan": xls.parse('trend_tmax_thn'),
    "Trend Suhu Udara Minimum Tahunan": xls.parse('trend_tmin_thn'),
    "Trend Suhu Udara Rata-Rata Tahunan": xls.parse('trend_trata_thn'),
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
