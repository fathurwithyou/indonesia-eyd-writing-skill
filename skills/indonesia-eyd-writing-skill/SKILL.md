---
name: indonesia-eyd-writing-skill
description: Menulis, menyunting, memeriksa, dan menjelaskan teks bahasa Indonesia agar konsisten dengan EYD V dan rujukan resmi Badan Bahasa. Gunakan ketika Agent diminta membuat draf berbahasa Indonesia, memperbaiki ejaan/tanda baca/diksi penulisan kata, membedakan bentuk seperti di/ke sebagai kata depan vs imbuhan, menangani singkatan-akronim, angka-bilangan, unsur serapan, atau menjawab pertanyaan kaidah penulisan bahasa Indonesia.
---

# Indonesia EYD Writing

Gunakan skill ini untuk pekerjaan menulis dan penyuntingan bahasa Indonesia yang perlu patuh pada EYD V.

Jadikan `${CLAUDE_PLUGIN_ROOT}/references/` sebagai sumber rujukan utama. Jangan menyalin ulang isi reference ke jawaban atau ke file lain kecuali ringkasan singkat memang dibutuhkan untuk menyelesaikan tugas.

## Alur Kerja

1. Identifikasi bentuk tugas:
   - menulis draf baru;
   - menyunting teks yang sudah ada;
   - menjawab pertanyaan kaidah; atau
   - menjelaskan alasan revisi.
2. Tentukan kategori kaidah yang relevan.
3. Baca hanya file `${CLAUDE_PLUGIN_ROOT}/references/` yang relevan dengan masalah yang sedang ditangani.
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

- `${CLAUDE_PLUGIN_ROOT}/references/huruf-abjad.md`
- `${CLAUDE_PLUGIN_ROOT}/references/huruf-vokal.md`
- `${CLAUDE_PLUGIN_ROOT}/references/huruf-konsonan.md`
- `${CLAUDE_PLUGIN_ROOT}/references/gabungan-huruf-vokal.md`
- `${CLAUDE_PLUGIN_ROOT}/references/gabungan-huruf-konsonan.md`
- `${CLAUDE_PLUGIN_ROOT}/references/huruf-kapital.md`
- `${CLAUDE_PLUGIN_ROOT}/references/huruf-miring.md`
- `${CLAUDE_PLUGIN_ROOT}/references/huruf-tebal.md`

Gunakan kelompok ini untuk kapitalisasi, huruf miring/tebal, atau pertanyaan bentuk huruf.

### Penulisan Kata

- `${CLAUDE_PLUGIN_ROOT}/references/kata-dasar.md`
- `${CLAUDE_PLUGIN_ROOT}/references/kata-turunan.md`
- `${CLAUDE_PLUGIN_ROOT}/references/pemenggalan-kata.md`
- `${CLAUDE_PLUGIN_ROOT}/references/kata-depan.md`
- `${CLAUDE_PLUGIN_ROOT}/references/partikel.md`
- `${CLAUDE_PLUGIN_ROOT}/references/kata-ganti.md`
- `${CLAUDE_PLUGIN_ROOT}/references/kata-sandang.md`
- `${CLAUDE_PLUGIN_ROOT}/references/singkatan-akronim.md`
- `${CLAUDE_PLUGIN_ROOT}/references/angka-bilangan.md`

Gunakan kelompok ini untuk isu seperti:

- `di`, `ke`, dan `dari` sebagai kata depan;
- imbuhan dan bentuk turunan;
- partikel seperti `-lah`, `-kah`, dan `-pun`;
- penulisan gelar, singkatan, akronim, angka, dan bilangan.

### Tanda Baca

- `${CLAUDE_PLUGIN_ROOT}/references/tanda-titik.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-koma.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-titik-koma.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-titik-dua.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-hubung.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-pisah.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-elipsis.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-tanya.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-seru.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-petik.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-petik-tunggal.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-kurung.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-kurung-siku.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-apostrof.md`
- `${CLAUDE_PLUGIN_ROOT}/references/tanda-garis-miring.md`

Gunakan kelompok ini untuk pemisahan klausa, dialog/kutipan, sisipan, rentang, bentuk ulang, dan tanda baca lain yang memengaruhi struktur kalimat.

### Unsur Serapan

- `${CLAUDE_PLUGIN_ROOT}/references/serapan-pengantar.md`
- `${CLAUDE_PLUGIN_ROOT}/references/serapan-umum.md`
- `${CLAUDE_PLUGIN_ROOT}/references/serapan-khusus.md`

Gunakan kelompok ini saat pengguna meminta bentuk baku kata serapan atau ketika ada istilah asing yang perlu diputuskan apakah diserap, dimiringkan, atau dipertahankan.

## Pola Triage Cepat

- Jika masalahnya `dirumah` vs `di rumah`, baca `${CLAUDE_PLUGIN_ROOT}/references/kata-depan.md`.
- Jika masalahnya `siapa pun` vs `siapapun`, baca `${CLAUDE_PLUGIN_ROOT}/references/partikel.md`.
- Jika masalahnya nama jabatan, nama lembaga, atau awal kalimat, baca `${CLAUDE_PLUGIN_ROOT}/references/huruf-kapital.md`.
- Jika masalahnya `PT`, `Dr.`, `DNA`, atau bentuk akronim lain, baca `${CLAUDE_PLUGIN_ROOT}/references/singkatan-akronim.md`.
- Jika masalahnya koma, titik dua, tanda petik, atau dialog, baca file tanda baca yang relevan.
- Jika masalahnya istilah asing atau bentuk serapan, mulai dari `${CLAUDE_PLUGIN_ROOT}/references/serapan-pengantar.md`, lalu lanjut ke `serapan-umum.md` atau `serapan-khusus.md` sesuai kasus.

## Bentuk Output

Sesuaikan keluaran dengan permintaan pengguna.

- Jika pengguna hanya meminta revisi, berikan teks revisi terlebih dahulu.
- Jika pengguna meminta penjelasan, tambahkan alasan singkat per kategori perubahan.
- Jika pengguna meminta pengecekan cepat, cukup sebutkan kesalahan yang ditemukan dan bentuk benarnya.
- Jika pengguna meminta penulisan dari nol, hasilkan naskah yang langsung patuh EYD tanpa memaparkan seluruh aturan.

## Batasan

- Jangan mengklaim aturan yang tidak didukung oleh `${CLAUDE_PLUGIN_ROOT}/references/` atau sumber resmi yang disebut di dalamnya.
- Jangan memuat seluruh isi reference ke konteks bila hanya satu topik yang relevan.
- Jangan mengubah istilah teknis, nama merek, atau gaya editorial khusus tanpa alasan jelas.
- Jangan memaksakan penyesuaian yang mengubah makna kalimat.

## Sumber Resmi

Rujukan utama skill ini berasal dari portal resmi EYD:

- https://ejaan.kemendikdasmen.go.id/eyd/
