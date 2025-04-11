# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
import requests
import io
from io import BytesIO

# Setting layout halaman
# st.logo('Logo_BMKG_(2010).png') # logo pada sidebar
st.set_page_config(
        page_title="Atlas Iklim Digital",
        page_icon="🏠",
        layout="centered",
        initial_sidebar_state="expanded"
    )

# Load custom CSS file
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Link ke file Excel dari repo kamu
url = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Sebaran.xlsx"

# Download file dan load ke pandas
response = requests.get(url)
xls = pd.ExcelFile(BytesIO(response.content))

# Pastikan file Excel Anda memiliki kolom seperti di atas
sheets = {
    "Sebaran Pengamatan Iklim": xls.parse('WMOID')}

# Load data
@st.cache_data
def load_data(df):
    df = sheets["Sebaran Pengamatan Iklim"]
    # Konversi kolom Lat dan Lon menjadi string terlebih dahulu
    df['Lat'] = df['Lat'].astype(str).str.replace(',', '.')
    df['Lon'] = df['Lon'].astype(str).str.replace(',', '.')
    # Lalu ubah menjadi numerik
    df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
    df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
    return df

df = load_data("Sebaran Pengamatan Iklim")

# Plot dengan scatter_mapbox
fig = px.scatter_mapbox(
    df,
    lat="Lat",
    lon="Lon",
    hover_name="Sta_Name",
    hover_data={"WMO_Id": True, "Kab/Kota": True, "Lat": False, "Lon": False},
    size_max=15,  # Ukuran maksimal titik
    size=[10] * len(df),  # Perbesar ukuran semua titik
    zoom=0.5,  # Zoom level
    height=500,  # Tinggi peta
    width=2000  # Lebar peta
)

# Tambahkan customdata untuk menyertakan kolom Sta_Name bersama Kab/Kota dan WMO_Id
fig.update_traces(
    customdata=df[["Sta_Name", "Kab/Kota", "WMO_Id"]],  # Kolom yang dibutuhkan
    hovertemplate=(
        "<b>Nama Stasiun:</b> %{customdata[0]}<br>"
        "<b>Kab/Kota:</b> %{customdata[1]}<br>"
        "<b>WMO ID:</b> %{customdata[2]}<extra></extra>"
    ),  # Template tooltip
    marker=dict(size=15)  # Atur ukuran marker
)

# Set layout untuk Mapbox
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=3.3,
    # mapbox_center={"lat": df["Lat"].mean(), "lon": df["Lon"].mean()},
    mapbox_center={"lat": -2, "lon": 118},
    # Title
    title={
        'text': "Peta Sebaran Stasiun UPT BMKG",
        'x': 0.5,  # Center title
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=16, color='black', family='Arial')},
    # Margin (in pixels)
    margin=dict(l=0, r=0, t=50, b=20),
)

# Link ke file Excel dari repo kamu
url1 = "https://raw.githubusercontent.com/adityoAJA/Atlas/main/Data_ready.xlsx"

# Download file dan load ke pandas
response1 = requests.get(url1)
xls1 = pd.ExcelFile(BytesIO(response1.content))

# sheet
sheets = {
    "Curah Hujan Bulanan": xls1.parse('CH_bln'),
    'Curah Hujan Harian Maksimum Bulanan': xls1.parse('RX1day_bln'),
    'Hari Hujan Bulanan': xls1.parse('HH_bln'),
    'Suhu Udara Rata-Rata Bulanan': xls1.parse('Trata_bln'),
    'Suhu Udara Minimum Bulanan': xls1.parse('Tmin_bln'),
    'Suhu Udara Maksimum Bulanan': xls1.parse('Tmax_bln'),
    'Kelembaban Udara Bulanan': xls1.parse('RH_bln'),
    'Rata-Rata Jumlah Hari dengan Kecepatan Angin >25 Knot Bulanan': xls1.parse('Wind_25_bln'),
    'PH Air Hujan Bulanan': xls1.parse('ph_bln'),
    'Lama Penyinaran Matahari Bulanan': xls1.parse('LPM_bln'),
    'Curah Hujan Tahunan': xls1.parse('CH_thn'),
    'Suhu Udara Tahunan': xls1.parse('Suhu_thn'),
    'Suhu Udara Maksimum Tahunan': xls1.parse('Tmax_abs_thn'),
    'Suhu Udara Minimum Tahunan': xls1.parse('Tmin_abs_thn'),
    'Laju Perubahan Suhu Udara Maksimum Tahunan': xls1.parse('trend_tmax_thn'),
    'Laju Perubahan Suhu Udara Minimum Tahunan': xls1.parse('trend_tmin_thn'),
    'Laju Perubahan Suhu Udara Rata-Rata Tahunan': xls1.parse('trend_trata_thn'),
    'Kelembaban Udara Tahunan': xls1.parse('RH_thn'),
    'Kelembaban Udara >90 % Tahunan': xls1.parse('RH_90_thn'),
    'Kelembaban Udara <70 % Tahunan': xls1.parse('RH_70_thn'),
    'PH Air Hujan Tahunan': xls1.parse('ph_thn'),
    'Suspended Particulate Matters (SPM) Tahunan': xls1.parse('SPM_thn'),
    'Rata-Rata Jumlah Hari dengan Kecepatan Angin >25 Knot Tahunan': xls1.parse('Wind_25_thn'),
    'Lama Penyinaran Matahari Tahunan': xls1.parse('LPM_thn'),
    }

# judul section 2
st.title('Data dan Metode')

st.divider()

# judul section 2.a
st.header('1. Data')

# narasi section 2.a
st.markdown('''
            <div class="justified-text">
Data pengamatan merupakan bahan dasar dari serangkaian kegiatan pengolahan sampai analisis. Data adalah sekeping fakta
            atau informasi yang menampilkan nilai tertentu, misalkan suhu udara, jumlah curah hujan dan lain-lain.
            Pada umumnya data cuaca dan iklim diamati menggunakan peralatan yang standard dan setiap jenis data cuaca
            dan iklim mempunyai satuan terkecil yang berbeda-beda. Berikut dijelaskan definisi data cuaca dan iklim.
            Pada hakekatnya data cuaca dan iklim adalah mempunyai definisi yang sama, perbedaannya hanya terletak pada satuan waktunya.
            Data cuaca adalah data hasil pengukuran unsur cuaca pada waktu tertentu dan pada tempat tertentu, sedangkan data iklim
            adalah rata-rata atau agregasi dari data cuaca dalam jangka waktu yang panjang misalnya 30 tahun.
            </div>
''', unsafe_allow_html=True)
st.markdown(''' ''')
st.markdown('''**Data yang digunakan untuk pengolahan Atlas Iklim adalah sebagai berikut:**''')

# narasi section 2.a
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**a.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data hujan harian : data hasil pengamatan curah hujan secara kumulatif pada periode tertentu.
    Untuk data hujan harian merupakan total jumlah curah hujan selama satu hari dari jam 07.00 waktu setempat
    sampai jam 07.00 hari berikutnya.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**b.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data suhu udara : data hasil pengamatan suhu udara menggunakan peralatan termometer setiap jam. Suhu yang diamati
    merupakan kondisi pada saat pengamatan yaitu pada periode 10 menit sebelum jam pengamatan
    (misalnya antara pukul 06.50 s.d. 07.00 untuk pengamatan pukul 07.00).</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**c.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data suhu maksimum dan minimum : data suhu maksimum diukur satu kali dalam sehari, suhu maksimum ini adalah
    suhu tertinggi yang dicapai selama satu hari. Demikian juga dengan suhu minimum, diamati satu kali dalam sehari,
    sehingga suhu minimum adalah suhu terendah yang dicapai selama satu hari.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**d.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data suhu rata-rata harian :  Rata-rata suhu harian yang dihitung menggunakan rumus tertentu, diantaranya rata-rata
    pengamatan tiap jam selama 24 jam, rata-rata tertimbang dari 3 kali pengamatan jam 07, 13 dan 18 waktu setempat.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**e.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data kelembaban udara : Rata-rata kelembaban udara harian yang dihitung menggunakan rumus tertentu,
    diantaranya rata-rata pengamatan tiap jam selama 24 jam, rata-rata tertimbang dari 3 kali pengamatan jam 07, 13 dan 18 waktu setempat.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**f.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data arah angin harian : Arah angin adalah arah datangnya gerakan udara / arah dari mana angin bertiup terbanyak selama 24 jam.
    Arah angin terbanyak selama satu hari yang diambil dari pengamatan arah angin per jam selama 24 jam.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**g.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data kecepatan angin harian.  Kecepatan angin tertinggi (dari hasil pengamatan per jam) yang terjadi dalam kurun waktu selama 24 jam.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**h.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data lama penyinaran matahari. Lamanya penyinaran matahari dari jam 08.00 sampai dengan jam 16.00.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**i.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data Keasaman air hujan (pH) : Derajat keasaman yang dihitung dari logaritma negatif konsentrasi ion Hidrogen pada air hujan.</div>
    ''', unsafe_allow_html=True)
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**j.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data kualitas udara (SPM) : Partikel polutan udara total yang berukuran lebih kecil dari 100 µm (mikrometer).</div>
    ''', unsafe_allow_html=True)

st.markdown(''' ''')

# Tampilkan plot di Streamlit
st.plotly_chart(fig, use_container_width=True)

# # judul tabel
# st.caption(f"**Tabel 1.** Data Stasiun {df1['Nama Stasiun'][0]}.")

# Dropdown untuk pilih data
selected_name = st.selectbox("📂 Pilih Dataset:", list(sheets.keys()))
df_tabel = sheets[selected_name]

# judul tabel
st.caption(f"**Tabel 1.** Data {selected_name} Periode Tahun 1991-2020 di Indonesia.")

# Menampilkan DataFrame yang dipilih menggunakan AgGrid
formatted_data = df_tabel.copy()

# Ubah kolom pertama jadi string
first_col = formatted_data.columns[0]
formatted_data[first_col] = formatted_data[first_col].astype(str)

# Reset index supaya kolom index (label paling kiri) hilang
formatted_data = formatted_data.reset_index(drop=True)

# Format semua kolom numerik (kecuali kolom pertama)
numeric_cols = formatted_data.select_dtypes(include='number').columns
numeric_format = {col: '{:.2f}' for col in numeric_cols}

# Terapkan style
styled_df = formatted_data.style.format(numeric_format)

# Tampilkan di Streamlit
st.dataframe(styled_df)

# narasi section 2.a
st.markdown('''<div class="justified-text">
Secara umum, data cuaca dan iklim dapat dijelaskan sebagai berikut :
</div>
''', unsafe_allow_html=True)

# narasi section 2.a
col1, col2 = st.columns([1, 30], gap='small')
with col1:
    st.markdown('''**-**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data cuaca dan iklim dikumpulkan dari hasil pengamatan menggunakan peralatan khusus,diamati pada waktu dan lokasi yang telah ditentukan.
    </div>''', unsafe_allow_html=True)
# narasi section 2.a
col1, col2 = st.columns([1, 30], gap='small')
with col1:
    st.markdown('''**-**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data telah dicek kualitasnya menggunakan metoda kendali mutu yang standar.
    </div>''', unsafe_allow_html=True)
# narasi section 2.a
col1, col2 = st.columns([1, 30], gap='small')
with col1:
    st.markdown('''**-**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data bulanan merupakan agregasi dari data pengamatan per jam dan data harian.
    </div>''', unsafe_allow_html=True)
# narasi section 2.a
col1, col2 = st.columns([1, 30], gap='small')
with col1:
    st.markdown('''**-**''')
with col2:
    st.markdown('''<div class="justified-text">
    Data yang digunakan terdiri dari data pengamatan in-situ.
    </div>''', unsafe_allow_html=True)

# judul section 2.b
st.header('2. Metode')

# narasi section 2.b
st.markdown('''<div class="justified-text">
Quisque egestas diam in arcu cursus euismod quis. A pellentesque sit amet porttitor eget dolor. Euismod in pellentesque massa placerat duis ultricies. In ante metus dictum at tempor commodo ullamcorper a lacus. Sit amet nisl purus in mollis nunc sed id semper. Adipiscing elit pellentesque habitant morbi. Vitae sapien pellentesque habitant morbi tristique senectus et netus. Vestibulum lectus mauris ultrices eros in. Pellentesque elit eget gravida cum sociis natoque. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor. Id venenatis a condimentum vitae. Nec ultrices dui sapien eget mi proin sed libero enim. Tellus at urna condimentum mattis pellentesque. Non sodales neque sodales ut etiam sit. Ut aliquam purus sit amet. Volutpat diam ut venenatis tellus in metus vulputate.
</div>''', unsafe_allow_html=True)

# penulisan rumus / algoritma
st.latex(r'''
    a r^{n-1} =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# narasi lanjutan section 2.b
st.markdown('''<div class="justified-text">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer vitae justo eget magna fermentum iaculis eu non. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. In nulla posuere sollicitudin aliquam ultrices sagittis. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Eget felis eget nunc lobortis mattis aliquam faucibus purus. Placerat in egestas erat imperdiet sed euismod nisi porta. Dictum at tempor commodo ullamcorper. Malesuada pellentesque elit eget gravida cum. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula.
</div>''', unsafe_allow_html=True)

# judul section 2.c
st.header('3. Quality Control')

# narasi section 2.c
st.markdown('''<div class="justified-text">
Tahapan yang paling krusial pada analisis klimatologi adalah kendali mutu data yang digunakan. Kendali mutu data terhadap
            data pengamatan dilakukan dalam tiga tahapan yaitu :</div>
            ''', unsafe_allow_html=True)

# narasi section 2.c
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**a.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Kendali mutu tingkat I : kendali mutu data yang dilakukan di Stasiun Pengamatan Iklim. Kendali mutu ini dilakukan
    pada saat pengamatan, penyandian dan pengiriman. Metode kendali mutu yang digunakan adalah mengecek data
    berdasarkan range tertentu (range check).</div>
    ''', unsafe_allow_html=True)

# narasi section 2.c
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**b.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Kendali mutu tingkat II : kendali mutu ini dilakukan setelah data terkumpul dalam jumlah yang panjang di Pusat Database.
    Metoda kendali mutu yang digunakan adalah range check, step-check (pengecekan terhadap perubahan nilai data
    terhadap perubahan waktu), spatial check (pengecekan data dengan membandingkan data dari satu stasiun terhadap stasiun sekitarnya).</div>
    ''', unsafe_allow_html=True)

# narasi section 2.c
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**c.**''')
with col2:
    st.markdown('''<div class="justified-text">
    Kendali mutu tingkat III : kendali mutu ini dilakukan pada tahap pengolahan data diantaranya pengecekan homogenitas data,
    pengecekan outlier, pengecekan keterkaitan antar parameter, dll.</div>
    ''', unsafe_allow_html=True)