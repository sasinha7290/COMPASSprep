# COMPASS Prep™ landing page

A desktop-first, responsive Streamlit landing page for **COMPASS Prep™ — data preparation for COMPASS**.

- **GEO-2-COMPASS:** live web application for public NCBI GEO studies at <https://geo2compass.precsn.com/>.
- **RAW-2-COMPASS:** downloadable standalone macOS application. The landing page links directly to the [v.05 GitHub Release asset](https://github.com/poojabio/RAW-2-COMPASS/releases/tag/v.05).
- **RAW-2-COMPASS user guide:** nine-page PDF available from the RAW-2-COMPASS card at `/app/static/RAW-2-COMPASS-User-Guide_DRAFT1.pdf`.

The page describes both routes in detail and uses the COMPASS icon in its header.

## Files

- `app.py` — the one-page Streamlit application
- `static/RAW-2-COMPASS-User-Guide_DRAFT1.pdf` — downloadable user guide for the macOS app
- `assets/compass-prep-background-4k.webp` — optimized 4K website background
- `assets/compass-prep-background-4k.png` — full-quality 4K background
- `assets/compass-logo.png` — COMPASS icon used in the header
- `.streamlit/config.toml` — Streamlit theme and static-file serving
- `railway.json`, `Procfile`, `runtime.txt`, `requirements.txt` — Railway deployment files

The v.05 release asset is `RAW-2-COMPASS-macos.zip` (145.5 MiB; publisher-provided SHA-256: `16b5cde5fc5b3aacee0a745953a4625cc019007d5696ca0cfd70c4deb11810c5`). The PDF guide still shows the earlier ZIP filename, so the page directs readers to use the v.05 link.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the printed local URL. The RAW download button links to the v.05 release asset; the PDF guide is served from `/app/static/RAW-2-COMPASS-User-Guide_DRAFT1.pdf`.

## Deploy on Railway

The ZIP is over GitHub's 100 MiB single-file limit, so the app links to the publisher's v.05 GitHub Release asset instead of storing the ZIP in this repository. Railway deploys this page from GitHub; the PDF guide is included in `static/`.

The app requires no API keys or database. Railway supplies `$PORT`; `railway.json` and `Procfile` bind Streamlit to it.

## Content notes

GEO-2-COMPASS capabilities are described from its project README. The RAW ZIP contains a packaged desktop app; the separate PDF guide explains installation, FASTQ input selection, pipeline operation, and output locations.

The background was generated specifically for this project using the built-in image-generation workflow, then upscaled to 3840×2160. See `assets/BACKGROUND_PROMPT.md` for the prompt.
