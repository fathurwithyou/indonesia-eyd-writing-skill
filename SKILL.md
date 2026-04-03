---
name: indonesia-eyd-writing-skill
description: Menulis, menyunting, memeriksa, dan menjelaskan teks bahasa Indonesia agar konsisten dengan EYD V dan rujukan resmi Badan Bahasa. Gunakan ketika Agent diminta membuat draf berbahasa Indonesia, memperbaiki ejaan/tanda baca/diksi penulisan kata, membedakan bentuk seperti di/ke sebagai kata depan vs imbuhan, menangani singkatan-akronim, angka-bilangan, unsur serapan, atau menjawab pertanyaan kaidah penulisan bahasa Indonesia.
---

# Indonesia EYD Writing

Gunakan skill ini untuk pekerjaan menulis dan penyuntingan bahasa Indonesia yang perlu patuh pada EYD V.

## Prinsip Utama

- Wajib baca `references/eyd/eyd-v.md` terlebih dahulu sebelum membuka rujukan EYD lain.
- Jadikan `references/eyd/eyd-v.md` sebagai rujukan utama untuk pertanyaan umum, lintas topik, atau saat perlu pijakan resmi yang paling lengkap.
- Gunakan file granular di `references/eyd/` hanya jika kasusnya sempit dan spesifik.
- Gunakan `references/seri-penyuluhan/` hanya saat perlu penjelasan tambahan, contoh, atau pembahasan yang lebih naratif.
- Gunakan `references/highlights/` hanya untuk ringkasan cepat, bukan untuk mengalahkan kaidah di folder `eyd/`.
- Jangan memuat banyak file sekaligus. Ambil sesedikit mungkin yang cukup untuk menyelesaikan tugas.

## Urutan Rujukan

1. `references/eyd/eyd-v.md`
2. `references/eyd/<topik-spesifik>.md`
3. `references/seri-penyuluhan/*.md`
4. `references/highlights/*.md`

## Alur Kerja

1. Identifikasi bentuk tugas: menulis, menyunting, menjawab kaidah, atau menjelaskan revisi.
2. Tentukan apakah masalahnya umum atau spesifik.
3. Baca `references/eyd/eyd-v.md` terlebih dahulu.
4. Jika kasusnya masih terlalu umum atau bercampur banyak topik, tetap gunakan `references/eyd/eyd-v.md` sebagai pijakan utama.
5. Jika spesifik, buka hanya file tambahan yang tepat di `references/eyd/`.
6. Terapkan kaidah tanpa mengubah maksud, fakta, nada, atau tingkat formalitas pengguna kecuali diminta.
7. Kembalikan hasil sesuai bentuk permintaan pengguna.

## Triage Cepat

- `di rumah` vs `dirumah`: `references/eyd/kata-depan.md`
- `siapa pun` vs `siapapun`: `references/eyd/partikel.md`
- kapitalisasi nama jabatan, lembaga, geografi: `references/eyd/huruf-kapital.md`
- singkatan, gelar, akronim: `references/eyd/singkatan-akronim.md`
- angka dan bilangan: `references/eyd/angka-bilangan.md`
- koma, titik dua, petik, hubung, pisah, elipsis: file terkait di `references/eyd/`
- unsur serapan: mulai dari `references/eyd/serapan-pengantar.md`
- jika masalah bercampur antara huruf, kata, dan tanda baca: kembali ke `references/eyd/eyd-v.md`

## Aturan Operasional

- Prioritaskan koreksi yang langsung memengaruhi kepatuhan EYD: kapitalisasi, penulisan kata, tanda baca, singkatan, angka, dan serapan.
- Bedakan koreksi kaidah dari perubahan gaya. Jangan mengubah gaya bila masalahnya hanya kepatuhan EYD.
- Jika pengguna memberi teks sumber, kerjakan berdasarkan teks itu, bukan contoh buatan sendiri.
- Jika ada banyak potensi masalah, cek yang paling sering keliru lebih dahulu: `di/ke`, kapitalisasi nama diri, tanda baca antarklausa, partikel, dan singkatan.
- Jika ragu antara dua bentuk, pilih bentuk yang paling defensible berdasarkan rujukan yang tersedia dan sebutkan kaidahnya secara singkat.

## Bentuk Output

- Jika pengguna meminta revisi, berikan teks revisi terlebih dahulu.
- Jika pengguna meminta penjelasan, tambahkan alasan singkat per kategori perubahan.
- Jika pengguna meminta pengecekan cepat, cukup sebutkan kesalahan yang ditemukan dan bentuk benarnya.
- Jika pengguna meminta penulisan dari nol, hasilkan naskah yang langsung patuh EYD tanpa memaparkan semua aturan.

## Batasan

- Jangan mengklaim aturan yang tidak didukung oleh `references/` atau sumber resmi yang disebut di dalamnya.
- Jangan memuat seluruh folder atau seluruh dokumen panjang ke konteks jika hanya satu bagian yang relevan.
- Jangan mengutamakan file ringkasan di atas rujukan utama EYD.
- Jangan mengubah istilah teknis, nama merek, atau gaya editorial khusus tanpa alasan jelas.
- Jangan memaksakan penyesuaian yang mengubah makna kalimat.

## Sumber Resmi

Rujukan utama skill ini berasal dari portal resmi EYD:

- https://ejaan.kemendikdasmen.go.id/eyd/
