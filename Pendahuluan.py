# import library
import streamlit as st

# Setting layout halaman
# st.logo('Logo_BMKG_(2010).png') # logo pada sidebar
st.set_page_config(
        page_title="Atlas Iklim Digital",
        page_icon="🏠",
        layout="centered",
        initial_sidebar_state="expanded"
    )

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

######################################################
# Judul utama halaman
st.title('Atlas Iklim Indonesia 1991-2020')

# atribut tambahan
st.markdown('''
**Kedeputian Bidang Klimatologi**

*Badan Meteorologi Klimatologi dan Geofisika, Website: https://bmkg.go.id/*

''')

# judul section
st.header('Overview')

# narasi utama (abstrak)
st.info('''
Atlas Iklim Indonesia adalah alat interaktif (interactive tools) bagi masyarakat, peneliti, dunia usaha dan pemerintah
        untuk belajar mengenai perubahan iklim di Indonesia. Atlas ini menjelaskan trend dan perubahan
        serta proyeksi unsur iklim dan kualitas udara yang dikaitkan dengan perubahan iklim dalam skala lokal (Provinsi) dan Nasional.
''')

# atribut tambahan
st.markdown('**Keywords:** *Iklim*, *Atlas*, *Indonesia*, *Parameter*')

# judul section 1
st.header('Latar Belakang')

# narasi pendahuluan
st.markdown('''
            <div class="justified-text">
Kedeputian Bidang Klimatologi memiliki tugas dan fungsi berdasarkan ketentuan yang berlaku yaitu
            melaksanakan pemberian bimbingan teknis, pembinaan teknis dan pengendalian terhadap kebijakan teknis,
            koordinasi kegiatan fungsional dan kerjasama, pengelolaan dan pelayanan data dan informasi,
            dan penyampaian informasi iklim dan kualitas udara. Terkait dengan pelayanan,
            BMKG melalui Kedeputian Bidang Klimatologi telah memberikan layanan data dan informasi iklim dan kualitas udara
            kepada stakeholder dan masyarakat luas.  Jenis informasi yang disampaikan kepada masyarakat meliputi analisis
            dan prediksi jangka menengah (prediksi iklim mulai rentang waktu 10 harian, musiman dan tahunan) sampai jangka panjang (proyeksi).  
            </div>   
''', unsafe_allow_html=True)
st.markdown(''' ''')
st.markdown('''
            <div class="justified-text">
Seiring dengan terjadinya perubahan iklim, dampak yang dirasakan masyarakat adalah meningkatnya kejadian ekstrim
            (extreme event) baik pada skala cuaca maupun skala iklim. Informasi kejadian cuaca dan iklim ekstrim
            menjadi kebutuhan masyarakat dalam mengantisipasi dampak yang ditimbulkan. Resume iklim yang terjadi
            selama 30 tahun terakhir (1991-2020)  dapat menjadi acuan terbaru dan bisa dijadikan sebagai normal baru.
            Resume dan ikhtisar dari kondisi iklim dalam jangka yang panjang biasanya disajikan dalam bentuk Atlas Iklim. 
            </div>   
''', unsafe_allow_html=True)
st.markdown(''' ''')
st.markdown('''
            <div class="justified-text">
Atlas Iklim Indonesia adalah alat interaktif (interactive tools) bagi masyarakat, peneliti, dunia usaha dan pemerintah
            untuk belajar mengenai perubahan iklim di Indonesia. Atlas ini menjelaskan trend dan perubahan serta proyeksi
            unsur iklim dan kualitas udara yang dikaitkan dengan perubahan iklim dalam skala lokal (propinsi) dan nasional.
            Aspek perubahan iklim dapat ditunjukkan melalui eksplorasi menggunakan peta, grafik, data iklim untuk provinsi dan nasional.
            Disamping itu, deskripsi dengan bahasa yang sederhana akan memudahkan masyarakat memahami ilmu iklim. 
            </div>   
''', unsafe_allow_html=True)
st.markdown(''' ''')
st.markdown('''
            <div class="justified-text">
Atlas Iklim Indonesia memuat analisis unsur iklim yang diamati sejak puluhan tahun yang lalu dan proyeksi iklim hingga
            puluhan tahun yang akan datang. Analisis iklim meliputi kejadian iklim rata-rata, tertinggi, terendah dan
            trend perubahannya di wilayah provinsi dan  nasional. Dengan bahasa yang sederhana, Atlas Iklim menyajikan kejadian apa,
            terjadi di mana, dan kapan terjadinya. Disamping dalam bentuk buku, untuk memudahkan masyarakat mendapatkan informasi dimaksud,
            Atlas Indonesia disajikan secara interaktif melalui website.
            </div>   
''', unsafe_allow_html=True)
st.markdown(''' ''')
st.markdown('''
            <div class="justified-text">
Menurut WMO, unsur iklim yang digunakan sebagai indikator utama dalam mendeteksi trend dan perubahan iklim adalah suhu dan curah hujan
            serta beberapa unsur kualitas udara. Untuk itu, dalam Atlas Iklim Indonesia ini hanya akan menganalisis unsur iklim suhu,
            curah hujan dan beberapa unsur kualitas udara. Data suhu dan curah hujan dikumpulkan dari hasil pengamatan BMKG sejak
            pertama kali diamati di stasiun tertentu. Sebagai basis data akan digunakan data suhu dan curah hujan harian.
            </div>   
''', unsafe_allow_html=True)

# judul section 2
st.header('Tujuan')

# narasi section 2
st.markdown('''
            <div class="justified-text">
Tujuan dari dibuatnya Atlas Iklim Indonesia tahun 1991-2020 adalah menyajikan kondisi iklim Indonesia
            periode tahun 1991-2020 dalam bentuk gambar dan grafik agar pengguna informasi (Kementerian dan Lembaga terkait,
            Pemerintah Daerah, Peneliti, Perguruan Tinggi, stakeholder, dan masyarakat) mudah memahaminya.</div>
''', unsafe_allow_html=True)

# judul section 3
st.header('Manfaat')

# narasi section 3
st.markdown('''
            <div class="justified-text">
BMKG dan pengguna informasi iklim seperti, Kementerian dan Lembaga terkait, Pemerintah Daerah, Peneliti,
            Perguruan Tinggi, stakeholder, dan masyarakat umum mendapatkan informasi iklim 30 tahun terakhir
            untuk menjadi pertimbangan dalam merencanakan program dan kegiatannya.</div> 
''', unsafe_allow_html=True)
