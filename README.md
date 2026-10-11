# COMPASS Prep™ landing page

A desktop-first, responsive Streamlit landing page for **COMPASS Prep™ — data preparation for COMPASS**.

- **GEO-2-COMPASS:** live web application for public NCBI GEO studies at <https://geo2compass.precsn.com/>.
- **RAW-2-COMPASS:** downloadable standalone application for macOS on Apple silicon. The landing page links to the GitHub Release asset; a local copy of the ZIP is served directly when present.
- **RAW-2-COMPASS user guide:** nine-page PDF available from the RAW-2-COMPASS card at `/app/static/RAW-2-COMPASS-User-Guide_DRAFT1.pdf`.

The page describes both routes in detail and uses the COMPASS icon in its header.

## Files

- `app.py` — the one-page Streamlit application
- `static/RAW2Compass-macos-arm64.zip` — supplied desktop app archive, 144.5 MiB
- `static/RAW-2-COMPASS-User-Guide_DRAFT1.pdf` — downloadable user guide for the macOS app
- `assets/compass-prep-background-4k.webp` — optimized 4K website background
- `assets/compass-prep-background-4k.png` — full-quality 4K background
- `assets/compass-logo.png` — COMPASS icon used in the header
- `.streamlit/config.toml` — Streamlit theme and static-file serving
- `railway.json`, `Procfile`, `runtime.txt`, `requirements.txt` — Railway deployment files

The ZIP contains `RAW2Compass.app`, a macOS arm64 executable. It does not include Windows or Intel Mac versions. The archive was validated with `unzip -t`; SHA-256: `8ec32dcfd052d07a30cf4676e71c9e68bf7dd02ff70cca6a7c04ae7`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the printed local URL. If the ZIP is present in `static/`, the RAW download link is served at `/app/static/RAW2Compass-macos-arm64.zip`. Otherwise, the page links to the GitHub Release asset.

## Deploy on Railway

The ZIP is over GitHub's 100 MiB single-file limit, so a normal GitHub repository push cannot carry this exact archive. To deploy the page **with the download bundled**, use Railway's local-directory deployment:

1. Keep `static/RAW2Compass-macos-arm64.zip` in this folder.
2. From this folder, run `railway link` to select the intended Railway project and service.
3. Run `railway up` to upload the local directory and deploy it.
4. Confirm the page and the RAW ZIP link on the Railway domain.

For GitHub-based automatic deployments, the page uses the `RAW2Compass-macos-arm64.zip` asset from the `raw2compass-macos-arm64-2026-10-08` GitHub Release. The ZIP is excluded from Git history. Set Railway's optional `RAW2COMPASS_DOWNLOAD_URL` environment variable to a different public HTTPS asset URL if you need to replace the default.

The app requires no API keys or database. Railway supplies `$PORT`; `railway.json` and `Procfile` bind Streamlit to it.

## Content notes

GEO-2-COMPASS capabilities are described from its project README. The RAW ZIP contains a packaged desktop app; the separate PDF guide explains installation, FASTQ input selection, pipeline operation, and output locations.

The background was generated specifically for this project using the built-in image-generation workflow, then upscaled to 3840×2160. See `assets/BACKGROUND_PROMPT.md` for the prompt.
