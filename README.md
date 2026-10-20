# Indonesia EYD Writing Skill

Skill penulisan bahasa Indonesia untuk naskah riset, karya kreatif, komunikasi profesional, tulisan populer, serta dokumentasi teknis. EYD V menjadi dasar ejaan; tujuan, pembaca, dan medium menentukan cara menulis.

**Visi:** membantu penulis menghasilkan naskah yang akurat, jelas, dan sesuai konteks tanpa kehilangan makna atau suara penulis.

Nama teknis `indonesia-eyd-writing-skill` dipertahankan agar instalasi dan pemanggilan sebelumnya tetap dikenali. Nama tampilan: **Penulisan Bahasa Indonesia**.

## Cakupan

| Profil | Contoh | Fokus |
| --- | --- | --- |
| Riset dan akademik | Laporan penelitian, proposal riset, abstrak, tinjauan pustaka | Hubungan klaim dan bukti, batas kepastian, sitasi, konsistensi istilah |
| Kreatif | Cerpen, novel, puisi, dialog | Suara, irama, sudut pandang, kesinambungan cerita |
| Profesional | Email, pesan kerja, memo, komentar tiket | Keperluan, konteks, tindakan berikutnya, kesopanan |
| Populer | Artikel, esai, blog, konten edukatif | Alur gagasan, contoh konkret, keterbacaan, akurasi |
| Teknis dan produk | Dokumentasi, tutorial, spesifikasi, teks antarmuka | Urutan tindakan, ketepatan istilah, keutuhan kode dan pengenal |

Profil tulisan berbeda dari tingkat revisi. Untuk setiap profil, pengguna dapat meminta **koreksi**, **sunting**, **tata ulang**, **tulis**, atau **penjelasan kaidah**. Jika tidak disebutkan, agen memilih perubahan paling kecil yang memenuhi permintaan.

Skill tidak menggantikan pedoman penerbit, verifikasi sumber, atau pemeriksaan fakta. Panduan genre merupakan saran editorial; ketentuan ejaan dirujukkan ke EYD. Tidak ada salinan KBBI dalam paket.

## Struktur dan pemuatan konteks

Sumber utama yang diedit berada pada akar repositori:

| Lokasi | Fungsi |
| --- | --- |
| `SKILL.md` | Menentukan konteks, tingkat revisi, profil, rujukan, dan pemeriksaan akhir |
| `references/editorial/context.md` | Ringkasan konteks dan konsistensi proyek panjang |
| `references/editorial/principles.md` | Kejelasan, suara, dan penjagaan makna |
| `references/editorial/sources.md` | Kewenangan EYD, KBBI, pedoman institusi, dan sumber fakta |
| `references/profiles/*.md` | Alur dan tolok mutu untuk lima jenis tulisan |
| `references/eyd/` | Naskah utama EYD V dan rujukan per topik |
| `references/seri-penyuluhan/` | Penjelasan pendamping tentang ejaan, kalimat, dan pilihan kata |
| `references/highlights/` | Ikhtisar cepat |
| `agents/openai.yaml` | Nama tampilan dan contoh prompt untuk host yang mendukungnya |
| `skills/indonesia-eyd-writing-skill/` | Salinan distribusi plugin, dibangkitkan dari sumber utama |
| `scripts/` | Sinkronisasi serta pemeriksaan struktur distribusi |
| `evals/cases.json` | Kasus evaluasi perilaku dan kriteria penilaian |

Agen memuat panduan utama, satu profil yang sesuai, lalu bagian rujukan yang diperlukan. Pertanyaan ejaan murni tidak membutuhkan profil. Tugas campuran dapat memuat dua profil. Seluruh korpus EYD tidak perlu dimasukkan ke konteks sekaligus.

## Instalasi

### Menggunakan skills CLI

```bash
npx skills add fathurwithyou/indonesia-eyd-writing-skill --skill indonesia-eyd-writing-skill
```

Pilih agen tujuan pada dialog pemasangan. Instalasi CLI ini terpisah dari pemasangan plugin Claude Code; pilih satu jalur agar skill tidak muncul dua kali.

### Claude Code melalui marketplace

```text
/plugin marketplace add fathurwithyou/indonesia-eyd-writing-skill
/plugin install indonesia-eyd-writing-skill@indonesia-eyd
```

### Pemasangan manual

Salin `SKILL.md`, `references/`, dan `agents/` sebagai satu folder skill ke lokasi yang sesuai. Jangan menyalin seluruh repositori ke dalam folder skill sehingga salinan distribusinya ikut terpasang dua kali.

| Lingkungan | Folder proyek | Folder pengguna |
| --- | --- | --- |
| Codex CLI / IDE | `.agents/skills/indonesia-eyd-writing-skill/` | `~/.agents/skills/indonesia-eyd-writing-skill/` |
| Claude Code | `.claude/skills/indonesia-eyd-writing-skill/` | `~/.claude/skills/indonesia-eyd-writing-skill/` |

Untuk host dengan unggah skill, sertakan tiga komponen yang sama sesuai mekanisme unggah host tersebut. Ketersediaan dan tampilan pengelolaan skill mengikuti produk yang digunakan.

## Cara memanggil

| Lingkungan | Pemanggilan eksplisit |
| --- | --- |
| ChatGPT dengan skill yang sudah tersedia | Ketik `@`, lalu pilih **Penulisan Bahasa Indonesia** atau nama yang terdaftar |
| Codex CLI / IDE | `$indonesia-eyd-writing-skill`; gunakan `/skills` untuk melihat daftar |
| Claude Code, instalasi skill langsung | `/indonesia-eyd-writing-skill` |
| Claude Code, instalasi plugin marketplace | `/indonesia-eyd-writing-skill:indonesia-eyd-writing-skill` |

Profil seperti `riset` dan `kreatif` merupakan konteks dalam prompt, bukan subperintah terpisah. Tidak ada perintah `/riset` atau `$riset` dalam paket ini. Agen juga dapat memilih skill secara otomatis jika deskripsi tugas cocok; gunakan pemanggilan eksplisit untuk memastikan pilihan.

### Contoh riset

```text
$indonesia-eyd-writing-skill
Sunting latar belakang laporan penelitian tentang umur simpan roti
untuk pembaca jurnal pangan.
Perjelas alur masalah dan pertahankan istilah, sitasi, serta tingkat kepastian.
Jangan menambahkan klaim atau referensi. Berikan naskah revisi saja.

[paragraf]
```

### Contoh kreatif

```text
$indonesia-eyd-writing-skill
Sunting cerpen tentang penjaga mercusuar berikut pada tingkat kalimat.
Pertahankan sudut pandang orang pertama, dialog informal, dan suasana sepi.
Jangan menambah tokoh atau mengubah akhir cerita.

[cerpen]
```

### Contoh profesional

```text
$indonesia-eyd-writing-skill
Rapikan pesan kepada pemasok untuk meminta konfirmasi jadwal pengiriman.
Tetap sopan dan lugas, maksimal 80 kata. Jangan menambah tenggat atau janji.

[pesan]
```

### Contoh populer

```text
$indonesia-eyd-writing-skill
Tulis artikel 500 kata tentang pengurangan sisa makanan di rumah tangga
berdasarkan catatan berikut. Gunakan satu contoh hipotetis yang jelas
ditandai. Jangan mengarang statistik.

[catatan]
```

### Contoh teknis

```text
$indonesia-eyd-writing-skill
Sunting petunjuk penggunaan mesin pengemas berikut untuk operator baru.
Perjelas prasyarat dan urutan langkah. Pertahankan kode model, nama tombol,
suhu, dan durasi. Tandai kemampuan alat yang belum didukung bahan sumber.

[petunjuk]
```

### Konteks yang membantu

Untuk permintaan singkat, cukup berikan tugas dan teks. Untuk proyek panjang, tambahkan pembaca, tujuan, bahan/sumber, ragam, panjang, pedoman institusi, bagian yang harus dipertahankan, dan bentuk keluaran. Agen tidak perlu meminta semuanya jika sudah jelas dari konteks.

Contoh ringkas: `Sunting abstrak penelitian pengeringan mangga ini untuk pembaca jurnal pangan, maksimal 200 kata, pertahankan angka dan sitasi, keluaran naskah saja.`

Seluruh contoh buatan menggunakan situasi rekaan yang umum. Identitas, pengalaman, institusi, dan proyek dari memori atau riwayat percakapan pengguna tidak digunakan sebagai bahan contoh tanpa permintaan eksplisit.

## Pemeliharaan

Edit sumber pada akar repositori, lalu bangkitkan salinan plugin:

```bash
python3 scripts/sync_distribution.py
python3 scripts/check_skill.py
```

Pemeriksaan memerlukan Python 3.10+ dan PyYAML (`python3 -m pip install PyYAML`). CI memeriksa metadata, tautan sumber utama, kelengkapan rujukan, manifest, dan kesamaan salinan distribusi. Skrip sinkronisasi hanya menulis `SKILL.md`, `references/`, dan `agents/` pada folder distribusi yang sudah ditentukan.

Kasus dalam `evals/cases.json` digunakan untuk evaluasi perilaku agen, bukan tes kecocokan kalimat persis. Jalankan prompt pada sesi baru dengan skill terpasang, kemudian nilai tiap kriteria berdasarkan jawaban dan jejak pembacaan berkas. Pemeriksaan struktur tidak membuktikan mutu penulisan atau kebenaran seluruh salinan rujukan.

Untuk menambah jenis tulisan, buat satu profil dengan konteks minimum, alur, batas perubahan, contoh, dan tolok mutu; daftarkan di `SKILL.md`; tambah kasus evaluasi; sinkronkan distribusi. Pisahkan menjadi skill mandiri hanya jika alur dan pemanggilannya memang perlu berdiri sendiri.

## Rujukan

- EYD V: https://ejaan.kemendikdasmen.go.id/eyd/
- KBBI Daring: https://kbbi.kemendikdasmen.go.id/
- Skill ChatGPT dan Codex: https://learn.chatgpt.com/docs/build-skills
- Skill Claude Code: https://code.claude.com/docs/en/skills
- skills CLI: https://github.com/vercel-labs/skills

## Lisensi

Kode dan instruksi asli repositori mengikuti [LICENSE](LICENSE). Dokumen rujukan Badan Bahasa tetap diatribusikan kepada sumbernya; lisensi repositori tidak dimaksudkan untuk mengubah hak atas dokumen pihak ketiga.
