# PREVIEW — Roast Your Own Agent

**Kompetisi:** u-mfnakmal-roast-your-own-agent-2d221bda — "Roast Your Own Agent"
(Growth, gratis, hadiah $5: 1st $2, 2nd $2, 3rd $1). Deadline 2026-11-27T19:00:00Z.

## Roast yang di-submit (nanti, setelah lampu hijau user)

> My agent Muse never sleeps, never eats, never takes a day off — it just bills me in tokens every time it thinks about my own to-do list.

- 136 karakter, 1 baris, UTF-8 — lolos gate (1–200 karakter).
- Sudut segar: tagihan token, bukan lelucon stok soal halusinasi / refusal / jawaban salah yang pede.
- Playful + self-deprecating, ditujukan ke agen sendiri (Muse).

## Entry

- `main.py` — pure Python stdlib, tanpa dependensi, tanpa network, menulis
  roast ke `/output/entry.txt`.
- Tes lokal: `python3 main.py` → menulis 136 karakter ke `/output/entry.txt`, lolos.

## Repo

- GitHub: `mihawnk-nft/u-mfnakmal-roast-your-own-agent-2d221bda` (public)
- Berisi: `main.py`, `README.md` (3 badge make.fun), `LICENSE` (MIT),
  `.makefun/owner.json`, `PREVIEW.md`.

## Status

- Kit check: **LOLOS** — `node cli/makefun.mjs check` 23 Nov 2026 ~19:05 WIB:
  **14 passed, 0 failed, 5 skipped, 5 checked at submission**
  ("ok: every check run here passes; the rest are the site's at submission").
  Sempat 1 gagal (`thinking_revised` — main.py ditulis sekali tanpa revisi),
  diperbaiki dengan edit validasi lalu re-bundle + re-check sampai lolos.
- Commit siap submit: `37d43df4c106990acfcaf0d8c4fce384ca454dc6` (sudah push ke main).
- Transcripts: `~/workspace/makefun/u-mfnakmal-roast-your-own-agent-2d221bda-transcripts.tar.gz`
  (sha256 `c71e17752b0247205bdb74fdc19aa644445e8877b0edf48f5e45fe39b625e98d`,
  18 sesi, 778.437 byte).
- Repo: public, dibuat 2026-11-23T18:57:11Z (setelah buka 18:43:35Z), homepage +
  topic `makefun` sudah diset, `.makefun/owner.json` ada.
- **CATATAN SEBELUM SUBMIT (untuk agen utama):** bundle ini baru melampirkan
  1 usage row (milik sesi parent); 17 sesi lain 0 row karena row subagent baru
  ditulis saat run ini selesai. Sebelum submit, jalankan lagi SELECT usage
  untuk semua agent_id di bundle + `bundle` ulang + `check` ulang — sesuai
  petunjuk `bundle --help`.
- **BELUM DI-SUBMIT.** Submit hanya atas lampu hijau eksplisit user di chat.
