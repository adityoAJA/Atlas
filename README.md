ini adalah project membuat atlas iklim interaktif Indonesia Tahun 2025 (streamlit)

catatan:
Menambahkan atau mengupdate data yang besar dan banyak (jadikan zip) lalu upload ke release, dengan cara sbb:
- Di repo kamu, klik tab “Releases” → klik “Draft a new release”. (sebelum itu, pastikan repo tidak empty saat klik release) ->  https://github.com/adityoAJA/Atlas/releases
- Isi versi (misal: v1.0), lalu upload file .zip/.rar.
- Klik “Publish release”.

GitHub Releases via browser memang punya limit 25MB per file saat upload lewat GitHub web interface langsung.
Tapi tenang, kamu tetap bisa upload file sampai 2GB ke Releases, asal pakai cara upload via GitHub CLI (Command Line Interface) atau Git LFS (Large File Storage). Nah, untuk kasus ini, pakai GitHub CLI adalah opsi paling simpel.
- https://cli.github.com/
- gh auth login
? Where do you use GitHub? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser
! First copy your one-time code: 85E4-BC91
- Salin kode tersebut (contohnya 85E4-BC91).
- Tekan Enter, maka browser akan terbuka ke halaman
- Paste kode tersebut di halaman itu lalu klik "Continue".
- Login ke akun GitHub kamu kalau diminta.
- Klik "Authorize GitHub CLI".

  Buat Release :
  - gh release create v1.0.0 --title "Initial PNG Release" --notes "Berisi semua file PNG"
  - gh release upload v1.0.0 all_pngs.zip
  - Jika belum bisa, lanjut langkah di bawah

Langkah install GIT di Windows:
- Download Git for Windows:
👉 https://git-scm.com/download/win
- Install seperti biasa:
- Klik Next terus sampai selesai.
- Pastikan opsi “Git from the command line and also from 3rd-party software” dipilih.
- Tunggu sampai instalasi selesai.
- Setelah selesai, restart terminal/command prompt kamu (atau buka terminal baru).
- git --version
- gh repo clone adityoAJA/Atlas
- cd Atlas
- gh release create v1.0.0 --title "Initial PNG Release" --notes "Berisi semua file PNG Atlas Iklim"
- move "C:\Users\apide\Downloads\peta.zip" "C:\Users\apide\Atlas\" (pindah/copy file atlas.zip ke repo Atlas)
- gh release upload v1.0.0 peta.zip
- Lalu akan dapat link_ID : url = "https://github.com/adityoAJA/Atlas/releases/download/v1.0.0/peta.zip"

Deploy ke Server: (cek git --> git --version) (kalau belum ada --> sudo apt install git)
Clone repo
- git clone https://github.com/adityoAJA/Atlas.git
- cd Atlas
Buat Virtual Env
- python3 -m venv env
- source env/bin/activate
Install dependencies
- pip install -r requirements.txt
Jalankan Skrip
- streamlit run Pendahuluan.py

Jalankan Git Pull (auto update) --> trigger
- screen -S streamlit-atlas (jalankan app streamlit di lokal, setelah clone menggunakan screen)
- cd /path/ke/folder/Atlas (sesuaikan path lokal)
- streamlit run app.py (jalankan pada screen)
- Buat Skrip Auto Pull + Restart:
  
#!/bin/bash
#Path ke repo lokal kamu
REPO_DIR="/path/ke/folder/Atlas"
#Masuk ke folder repo
cd "$REPO_DIR" || exit
#Tarik update dari GitHub
echo "Melakukan git pull pada $(date)" >> pull_log.txt
git pull origin main >> pull_log.txt 2>&1
#Hentikan streamlit di dalam screen (kalau ada)
screen -S streamlit-atlas -X quit
#Jalankan ulang streamlit dalam screen
screen -dmS streamlit-atlas bash -c "cd $REPO_DIR && streamlit run app.py"

- /home/username/scripts/auto_pull.sh (simpan sebagai sh --> sesuaikan nama dan path)
- chmod +x /home/username/scripts/auto_pull.sh (jalankan atau run kode.sh)
- crontab -e
- 0 7 5 * * /home/username/scripts/auto_pull.sh ( git pull dan restart app jam 07:00 pagi setiap tanggal 5 ) --> ganti jamnya sesuka hati, misal 0 0 5 * * untuk tengah malam.
- screen -ls (monitoring screen)
- screen -r streamlit-atlas (masuk ke screen)





