# Evaluasi Profil: Tugas Membuat Tulisan

Tiga subagen membuat naskah baru untuk lima profil. Setiap prompt meminta “Buatlah ...” karena skill ini dipakai untuk menghasilkan tulisan, bukan hanya menyuntingnya.

## Patokan

Saya memeriksa apakah hasilnya memakai bahasa yang wajar dan kalimat yang mudah diikuti. Saya juga menilai kesesuaian nada, ketepatan informasi, serta pemakaian konjungsi. Untuk tulisan populer, saya melihat apakah rincian mengalir tanpa menjadi deretan informasi.

**Hasil akhir: 5 dari 5 kasus lulus setelah satu perbaikan.** Caption populer pertama masih terasa seperti daftar, jadi arahan pada profilnya diperjelas dan kasus itu diulang. Nilai ini adalah pemeriksaan kualitatif, bukan benchmark independen.

## 1. Tulisan populer — lulus setelah perbaikan

**Masukan**

> Buatlah caption Instagram untuk orang tua tentang program Baca Bareng Sabtu di Rumah Baca Rintik. Program ini berisi kegiatan membaca nyaring dan membaca mandiri, berlangsung setiap Sabtu pukul 09.00–11.00, gratis, untuk anak usia 7–12 tahun yang didampingi orang tua/wali. Buku disediakan; anak perlu membawa botol minum. Kapasitas 15 anak, pendaftaran lewat WhatsApp 0812-3456-7890 paling lambat Jumat. Maksimal 90 kata, santai dan jelas. Jangan menambah manfaat, fasilitas, atau syarat lain.

**Contoh hasil setelah perbaikan profil**

> Yuk, ajak si kecil membaca di Rumah Baca Rintik Sabtu pagi. Dalam program Baca Bareng Sabtu, anak usia 7–12 tahun bisa ikut membaca nyaring dan membaca mandiri dengan didampingi orang tua atau wali. Kegiatan gratis ini berlangsung setiap Sabtu pukul 09.00–11.00. Buku disediakan; peserta perlu membawa botol minum. Karena kapasitasnya 15 anak, daftar lewat WhatsApp 0812-3456-7890 paling lambat Jumat.

**Penilaian: lulus.** Ajakan membuka caption, lalu rincian mengikuti alur kegiatan hingga pendaftaran. Semua informasi tetap ada dalam batas 90 kata. Uji awal menemukan gaya yang terlalu mirip daftar, jadi profil populer kini meminta agar syarat disisipkan ke dalam alur tulisan.

## 2. Tulisan teknis — lulus

**Masukan**

> Buatlah panduan ringkas untuk engineer on-call yang akan menjalankan deployment staging `billing-api`. Gunakan fakta berikut saja dan pertahankan semua identifier serta perintah persis seperti tertulis: ID panduan `OPS-17`; peran yang diperlukan `ops-staging`; build harus berstatus `approved`; jalankan perintah dari root repository: `npm run deploy:staging -- --service billing-api`. Setelah selesai, periksa panel Releases. Deployment siap jika entri terbaru menunjukkan `environment: staging` dan `status: ready`. Jika status belum `ready`, catat `release_id` dan laporkan di `#platform-oncall`.

**Contoh hasil**

> **OPS-17 — Deployment staging `billing-api`**
>
> Sebelum mulai, pastikan akun Anda memiliki peran `ops-staging` dan build berstatus `approved`. Panduan ini hanya berlaku untuk environment staging.
>
> Dari root repository, jalankan:
>
> ```sh
> npm run deploy:staging -- --service billing-api
> ```
>
> Setelah proses selesai, buka panel Releases. Deployment siap jika entri terbaru untuk `billing-api` menunjukkan `environment: staging` dan `status: ready`. Jika belum, catat `release_id` lalu laporkan di `#platform-oncall`.

**Penilaian: lulus.** Langkahnya berurutan dan mudah diikuti. Perintah serta semua identifier tetap persis, sementara kondisi siap dan tindak lanjut dijelaskan dengan jelas.

## 3. Komunikasi kerja — lulus

**Masukan**

> Buatlah pesan singkat untuk grup kerja yang meminta rekan meninjau draf panduan peserta pelatihan di folder Bersama > Pelatihan. Minta masukan paling lambat Rabu, 11 November, agar saya sempat merapikan draf untuk dibagikan Kamis, 12 November. Nadanya profesional tapi hangat, maksimal empat kalimat. Jangan menyebut persetujuan sudah diberikan atau membuat tenggat baru.

**Contoh hasil**

> Halo, teman-teman. Draf panduan untuk peserta pelatihan sudah tersedia di folder Bersama > Pelatihan. Boleh kirimkan masukan paling lambat Rabu, 11 November? Saya akan merapikannya untuk dibagikan Kamis, 12 November.

**Penilaian: lulus.** Pesannya hangat dan langsung keperluan. Tujuan tenggat tersampaikan dengan alami, tanpa menambah persetujuan atau tenggat baru.

## 4. Proposal riset — lulus

**Masukan**

> Buatlah satu paragraf 120–150 kata untuk latar belakang dan tujuan proposal penelitian. Gunakan hanya bahan berikut; bedakan temuan terdahulu dari rencana penelitian, dan jangan menyatakan hubungan sebab-akibat.
>
> **Sumber yang sudah diperiksa:** Burnell et al. (2022), “Associations Between Adolescents' Daily Digital Technology Use and Sleep,” *Journal of Adolescent Health*, 70(3), 450–456, DOI `10.1016/j.jadohealth.2021.09.033`. Ringkasan abstrak: 388 remaja mengisi laporan harian tentang penggunaan teknologi digital dan tidur selama dua minggu; subkelompok 254 remaja memakai perangkat wearable untuk mencatat tidur selama rata-rata 3,4 hari. Penggunaan digital nonakademik yang lebih lama dibanding teman sebaya berkaitan dengan durasi tidur yang dilaporkan sendiri lebih pendek dan waktu tidur lebih larut. Hubungan dalam perbandingan tiap peserta sendiri hanya sedikit dan tidak konsisten.
>
> **Rencana:** studi observasional terhadap 120 siswa berusia 15–17 tahun dari tiga SMA di Surabaya selama 14 hari. Siswa akan mencatat penggunaan digital nonakademik dan pesan setiap hari; durasi tidur diukur dengan perangkat wearable. Tujuan penelitian adalah mengestimasi hubungan harian tersebut pada tiap peserta.

**Contoh hasil dari subagen**

> Burnell et al. (2022) mengamati 388 remaja selama dua minggu melalui laporan harian tentang penggunaan teknologi dan tidur; subkelompok 254 remaja juga memakai perangkat wearable untuk mencatat tidur selama rata-rata 3,4 hari. Penggunaan teknologi digital nonakademik yang lebih lama daripada teman sebaya berkaitan dengan durasi tidur yang dilaporkan sendiri lebih pendek dan waktu tidur lebih larut. Namun, hubungan dalam perbandingan harian tiap peserta hanya sedikit dan tidak konsisten. Temuan ini menjadi alasan untuk menguji hubungan penggunaan digital dan tidur pada siswa di Surabaya. Penelitian yang diusulkan akan mengikuti 120 siswa berusia 15–17 tahun dari tiga SMA selama 14 hari. Siswa akan mencatat penggunaan digital nonakademik dan pesan, sementara durasi tidur diukur dengan perangkat wearable. Studi observasional ini bertujuan mengestimasi hubungan harian pada tiap peserta, bukan menguji sebab-akibat.

**Penilaian: lulus.** Bahasanya lugas dan mengalir. “Namun” menandai batas temuan, sementara “sementara” menghubungkan dua cara pengukuran. Klaim dari studi terdahulu dibedakan dari rencana; hasil observasional tidak diubah menjadi sebab-akibat. Metadata artikel dan isi abstrak cocok dengan [catatan PubMed](https://pubmed.ncbi.nlm.nih.gov/34756778/).

## 5. Tulisan kreatif — lulus

**Masukan**

> Buatlah cerpen mini sekitar 100 kata dengan sudut pandang orang pertama dan bahasa Indonesia sehari-hari. Aku sedang berteduh di warung saat pemiliknya mengira aku pelanggan lama yang pernah berutang. Buat suasananya canggung tapi hangat; dialog boleh santai. Jangan akhiri dengan pesan moral.

**Contoh hasil**

> “Dimas, akhirnya kelihatan juga,” kata Bu Sari, menaruh segelas teh di depanku.
>
> Aku menunjuk diri sendiri. “Saya?”
>
> “Lho, bukan Dimas? Rambutnya sama.”
>
> “Bukan, Bu. Saya baru pindah ke sini.”
>
> Bu Sari tertawa kecil, lalu menggaruk pipinya. “Pantas saja. Dimas biasanya datang pas hujan, kabur dari yang nagih.”
>
> Aku ikut tertawa. Di luar, air mengalir dari ujung terpal ke selokan. Bu Sari menggeser piring pisang goreng ke dekatku.
>
> “Ini gratis. Maaf tadi salah orang.”
>
> “Kalau saya jadi langganan, utangnya ikut diwariskan?”
>
> “Jangan kasih ide,” katanya, tapi dia tersenyum sambil menuang teh lagi.

**Penilaian: lulus.** Cerita memakai sudut pandang orang pertama, menjaga suasana canggung dan hangat, serta berakhir pada adegan, bukan pesan moral. Dialognya santai dan tidak dibakukan.

## Batas evaluasi

Subagen membuat keluaran; saya menilainya secara manual dengan patokan di atas. Contoh ini menunjukkan cara kerja pada lima prompt, tetapi belum mengukur konsistensi pada banyak penulis atau dibandingkan dengan penilai independen.
