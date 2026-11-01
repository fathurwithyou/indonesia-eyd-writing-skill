# Skill Menulis Bahasa Indonesia

Skill ini membantu agen membuat dan menyunting tulisan yang jelas, alami, dan sesuai konteks. EYD V menjadi dasar ejaan; gaya tulisan mengikuti pembaca, tujuan, dan suara penulis.

## Isi repo

- `SKILL.md`: panduan utama.
- `references/profiles/`: panduan untuk lima jenis tulisan.
- `references/editorial/`: prinsip penyuntingan dan peta sumber.
- `references/eyd/`: EYD V dan rujukan per topik.
- `evals/`: kasus uji dan contoh hasil.
- `skills/indonesia-eyd-writing-skill/`: salinan paket plugin.

Pendekatan penyuntingan juga mengambil prinsip dari [no-ai-slop](https://github.com/petergyang/no-ai-slop). Profil riset merujuk pada [research-proposal](https://github.com/luwill/research-skills/tree/main/research-proposal).

## Memasang

### Skills CLI

```bash
npx skills add fathurwithyou/indonesia-eyd-writing-skill --skill indonesia-eyd-writing-skill
```

### Plugin Claude Code

```text
/plugin marketplace add fathurwithyou/indonesia-eyd-writing-skill
/plugin install indonesia-eyd-writing-skill@indonesia-eyd
```

### Pasang manual

Salin `SKILL.md`, `references/`, dan `agents/` ke salah satu folder berikut:

| Aplikasi | Dalam proyek | Untuk semua proyek |
| --- | --- | --- |
| Codex | `.agents/skills/indonesia-eyd-writing-skill/` | `~/.agents/skills/indonesia-eyd-writing-skill/` |
| Claude Code | `.claude/skills/indonesia-eyd-writing-skill/` | `~/.claude/skills/indonesia-eyd-writing-skill/` |

Untuk host yang menerima unggahan skill, buat ZIP berisi berkas dan folder yang sama.

## Evaluasi

`evals/cases.json` berisi prompt dan kriteria pemeriksaan. [Contoh evaluasi](evals/profile-examples.md) memperlihatkan masukan dan keluaran untuk kelima profil.

## Pemeliharaan

Ubah sumber di repo utama, lalu sinkronkan salinan plugin dan periksa strukturnya:

```bash
python3 scripts/sync_distribution.py
python3 scripts/check_skill.py
```

Pemeriksaan memakai Python 3.10+ dan PyYAML. CI menjalankan pemeriksaan saat ada push atau pull request.

## Rujukan

- [EYD V](https://ejaan.kemendikdasmen.go.id/eyd/)
- [KBBI Daring](https://kbbi.kemendikdasmen.go.id/)
- [Research Proposal Skill](https://github.com/luwill/research-skills/tree/main/research-proposal)

## Lisensi

MIT untuk instruksi asli repo. Dokumen Badan Bahasa tetap mengikuti hak dan lisensinya sendiri.
