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

# Load custom CSS file
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# judul section
st.title('Penutup')

st.divider()

# judul section
st.header('1. Kesimpulan')

# narasi utama
st.markdown('''
            <div class="justified-text">
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </div>
''', unsafe_allow_html=True)

# judul section 1
st.header('2. Saran')

# narasi pendahuluan
st.warning('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua [1].
           Tempus quam pellentesque nec nam aliquam sem et tortor. Vestibulum rhoncus est pellentesque elit ullamcorper. Diam vulputate ut pharetra sit amet aliquam.
           Sed turpis tincidunt id aliquet risus feugiat in ante. Auctor urna nunc id cursus metus aliquam eleifend mi. Tortor at risus viverra adipiscing at.
           Cras sed felis eget velit aliquet. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla. Arcu risus quis varius quam quisque id diam.
           Tempor orci eu lobortis elementum nibh tellus molestie nunc. Ultricies mi eget mauris pharetra et ultrices neque ornare. Odio eu feugiat pretium nibh ipsum.
           Vulputate dignissim suspendisse in est ante in nibh mauris. Rutrum quisque non tellus orci ac auctor. Ultrices dui sapien eget mi. Volutpat diam ut venenatis tellus in.
           Congue nisi vitae suscipit tellus mauris a. Elementum sagittis vitae et leo.

           Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis. Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla.
           Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Sapien et ligula ullamcorper malesuada proin. Feugiat nibh sed pulvinar proin gravida hendrerit lectus.
           Eget egestas purus viverra accumsan in nisl nisi. Libero id faucibus nisl tincidunt eget nullam non nisi. Arcu odio ut sem nulla pharetra diam sit amet nisl. Mollis nunc sed id semper risus.
           Quam elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. Ac odio tempor orci dapibus. In hac habitasse platea dictumst vestibulum rhoncus est. Sit amet dictum sit amet justo donec enim.
           Accumsan tortor posuere ac ut. Id aliquet risus feugiat in ante. Pulvinar pellentesque habitant morbi tristique senectus et netus et malesuada. Etiam tempor orci eu lobortis elementum nibh tellus.
''')

st.header('Daftar Pustaka')
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**1.**''')
with col2:
    st.markdown('''
                Li H, Tamang T, Nantasenamat C.
                Toward insights on antimicrobial selectivity of host defense peptides
                via machine learning model interpretation.
                Genomics. 2021;113(6):3851-3863.
                ''')
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**2.**''')
with col2:
    st.markdown('''
                Schaduangrat N, Malik AA, Nantasenamat C.
               ERpred: a web server for the prediction of subtype-specific estrogen receptor antagonists.
               PeerJ. 2021;9:e11716.''')
col1, col2 = st.columns([1, 20], gap='small')
with col1:
    st.markdown('''**3.**''')
with col2:
    st.markdown('''
                Schaduangrat N, Lampa S, Simeon S, Gleeson MP, Spjuth O, Nantasenamat C.
                Towards reproducible computational drug discovery. J Cheminform. 2020;12(1):9. 
                ''')