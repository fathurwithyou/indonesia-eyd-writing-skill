---
name: indonesia-eyd-writing-skill
description: Menulis, menyunting, memeriksa, dan menjelaskan teks bahasa Indonesia agar konsisten dengan EYD V dan rujukan resmi Badan Bahasa. Gunakan ketika Agent diminta membuat draf berbahasa Indonesia, memperbaiki ejaan/tanda baca/diksi penulisan kata, membedakan bentuk seperti di/ke sebagai kata depan vs imbuhan, menangani singkatan-akronim, angka-bilangan, unsur serapan, atau menjawab pertanyaan kaidah penulisan bahasa Indonesia.
---

# Indonesia EYD Writing

Gunakan skill ini untuk pekerjaan menulis dan penyuntingan bahasa Indonesia yang perlu patuh pada EYD V.

Jadikan `references/` sebagai sumber rujukan utama. Jangan menyalin ulang isi reference ke jawaban atau ke file lain kecuali ringkasan singkat memang dibutuhkan untuk menyelesaikan tugas.

## Alur Kerja

1. Identifikasi bentuk tugas:
   - menulis draf baru;
   - menyunting teks yang sudah ada;
   - menjawab pertanyaan kaidah; atau
   - menjelaskan alasan revisi.
2. Tentukan kategori kaidah yang relevan.
3. Baca hanya file `references/` yang relevan dengan masalah yang sedang ditangani.
4. Terapkan kaidah tanpa mengubah maksud, fakta, nada, atau tingkat formalitas pengguna kecuali diminta.
5. Kembalikan hasil sesuai kebutuhan tugas:
   - untuk penyuntingan: berikan versi revisi;
   - untuk proofreading: sorot perubahan penting dan alasannya secara singkat;
   - untuk pertanyaan kaidah: jawab langsung lalu beri contoh ringkas;
   - untuk penulisan baru: hasilkan teks yang sudah patuh EYD sejak awal.

## Aturan Operasional

- Prioritaskan perbaikan yang berdampak langsung pada keterbacaan dan kepatuhan EYD: kapitalisasi, penulisan kata, tanda baca, dan unsur serapan.
- Bedakan koreksi ejaan dari perubahan gaya. Jangan mengubah gaya jika masalahnya hanya kaidah.
- Jika pengguna memberi teks sumber, kerjakan berdasarkan teks itu, bukan contoh buatan sendiri.
- Jika ada banyak potensi masalah, periksa yang paling mungkin salah terlebih dahulu: `di/ke`, kapitalisasi nama diri, tanda baca antarklausa, partikel, dan singkatan.
- Jika pertanyaan menyentuh area tertentu, buka reference yang spesifik untuk area itu, bukan seluruh folder.
- Jika ragu antara dua bentuk, pilih bentuk yang paling defensible berdasarkan reference yang tersedia dan sebutkan kaidahnya secara singkat.

## Cara Menggunakan References

Pilih file berdasarkan jenis masalah.

### Penggunaan Huruf

- `references/huruf-abjad.md`
- `references/huruf-vokal.md`
- `references/huruf-konsonan.md`
- `references/gabungan-huruf-vokal.md`
- `references/gabungan-huruf-konsonan.md`
- `references/huruf-kapital.md`
- `references/huruf-miring.md`
- `references/huruf-tebal.md`

Gunakan kelompok ini untuk kapitalisasi, huruf miring/tebal, atau pertanyaan bentuk huruf.

### Penulisan Kata

- `references/kata-dasar.md`
- `references/kata-turunan.md`
- `references/pemenggalan-kata.md`
- `references/kata-depan.md`
- `references/partikel.md`
- `references/kata-ganti.md`
- `references/kata-sandang.md`
- `references/singkatan-akronim.md`
- `references/angka-bilangan.md`

Gunakan kelompok ini untuk isu seperti:

- `di`, `ke`, dan `dari` sebagai kata depan;
- imbuhan dan bentuk turunan;
- partikel seperti `-lah`, `-kah`, dan `-pun`;
- penulisan gelar, singkatan, akronim, angka, dan bilangan.

### Tanda Baca

- `references/tanda-titik.md`
- `references/tanda-koma.md`
- `references/tanda-titik-koma.md`
- `references/tanda-titik-dua.md`
- `references/tanda-hubung.md`
- `references/tanda-pisah.md`
- `references/tanda-elipsis.md`
- `references/tanda-tanya.md`
- `references/tanda-seru.md`
- `references/tanda-petik.md`
- `references/tanda-petik-tunggal.md`
- `references/tanda-kurung.md`
- `references/tanda-kurung-siku.md`
- `references/tanda-apostrof.md`
- `references/tanda-garis-miring.md`

Gunakan kelompok ini untuk pemisahan klausa, dialog/kutipan, sisipan, rentang, bentuk ulang, dan tanda baca lain yang memengaruhi struktur kalimat.

### Unsur Serapan

- `references/serapan-pengantar.md`
- `references/serapan-umum.md`
- `references/serapan-khusus.md`

Gunakan kelompok ini saat pengguna meminta bentuk baku kata serapan atau ketika ada istilah asing yang perlu diputuskan apakah diserap, dimiringkan, atau dipertahankan.

## Pola Triage Cepat

- Jika masalahnya `dirumah` vs `di rumah`, baca `references/kata-depan.md`.
- Jika masalahnya `siapa pun` vs `siapapun`, baca `references/partikel.md`.
- Jika masalahnya nama jabatan, nama lembaga, atau awal kalimat, baca `references/huruf-kapital.md`.
- Jika masalahnya `PT`, `Dr.`, `DNA`, atau bentuk akronim lain, baca `references/singkatan-akronim.md`.
- Jika masalahnya koma, titik dua, tanda petik, atau dialog, baca file tanda baca yang relevan.
- Jika masalahnya istilah asing atau bentuk serapan, mulai dari `references/serapan-pengantar.md`, lalu lanjut ke `serapan-umum.md` atau `serapan-khusus.md` sesuai kasus.

## Bentuk Output

Sesuaikan keluaran dengan permintaan pengguna.

- Jika pengguna hanya meminta revisi, berikan teks revisi terlebih dahulu.
- Jika pengguna meminta penjelasan, tambahkan alasan singkat per kategori perubahan.
- Jika pengguna meminta pengecekan cepat, cukup sebutkan kesalahan yang ditemukan dan bentuk benarnya.
- Jika pengguna meminta penulisan dari nol, hasilkan naskah yang langsung patuh EYD tanpa memaparkan seluruh aturan.

## Batasan

- Jangan mengklaim aturan yang tidak didukung oleh `references/` atau sumber resmi yang disebut di dalamnya.
- Jangan memuat seluruh isi reference ke konteks bila hanya satu topik yang relevan.
- Jangan mengubah istilah teknis, nama merek, atau gaya editorial khusus tanpa alasan jelas.
- Jangan memaksakan penyesuaian yang mengubah makna kalimat.

## Sumber Resmi

Rujukan utama skill ini berasal dari portal resmi EYD:

- https://ejaan.kemendikdasmen.go.id/eyd/
