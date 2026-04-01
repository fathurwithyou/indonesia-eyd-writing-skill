# Indonesia EYD Writing Skill

Repositori ini dibuat untuk membantu penulisan bahasa Indonesia agar lebih sesuai dengan **EYD V** dan kaidah resmi.

Skill ini dapat digunakan untuk:
- menulis teks bahasa Indonesia yang lebih baku,
- menyunting dan melakukan proofreading,
- memperbaiki ejaan, tanda baca, dan penulisan kata,
- menjelaskan aturan penulisan secara singkat dan terarah.

Isi utama repositori:
- `SKILL.md` sebagai panduan penggunaan skill,
- `references/` sebagai kumpulan referensi kaidah bahasa Indonesia.

Cakupan materi meliputi:
- penggunaan huruf,
- penulisan kata,
- tanda baca,
- unsur serapan.

Repositori ini ditujukan untuk membantu agent, developer, penulis, editor, maupun pengguna umum yang ingin menulis bahasa Indonesia dengan lebih rapi, konsisten, dan sesuai pedoman resmi.

## Cara Memuat Skill

### 1. ChatGPT / Claude

#### ChatGPT

ChatGPT mendukung **Skills** sebagai workflow yang dapat digunakan ulang dan dibagikan. Skill dapat berisi instruksi, contoh, dan bahkan kode, lalu digunakan secara otomatis ketika relevan. Dokumentasi resmi juga menyebut bahwa skill dapat diunggah dari komputer melalui halaman Skills.

Langkah yang disarankan:

1. Buka menu profil di ChatGPT.
2. Masuk ke halaman **Skills**.
3. Klik **New skill**.
4. Pilih **Upload from your computer**.
5. Unggah skill ini dari komputer Anda. ([OpenAI Help Center][1])

Agar struktur skill rapi saat diunggah, siapkan arsip ZIP yang memuat:

* `SKILL.md`
* folder `references/`

Struktur ZIP yang disarankan:

```text
indonesia-eyd-writing-skill.zip
├── SKILL.md
└── references/
    ├── ...
```

Catatan:

* `SKILL.md` sebaiknya berada pada level utama di dalam ZIP.
* Folder `references/` sebaiknya ikut disertakan agar seluruh referensi kaidah tersedia saat skill digunakan.
* Dokumentasi resmi juga menyebut bahwa skill saat ini tersedia dalam beta pada ChatGPT **Business**, **Enterprise**, **Edu**, **Teachers**, dan **Healthcare**.

#### Claude

Untuk Claude versi web, skill ini dapat ditambahkan melalui halaman kustomisasi skill.

Langkah yang disarankan:

1. Buka [`https://claude.ai/customize/skills`.](https://claude.ai/customize/skills)
2. Klik tombol **+**.
3. Unggah skill ini dalam bentuk **berkas ZIP**.
4. Pastikan isi ZIP mencakup:

   * `SKILL.md`
   * folder `references/`

Struktur ZIP yang disarankan:

```text
indonesia-eyd-writing-skill.zip
├── SKILL.md
└── references/
    ├── ...
```

Catatan:

* Pastikan `SKILL.md` berada pada level utama di dalam ZIP.
* Folder `references/` sebaiknya ikut dimasukkan agar seluruh referensi kaidah dapat digunakan bersama skill.

---

### 2. Codex

Codex mendukung skill secara native. Untuk memuat skill ini, simpan repositori atau isi skill ke dalam direktori `.agents/skills/` pada proyek Anda.

Struktur yang disarankan:

```text
your-project/
├── .agents/
│   └── skills/
│       └── indonesia-eyd-writing/
│           ├── SKILL.md
│           └── references/
│               ├── ...
```

Catatan penting:

* `SKILL.md` adalah berkas utama yang wajib ada.
* Folder `references/` dapat diletakkan dalam direktori skill yang sama.
* Nama folder skill dapat disesuaikan, tetapi sebaiknya ringkas dan deskriptif, misalnya `indonesia-eyd-writing`.

Praktik yang disarankan:

* simpan semua referensi pendukung di dalam folder skill yang sama,
* tulis rujukan ke berkas referensi dari `SKILL.md` bila diperlukan,
* gunakan struktur yang konsisten agar mudah dipindahkan ke proyek lain.

---

### 3. Claude Code

Claude Code juga mendukung skill secara native melalui `SKILL.md`. Skill dapat dipasang sebagai **personal skill** atau **project skill**.

#### Opsi A — Personal Skill

Simpan skill pada direktori berikut:

```text
~/.claude/skills/indonesia-eyd-writing/
├── SKILL.md
└── references/
    ├── ...
```

Skill pada lokasi ini akan tersedia untuk semua proyek Anda.

#### Opsi B — Project Skill

Simpan skill pada direktori berikut:

```text
your-project/
└── .claude/
    └── skills/
        └── indonesia-eyd-writing/
            ├── SKILL.md
            └── references/
                ├── ...
```

Skill pada lokasi ini hanya berlaku untuk proyek tersebut.

Catatan:

* `SKILL.md` adalah titik masuk utama skill.
* Folder `references/` dapat disimpan dalam direktori yang sama.
* Bila skill ini ingin dibagikan ke anggota tim, direktori `.claude/skills/` dapat ikut dimasukkan ke version control.
* Struktur yang rapi akan memudahkan Claude Code memuat referensi tambahan dari skill ini.

## Rekomendasi Penggunaan

Agar skill ini bekerja dengan baik di berbagai platform, ikuti prinsip berikut:

* jadikan `SKILL.md` sebagai sumber instruksi utama,
* simpan referensi tambahan dalam folder `references/`,
* gunakan nama folder skill yang jelas dan konsisten,
* pastikan struktur file tidak berubah saat diarsipkan atau dipindahkan,
* rujuk referensi yang relevan dari dalam `SKILL.md` bila diperlukan.

## Ringkasan

* **ChatGPT**: unggah skill melalui halaman **Skills** dengan opsi **Upload from your computer**.
* **Claude**: unggah skill dalam bentuk ZIP yang berisi `SKILL.md` dan `references/`.
* **Codex**: simpan skill di `.agents/skills/<nama-skill>/`.
* **Claude Code**: simpan skill di `~/.claude/skills/` atau `.claude/skills/` dalam proyek.

## License

MIT