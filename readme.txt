✅ Cara agar main lebih aman dan collaborator hanya bisa branch/PR:
Masuk ke GitHub repository kamu

Klik tab Settings

Di sidebar kiri, klik Branches

Di bagian Branch protection rules, klik tombol Add rule

Isi:

Branch name pattern: main

Centang opsi-opsi berikut:

✅ Require a pull request before merging

✅ Require approvals (misalnya 1 approval)

✅ Restrict who can push to matching branches (tambahkan hanya kamu atau tim admin)

✅ (Opsional) Include administrators → supaya kamu juga gak bisa accidentally push ke main

Klik Create atau Save changes

🔒 Hasil dari ini:
Collaborator tidak bisa langsung push ke main

Mereka tetap bisa buat branch dari main

Mereka harus buat Pull Request (PR) dan menunggu approval (misalnya dari kamu)

Aman dari perubahan langsung di main

Kalau kamu mau bantu buat aturan ini, aku bisa kasih contoh step-by-step screenshot atau command line juga. Perlu?



✅ Pengaturan Aman untuk Branch main
Berikut opsi yang perlu kamu aktifkan:

1. ✅ Require a pull request before merging
"Require all commits be made to a non-target branch and submitted via a pull request before they can be merged."

Penjelasan: Mencegah push langsung ke main. Semua perubahan harus lewat Pull Request.

2. ✅ Required approvals → Isi: 1
"The number of approving reviews that are required before a pull request can be merged."

Penjelasan: Perlu minimal 1 orang menyetujui (reviewer lain, bisa kamu sendiri) sebelum PR bisa digabung ke main.

3. ✅ Restrict updates
"Only allow users with bypass permission to update matching refs."

Penjelasan: Mencegah semua orang (termasuk collaborator) dari mengubah branch main langsung. Hanya yang kamu izinkan (via bypass) yang bisa.

⚠️ Kalau kamu aktifkan ini, pastikan kamu tambahkan dirimu sendiri ke daftar bypass, kalau tidak kamu juga tidak bisa update main.

4. ✅ Block force pushes
"Prevent users with push access from force pushing to refs."

Penjelasan: Mencegah git push --force ke main yang bisa merusak riwayat commit.

5. ✅ Restrict deletions
"Only allow users with bypass permissions to delete matching refs."

Penjelasan: Mencegah main terhapus secara tidak sengaja.

Opsional tapi disarankan:
✅ Dismiss stale pull request approvals when new commits are pushed

✅ Require review from Code Owners (jika kamu pakai CODEOWNERS)

✅ Require conversation resolution before merging

🔧 Contoh Hasilnya
Dengan semua ini:

Collaborator hanya bisa membuat branch dari main

Mereka harus buat PR untuk mengubah main

Mereka tidak bisa push langsung ke main

PR harus kamu review dan approve dulu

Kalau kamu butuh bantu setting langsung atau lihat contoh visual cara nyetelnya, tinggal bilang aja! Mau aku bantuin step-by-step dalam bentuk gambar atau CLI juga bisa.



Berikut panduan step-by-step visual untuk mengatur Branch Protection Rule di GitHub agar collaborator tidak bisa langsung mengubah main, hanya bisa bikin branch dan PR saja.

🔐 Step-by-Step Setting Branch Protection Rule di GitHub
✅ 1. Buka Repository Kamu
Masuk ke GitHub

Buka repository kamu (misalnya: https://github.com/namamu/namarepo)

✅ 2. Klik Settings
Ada di tab paling kanan

✅ 3. Di sidebar kiri, klik Branches
✅ 4. Di bagian Branch protection rules, klik tombol “Add rule”
✅ 5. Atur seperti ini:
Pengaturan	Nilai yang Disarankan
Branch name pattern	main
✅ Require a pull request before merging	✔
✅ Required approvals	1 (atau lebih kalau kamu mau lebih ketat)
✅ Dismiss stale pull request approvals	✔
✅ Require review from Code Owners	✔ (opsional, kalau pakai CODEOWNERS)
✅ Require approval of most recent push	✔ (biar push terbaru harus di-review)
✅ Require conversation resolution	✔ (biar semua komentar diselesaikan dulu)
✅ Block force pushes	✔
✅ Restrict deletions	✔
✅ Restrict updates	✔ (tapi tambahkan dirimu di bypass list!)
✅ 6. Scroll ke bawah dan klik “Create”
📌 Penting!
Kalau kamu aktifkan:
Restrict updates dan Restrict deletions

Maka kamu harus menambahkan dirimu sendiri ke bagian:

“Restrict who can push to matching branches” atau “Bypass list”

Agar kamu tetap bisa push dan merge ke main.

🎯 Hasilnya:
Akses	Collaborator	Kamu
Push langsung ke main	❌ Tidak boleh	✅ Boleh (karena kamu bypass)
Bikin branch dari main	✅ Boleh	✅ Boleh
Buat PR ke main	✅ Boleh	✅ Boleh
Merge PR	❌ Tidak boleh tanpa approval	✅ Boleh
Kalau kamu mau, aku juga bisa bantu buatin file CODEOWNERS supaya otomatis kamu jadi reviewer pas ada PR. Mau sekalian?

"This ruleset does not target any resources and will not be applied" artinya aturan branch protection-mu belum mengarah ke branch apa pun, jadi GitHub tidak tahu harus menerapkan aturan ini ke mana.

✅ Solusi: Pastikan Branch name pattern sudah benar
Waktu kamu membuat ruleset, bagian ini harus kamu isi dengan nama branch yang ingin kamu proteksi, biasanya:

css
Salin
Edit
main
✅ Langkah cek dan perbaiki:
Buka repository kamu

Klik Settings > Branches

Klik pada ruleset yang kamu buat

Pastikan di bagian Branch name pattern, kamu isi dengan:

css
Salin
Edit
main
atau jika kamu ingin mencakup semua branch:

markdown
Salin
Edit
*
⚠️ Kalau kamu pakai default branch yang namanya master, kamu harus tulis master, bukan main.

🔍 Cara cek nama branch default
Kalau kamu gak yakin branch default-nya apa, kamu bisa cek:

Buka tab Code

Klik dropdown branch (kiri atas), dan lihat nama yang ditandai “default”

Biasanya main atau master

Setelah kamu isi Branch name pattern dengan benar (misalnya main), aturan baru akan aktif dan tidak akan muncul pesan error itu lagi.

Mau aku bantu cek nama branch default atau mau dibimbing langsung lagi untuk koreksi ruleset?


✅ Yang harus kamu lakukan sekarang:
Di bagian Targets, pastikan kamu melakukan ini:
Pilih "Target branches"

Di kolom "Branch name pattern" ➜ ketik:

css
Salin
Edit
main
(atau master kalau branch default kamu bernama master)

Setelah kamu ketik main, GitHub akan muncul preview:
"1 matching branch" atau semacamnya.

Baru klik Save ruleset atau Create.

📌 Penjelasan:
GitHub tidak akan menerapkan ruleset sampai kamu tentukan branch mana yang harus diproteksi.

Kalau kamu tulis main, maka hanya branch main yang dilindungi.

Kalau kamu tulis release/*, semua branch seperti release/v1, release/v2 akan dilindungi.

Kalau kamu tulis *, semua branch akan dilindungi (lebih global).

Kalau kamu kirim screenshot ruleset kamu di bagian “Target branches”, aku bisa bantu pastikan tidak ada kesalahan format. Mau dicontohin juga pakai gambar kalau perlu 😊


✅ Dengan tampilan:

"Applies to 1 target: main"

berarti sekarang ruleset kamu sudah aktif dan akan diterapkan ke branch main.

🔒 Sekarang yang terjadi adalah:
Collaborator tidak bisa:

Push langsung ke main

Delete atau force push ke main (kalau kamu aktifkan restriksi tersebut)

Merge tanpa PR dan review (kalau kamu aktifkan “Require pull request before merging”)

Kamu tetap bisa push ke main jika kamu ada di bypass list / admin permission

Kalau kamu mau tes:

Suruh collaborator bikin branch baru dari main

Push perubahan ke branch itu

Bikin Pull Request ke main

Kalau semua setting benar, dia tidak akan bisa merge langsung, dan akan butuh review dari kamu ✅

Kalau butuh bantuan buat CODEOWNERS atau otomasi approval, tinggal bilang aja. Mau lanjut ke sana?


✅ 1. Collaborator-mu punya izin "Admin" atau "Maintain"
Kalau akun kedua (kolaborator) punya admin permission, maka bisa bypass rules secara default.

💡 Solusi:
Ubah permission collaborator jadi "Write" saja, bukan Admin atau Maintain.

Cara ubah permission:
Buka repo kamu di GitHub

Masuk ke Settings > Collaborators and teams

Klik ikon pensil di sebelah akun collaborator

Ganti dari Admin menjadi Write

Klik Save

✅ 2. Kamu belum centang opsi “Do not allow bypassing the rules”
Waktu bikin ruleset, ada bagian seperti ini:

🔒 Bypass permissions
Users with the following roles can bypass rules...

💡 Solusi:
Edit ruleset yang tadi

Scroll ke bawah bagian Bypass permissions

Uncheck semua role seperti:

Administrators

Push access

Custom roles

Simpan ruleset

Ini akan memastikan bahkan admin pun gak bisa push langsung ke main — harus via pull request.

🔁 Setelah itu:
Pastikan akun collaborator logout dan login lagi biar refresh token

Coba lagi push ke main → seharusnya langsung ditolak GitHub

Kalau kamu mau, aku bisa bantu cek bareng dari awal. Cukup kirim screenshot:

Halaman Ruleset

Halaman Collaborators & roles

Atau, kalau kamu kasih nama repo dummy untuk tes, aku bantu setup contoh realnya juga. Gimana?


Repo kamu public atau private tidak memengaruhi apakah collaborator bisa push ke main — yang penting adalah kombinasi dari:

✅ 1. Permission level collaborator
Kalau collaborator kamu masih bisa edit main, sangat mungkin karena:

🚨 Dia punya Admin atau Maintain access
Dengan izin ini, dia bisa bypass semua rules.

🔍 Ceknya:
Masuk ke repo ➝ Settings > Collaborators and teams
Lihat kolom Role untuk akun tersebut. Harusnya "Write", bukan Admin.

✅ 2. Bypass permission masih aktif di ruleset
Saat membuat branch ruleset, GitHub ada pilihan:

Bypass permissions
✅ Allow administrators to bypass

Kalau ini dicentang, maka pengguna dengan permission admin tetap bisa push ke main.

🔧 Solusi:
Edit ruleset ➝ Scroll ke bawah bagian "Bypass permissions"
➝ Uncheck semua opsi (terutama Administrators dan Push access)
➝ Save

✅ 3. Ruleset status harus "Active"
Setelah semua disimpan, pastikan:

Ruleset status = ✅ Active

Target = ✅ main

Di collaborator view, coba git push langsung ➝ harusnya GitHub tolak dengan error seperti:

vbnet
Salin
Edit
remote: error: GH006: Protected branch update failed for refs/heads/main.
🔁 Uji Coba Lokal:
Kalau kamu mau pastikan sendiri:

Dari akun kedua (collaborator):

bash
Salin
Edit
git clone https://github.com/username/repo-name.git
cd repo-name
git checkout main
echo "test" >> coba.txt
git add .
git commit -m "test edit"
git push origin main
Kalau ruleset sudah betul, GitHub akan menolak push ke main langsung.
