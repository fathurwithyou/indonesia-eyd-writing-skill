# Peta rujukan

## Pisahkan kewenangan sumber

| Kebutuhan | Rujukan | Batas |
| --- | --- | --- |
| Ejaan, kapitalisasi, penulisan kata, tanda baca, serapan | EYD V; `references/eyd/eyd-edisi-v-2022.md` dan berkas per topik | Tidak menetapkan struktur riset, mutu argumen, atau seluruh persoalan tata bahasa. |
| Bentuk baku dan arti kata | KBBI Daring, https://kbbi.kemendikdasmen.go.id/ | Tidak ada salinan KBBI dalam paket; jangan mengaku sudah memeriksanya tanpa akses. |
| Penjelasan kalimat dan pilihan kata | `references/seri-penyuluhan/` | Bahan pendamping; periksa konteks dan edisi bila berbenturan dengan EYD V. |
| Ikhtisar cepat | `references/highlights/` | Ringkasan tidak menggantikan naskah resmi. |
| Struktur bab, gaya sitasi, tata letak | Pedoman jurnal, penerbit, organisasi, atau proyek yang diberikan pengguna | Jangan mengatasnamakan EYD untuk aturan lokal. |
| Alur, suara, keterbacaan, pilihan genre | Profil dan prinsip editorial dalam skill | Saran editorial, bukan ketentuan Badan Bahasa. |
| Kebenaran klaim riset atau fakta produk | Dokumen sumber, data, artikel ilmiah, spesifikasi yang relevan | Pedoman bahasa tidak membuktikan klaim faktual. |

## Cara membaca korpus lokal

Gunakan pencarian teks atau daftar judul bagian untuk menemukan potongan yang tepat. Contoh jika alat shell tersedia:

```bash
rg -n '^###|^####|keterangan tambahan|anak kalimat' references/eyd/eyd-edisi-v-2022.md
```

Baca bagian yang ditemukan beserta konteks sebelum menerapkan aturan. Berkas granular dapat memuat contoh yang lebih sedikit daripada naskah utama; ketiadaan contoh tidak membuktikan larangan. `references/eyd/eyd-v.md` adalah salinan alternatif yang dipertahankan untuk kompatibilitas; gunakan `eyd-edisi-v-2022.md` sebagai titik acuan.

Jika salinan lokal tidak cukup jelas atau pengguna meminta aturan terkini, periksa portal resmi https://ejaan.kemendikdasmen.go.id/eyd/ jika akses tersedia. Sebutkan sumber yang benar-benar dipakai; jangan menyatakan verifikasi daring berdasarkan salinan lokal.

Untuk catatan koreksi, pisahkan label **kaidah ejaan**, **pilihan editorial**, dan **hal yang perlu verifikasi** bila pembedaan itu relevan. Sertakan bagian kaidah atau URL yang mendukung; jangan mengarang nomor aturan atau entri kamus.
