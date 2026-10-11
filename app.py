"""COMPASS Prep landing page.

Run locally with:
    streamlit run app.py
"""

from __future__ import annotations

import base64
import os
from html import escape
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
BACKGROUND_PATH = APP_DIR / "assets" / "compass-prep-background-4k.webp"
COMPASS_LOGO_PATH = APP_DIR / "assets" / "compass-logo.png"
RAW_ARCHIVE_NAME = "RAW2Compass-macos-arm64.zip"
RAW_ARCHIVE_PATH = APP_DIR / "static" / RAW_ARCHIVE_NAME
RAW_ARCHIVE_URL = f"/app/static/{RAW_ARCHIVE_NAME}"
RAW_GUIDE_NAME = "RAW-2-COMPASS-User-Guide_DRAFT1.pdf"
RAW_GUIDE_URL = f"/app/static/{RAW_GUIDE_NAME}"
RELEASE_RAW_URL = (
    "https://github.com/sasinha7290/COMPASSprep/releases/download/"
    "raw2compass-macos-arm64-2026-10-08/RAW2Compass-macos-arm64.zip"
)
EXTERNAL_RAW_URL = os.getenv("RAW2COMPASS_DOWNLOAD_URL", "").strip()


def asset_data_uri(path: Path, mime_type: str) -> str:
    """Return a local image as an embeddable data URI."""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


st.set_page_config(
    page_title="COMPASS Prep | Coding-free preprocessing",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

background_uri = asset_data_uri(BACKGROUND_PATH, "image/webp")
compass_logo_uri = asset_data_uri(COMPASS_LOGO_PATH, "image/png")
if EXTERNAL_RAW_URL and not EXTERNAL_RAW_URL.startswith("https://"):
    st.error("RAW2COMPASS_DOWNLOAD_URL must be an HTTPS URL.")
    st.stop()
raw_download_source = EXTERNAL_RAW_URL or (
    RAW_ARCHIVE_URL if RAW_ARCHIVE_PATH.is_file() else RELEASE_RAW_URL
)
raw_download_url = escape(raw_download_source, quote=True)
raw_download_attributes = (
    'target="_blank" rel="noopener noreferrer"'
    if raw_download_source.startswith("https://")
    else f'download="{RAW_ARCHIVE_NAME}"'
)
raw_archive_size_mib = (
    RAW_ARCHIVE_PATH.stat().st_size / (1024 * 1024)
    if RAW_ARCHIVE_PATH.is_file()
    else 144.5
)

st.html(
    f"""
    <style>
        :root {{
            --navy: #08264a;
            --blue: #1677c8;
            --teal: #159f9a;
            --gold: #d89a2b;
            --ink: #10243d;
            --muted: #5f7185;
            --line: rgba(10, 73, 123, 0.14);
            --ice: #f4fbfc;
            --white: #ffffff;
        }}

        * {{ box-sizing: border-box; }}

        html {{ scroll-behavior: smooth; }}

        body {{
            margin: 0;
            background: #f7fbfc;
            color: var(--ink);
        }}

        body, button, a {{
            font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;
        }}

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        footer {{
            display: none !important;
        }}

        [data-testid="stAppViewContainer"] {{
            background: #f7fbfc;
        }}

        [data-testid="stMain"] {{
            padding: 0;
        }}

        .block-container {{
            max-width: none;
            padding: 0 !important;
        }}

        .compass-page {{
            min-height: 100vh;
            overflow: hidden;
            background: linear-gradient(180deg, #ffffff 0%, #f5fbfc 62%, #ffffff 100%);
        }}

        .site-nav {{
            position: absolute;
            z-index: 10;
            top: 0;
            left: 50%;
            width: min(1180px, calc(100% - 64px));
            height: 84px;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(8, 38, 74, 0.09);
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--navy);
            font-size: 17px;
            font-weight: 760;
            letter-spacing: -0.02em;
            text-decoration: none;
        }}

        .brand-logo {{
            display: block;
            width: 48px;
            height: 48px;
            object-fit: contain;
            flex: 0 0 auto;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 30px;
        }}

        .nav-links a {{
            color: #38516a;
            font-size: 14px;
            font-weight: 630;
            text-decoration: none;
            transition: color .2s ease;
        }}

        .nav-links a:hover {{ color: var(--blue); }}

        .hero {{
            position: relative;
            min-height: 680px;
            padding: 146px max(32px, calc((100vw - 1180px) / 2)) 76px;
            background-image:
                linear-gradient(90deg,
                    rgba(255,255,255,.98) 0%,
                    rgba(255,255,255,.94) 37%,
                    rgba(255,255,255,.53) 66%,
                    rgba(255,255,255,.08) 100%),
                url("{background_uri}");
            background-size: cover;
            background-position: center center;
            border-bottom: 1px solid var(--line);
        }}

        .hero::after {{
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: 120px;
            background: linear-gradient(180deg, rgba(247,251,252,0), #f7fbfc);
            pointer-events: none;
        }}

        .hero-copy {{
            position: relative;
            z-index: 2;
            width: min(650px, 58vw);
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 9px;
            margin: 0 0 22px;
            color: var(--blue);
            font-size: 12px;
            font-weight: 800;
            letter-spacing: .16em;
            text-transform: uppercase;
        }}

        .eyebrow::before {{
            content: "";
            width: 24px;
            height: 2px;
            background: linear-gradient(90deg, var(--teal), var(--gold));
        }}

        .hero h1 {{
            margin: 0;
            color: var(--navy);
            font-size: clamp(52px, 5.6vw, 84px);
            line-height: .98;
            letter-spacing: -0.058em;
        }}

        .hero h1 sup {{
            position: relative;
            top: -1.8em;
            margin-left: 4px;
            color: var(--blue);
            font-size: 15px;
            letter-spacing: 0;
        }}

        .hero-tagline {{
            margin: 25px 0 0;
            color: #24445f;
            font-size: clamp(20px, 2vw, 27px);
            font-weight: 540;
            line-height: 1.35;
            letter-spacing: -0.025em;
        }}

        .hero-body {{
            max-width: 600px;
            margin: 18px 0 0;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.72;
        }}

        .hero-actions {{
            display: flex;
            align-items: center;
            gap: 22px;
            margin-top: 32px;
        }}

        .primary-link {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 50px;
            padding: 0 24px;
            border-radius: 9px;
            background: linear-gradient(135deg, var(--blue), #0d5fa6);
            box-shadow: 0 12px 28px rgba(22, 119, 200, .23);
            color: white !important;
            font-size: 14px;
            font-weight: 740;
            text-decoration: none;
            transition: transform .2s ease, box-shadow .2s ease;
        }}

        .primary-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 16px 34px rgba(22, 119, 200, .3);
        }}

        .primary-link span {{
            margin-left: 10px;
            font-size: 19px;
            line-height: 1;
        }}

        .quiet-link {{
            color: #3f607d !important;
            font-size: 14px;
            font-weight: 670;
            text-decoration: none;
            border-bottom: 1px solid rgba(63, 96, 125, .34);
        }}

        .trust-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px 22px;
            margin-top: 36px;
            color: #516b83;
            font-size: 12px;
            font-weight: 650;
        }}

        .trust-row span::before {{
            content: "✓";
            margin-right: 7px;
            color: var(--teal);
            font-weight: 900;
        }}

        .section {{
            width: min(1180px, calc(100% - 64px));
            margin: 0 auto;
            padding: 84px 0;
        }}

        .section-kicker {{
            margin: 0 0 10px;
            color: var(--teal);
            font-size: 12px;
            font-weight: 800;
            letter-spacing: .15em;
            text-transform: uppercase;
        }}

        .section-title {{
            max-width: 720px;
            margin: 0;
            color: var(--navy);
            font-size: clamp(31px, 3vw, 44px);
            line-height: 1.12;
            letter-spacing: -.04em;
        }}

        .section-lede {{
            max-width: 660px;
            margin: 16px 0 0;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.65;
        }}

        .path-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 24px;
            margin-top: 40px;
        }}

        .path-card {{
            position: relative;
            min-height: 355px;
            padding: 34px;
            overflow: hidden;
            border: 1px solid var(--line);
            border-radius: 20px;
            background: rgba(255,255,255,.92);
            box-shadow: 0 20px 60px rgba(13, 66, 105, .08);
        }}

        .path-card.live {{
            background:
                radial-gradient(circle at 93% 8%, rgba(32,167,160,.16), transparent 32%),
                white;
        }}

        .path-card.raw {{
            background:
                radial-gradient(circle at 94% 8%, rgba(216,154,43,.14), transparent 31%),
                linear-gradient(135deg, #ffffff, #fbfcfc);
        }}

        .card-status {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 28px;
            padding: 7px 11px;
            border-radius: 100px;
            color: #107d78;
            background: #e8f8f6;
            font-size: 11px;
            font-weight: 820;
            letter-spacing: .08em;
            text-transform: uppercase;
        }}

        .card-status::before {{
            content: "";
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--teal);
            box-shadow: 0 0 0 4px rgba(21,159,154,.12);
        }}

        .card-status.download {{
            color: #8b621a;
            background: #fcf4e5;
        }}

        .card-status.download::before {{
            background: var(--gold);
            box-shadow: 0 0 0 4px rgba(216,154,43,.12);
        }}

        .path-card h3 {{
            margin: 0;
            color: var(--navy);
            font-size: 28px;
            line-height: 1.2;
            letter-spacing: -.035em;
        }}

        .path-label {{
            margin: 7px 0 0;
            color: var(--blue);
            font-size: 12px;
            font-weight: 800;
            letter-spacing: .11em;
            text-transform: uppercase;
        }}

        .path-card p {{
            margin: 18px 0 22px;
            color: var(--muted);
            font-size: 15px;
            line-height: 1.62;
        }}

        .mini-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 26px;
        }}

        .mini-list span {{
            padding: 7px 10px;
            border: 1px solid rgba(13, 95, 166, .12);
            border-radius: 7px;
            color: #49637b;
            background: #f8fbfd;
            font-size: 11px;
            font-weight: 650;
        }}

        .card-action {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 46px;
            padding: 0 18px;
            border: 0;
            border-radius: 8px;
            color: white !important;
            background: var(--navy);
            font-size: 13px;
            font-weight: 750;
            text-decoration: none;
            transition: background .2s ease, transform .2s ease;
        }}

        .card-action:hover {{
            transform: translateY(-1px);
            background: var(--blue);
        }}

        .download-note {{
            display: block;
            margin-top: 12px;
            color: var(--muted);
            font-size: 12px;
            line-height: 1.5;
        }}

        .guide-link {{
            display: inline-block;
            margin-top: 14px;
            color: #0d649c;
            font-size: 13px;
            font-weight: 750;
            text-decoration: underline;
            text-underline-offset: 3px;
        }}

        .path-details {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 24px;
            margin-top: 28px;
        }}

        .detail-card {{
            padding: 28px 30px;
            border: 1px solid var(--line);
            border-radius: 16px;
            background: #f9fcfd;
        }}

        .detail-card h3 {{
            margin: 0 0 13px;
            color: var(--navy);
            font-size: 19px;
        }}

        .detail-card p, .detail-card li {{
            color: #4e6578;
            font-size: 14px;
            line-height: 1.65;
        }}

        .detail-card p {{ margin: 0 0 13px; }}
        .detail-card ol, .detail-card ul {{ margin: 0; padding-left: 20px; }}
        .detail-card li + li {{ margin-top: 7px; }}
        .detail-card li::marker {{ color: var(--teal); font-weight: 700; }}

        .workflow-wrap {{
            padding: 78px max(32px, calc((100vw - 1180px) / 2));
            background: var(--navy);
            color: white;
        }}

        .workflow-top {{
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 40px;
        }}

        .workflow-top h2 {{
            max-width: 600px;
            margin: 0;
            font-size: clamp(30px, 3vw, 43px);
            line-height: 1.13;
            letter-spacing: -.04em;
        }}

        .workflow-top p {{
            max-width: 420px;
            margin: 0;
            color: #b9cedd;
            font-size: 15px;
            line-height: 1.6;
        }}

        .workflow {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0;
            margin-top: 46px;
            border: 1px solid rgba(255,255,255,.14);
            border-radius: 16px;
            overflow: hidden;
        }}

        .step {{
            position: relative;
            min-height: 180px;
            padding: 28px;
            border-right: 1px solid rgba(255,255,255,.14);
            background: rgba(255,255,255,.035);
        }}

        .step:last-child {{ border-right: 0; }}

        .step-number {{
            color: #5bcac4;
            font-size: 12px;
            font-weight: 850;
            letter-spacing: .1em;
        }}

        .step h3 {{
            margin: 18px 0 8px;
            color: white;
            font-size: 19px;
        }}

        .step p {{
            margin: 0;
            color: #aac1d2;
            font-size: 14px;
            line-height: 1.55;
        }}

        .principles {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-top: 44px;
        }}

        .principle {{
            padding-top: 20px;
            border-top: 2px solid #dcebef;
        }}

        .principle strong {{
            display: block;
            color: var(--navy);
            font-size: 16px;
        }}

        .principle span {{
            display: block;
            margin-top: 8px;
            color: var(--muted);
            font-size: 13px;
            line-height: 1.5;
        }}

        .site-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            width: min(1180px, calc(100% - 64px));
            margin: 0 auto;
            padding: 28px 0 34px;
            border-top: 1px solid var(--line);
            color: #718294;
            font-size: 12px;
        }}

        .footer-brand {{
            color: var(--navy);
            font-weight: 760;
        }}

        .footer-links {{
            display: flex;
            gap: 22px;
        }}

        .footer-links a {{
            color: #566f87;
            text-decoration: none;
        }}

        .footer-links a:hover {{ color: var(--blue); }}

        @media (max-width: 900px) {{
            .site-nav {{ width: calc(100% - 40px); }}
            .nav-links a:not(:last-child) {{ display: none; }}
            .hero {{
                min-height: 660px;
                padding: 132px 24px 62px;
                background-position: 62% center;
            }}
            .hero-copy {{ width: min(610px, 88vw); }}
            .path-grid {{ grid-template-columns: 1fr; }}
            .path-details {{ grid-template-columns: 1fr; }}
            .workflow-top {{ align-items: start; flex-direction: column; }}
            .principles {{ grid-template-columns: repeat(2, 1fr); }}
        }}

        @media (max-width: 620px) {{
            .site-nav {{ height: 70px; width: calc(100% - 32px); }}
            .nav-links {{ display: none; }}
            .brand {{ font-size: 15px; }}
            .brand-logo {{ width: 42px; height: 42px; }}
            .hero {{
                min-height: 700px;
                padding: 116px 20px 58px;
                background-image:
                    linear-gradient(180deg, rgba(255,255,255,.98) 0%, rgba(255,255,255,.92) 55%, rgba(255,255,255,.75) 100%),
                    url("{background_uri}");
            }}
            .hero-copy {{ width: 100%; }}
            .hero h1 {{ font-size: 50px; }}
            .hero h1 sup {{ top: -1.5em; }}
            .hero-actions {{ align-items: flex-start; flex-direction: column; gap: 16px; }}
            .section {{ width: calc(100% - 40px); padding: 62px 0; }}
            .path-card {{ padding: 27px; }}
            .detail-card {{ padding: 24px; }}
            .workflow-wrap {{ padding: 62px 20px; }}
            .workflow {{ grid-template-columns: 1fr; }}
            .step {{ min-height: auto; border-right: 0; border-bottom: 1px solid rgba(255,255,255,.14); }}
            .step:last-child {{ border-bottom: 0; }}
            .principles {{ grid-template-columns: 1fr; }}
            .site-footer {{ align-items: flex-start; flex-direction: column; width: calc(100% - 40px); }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            html {{ scroll-behavior: auto; }}
            * {{ transition: none !important; }}
        }}
    </style>

    <main class="compass-page" id="top">
        <nav class="site-nav" aria-label="Primary navigation">
            <a class="brand" href="#top" aria-label="COMPASS Prep home">
                <img class="brand-logo" src="{compass_logo_uri}" alt="" aria-hidden="true">
                <span>COMPASS Prep</span>
            </a>
            <div class="nav-links">
                <a href="#pathways">Pathways</a>
                <a href="#workflow">How it works</a>
                <a href="https://geo2compass.precsn.com/" target="_blank" rel="noopener noreferrer">Launch GEO-2-COMPASS ↗</a>
            </div>
        </nav>

        <header class="hero">
            <div class="hero-copy">
                <p class="eyebrow">Data preparation for COMPASS</p>
                <h1>COMPASS Prep<sup>™</sup></h1>
                <p class="hero-tagline">Coding-free preprocessing for deterministic biology.</p>
                <p class="hero-body">
                    Prepare public GEO expression studies with the web app, or download RAW-2-COMPASS to work with your own data locally. Choose the route that matches your starting data.
                </p>
                <div class="hero-actions">
                    <a class="primary-link" href="https://geo2compass.precsn.com/" target="_blank" rel="noopener noreferrer">
                        Start with public data <span aria-hidden="true">→</span>
                    </a>
                    <a class="quiet-link" href="#pathways">Explore both pathways</a>
                </div>
                <div class="trust-row" aria-label="Platform benefits">
                    <span>Coding-free</span>
                    <span>COMPASS-ready export</span>
                    <span>Reproducible workflow</span>
                </div>
            </div>
        </header>

        <section class="section" id="pathways">
            <p class="section-kicker">Choose your starting point</p>
            <h2 class="section-title">One preparation layer. Two routes into COMPASS.</h2>
            <p class="section-lede">
                GEO-2-COMPASS is a web workflow for public datasets. RAW-2-COMPASS is a downloadable desktop application for custom data; the current package is for macOS on Apple silicon.
            </p>

            <div class="path-grid">
                <article class="path-card live">
                    <div class="card-status">Available now</div>
                    <h3>GEO-2-COMPASS</h3>
                    <div class="path-label">Public datasets · Web application</div>
                    <p>
                        Enter a public GEO Series accession to retrieve study and sample details. GEO-2-COMPASS builds an expression matrix, lets you inspect it, and exports a file for COMPASS analysis.
                    </p>
                    <div class="mini-list" aria-label="GEO-2-COMPASS capabilities">
                        <span>RNA-seq &amp; microarray studies</span>
                        <span>Platform selection</span>
                        <span>Compressed matrix export</span>
                    </div>
                    <a class="card-action" href="https://geo2compass.precsn.com/" target="_blank" rel="noopener noreferrer">
                        Launch GEO-2-COMPASS&nbsp; ↗
                    </a>
                </article>

                <article class="path-card raw" id="raw-download">
                    <div class="card-status download">Download available</div>
                    <h3>RAW-2-COMPASS</h3>
                    <div class="path-label">Your data · Standalone desktop app</div>
                    <p>
                        Work with your own data in a local desktop application designed to prepare inputs for COMPASS. Download the Apple silicon macOS build as a ZIP archive containing RAW2Compass.app.
                    </p>
                    <div class="mini-list" aria-label="RAW-2-COMPASS download details">
                        <span>macOS Apple silicon</span>
                        <span>Local desktop workflow</span>
                        <span>{raw_archive_size_mib:.1f} MiB ZIP</span>
                    </div>
                    <a class="card-action" href="{raw_download_url}" {raw_download_attributes} type="application/zip">Download RAW-2-COMPASS ↓</a>
                    <small class="download-note">The ZIP contains a macOS arm64 app. Windows and Intel Mac builds are not included.</small>
                    <a class="guide-link" href="{RAW_GUIDE_URL}" target="_blank" rel="noopener noreferrer" type="application/pdf">Read the RAW-2-COMPASS user guide (PDF) ↗</a>
                </article>
            </div>

            <div class="path-details" aria-label="Detailed pathway descriptions">
                <article class="detail-card">
                    <h3>What GEO-2-COMPASS does</h3>
                    <p>GEO-2-COMPASS turns a public NCBI GEO study into an expression matrix that you can bring into COMPASS. Enter a GSE accession to see the study and sample details, then choose a GPL platform if the study includes more than one.</p>
                    <ol>
                        <li>Retrieve GEO study and sample metadata and identify available RNA-seq or microarray expression data.</li>
                        <li>Build an expression matrix from available count or supplementary files. Map probe or gene identifiers to symbols when usable annotations are available.</li>
                        <li>Optionally annotate sample columns, apply log, CPM, or log-CPM transformations, and prepare survival metadata where the source record supports it.</li>
                        <li>Preview the result and download the complete matrix as a compressed tab-separated file for use with COMPASS.</li>
                    </ol>
                    <p>Some GEO records have unusual files or exceed hosted processing limits; the web app reports when it cannot build a usable matrix.</p>
                </article>
                <article class="detail-card">
                    <h3>What RAW-2-COMPASS provides</h3>
                    <p>Use this route for your own datasets rather than a public GEO accession. It is a separate desktop application, so the landing page does not upload or process your files.</p>
                    <ol>
                        <li>Download the {raw_archive_size_mib:.1f} MiB ZIP on a Mac with Apple silicon and extract <strong>RAW2Compass.app</strong>.</li>
                        <li>Open the local application and follow its on-screen workflow to prepare your data for COMPASS.</li>
                        <li>Save the prepared output locally, then use the compatible data in your COMPASS analysis.</li>
                    </ol>
                    <p>This package contains only the macOS arm64 build. The PDF user guide explains app setup, FASTQ selection, pipeline steps, and where to find the output files.</p>
                </article>
            </div>
        </section>

        <section class="workflow-wrap" id="workflow">
            <div class="workflow-top">
                <h2>From dataset to a COMPASS-ready input.</h2>
                <p>COMPASS Prep makes the transformation explicit, traceable, and approachable—without requiring a custom preprocessing script.</p>
            </div>
            <div class="workflow">
                <article class="step">
                    <div class="step-number">01 · SELECT</div>
                    <h3>Choose your data source</h3>
                    <p>Enter a public GEO accession in the web app, or download the standalone RAW-2-COMPASS application for your own data.</p>
                </article>
                <article class="step">
                    <div class="step-number">02 · PREPARE</div>
                    <h3>Prepare the expression matrix</h3>
                    <p>Review the available expression data, sample context, and preparation options before export.</p>
                </article>
                <article class="step">
                    <div class="step-number">03 · CONTINUE</div>
                    <h3>Move into COMPASS</h3>
                    <p>Export a clean expression matrix and supporting metadata ready for deterministic biological analysis.</p>
                </article>
            </div>
        </section>

        <section class="section" aria-labelledby="principles-title">
            <p class="section-kicker">Built for scientific clarity</p>
            <h2 class="section-title" id="principles-title">A dependable front door to the COMPASS ecosystem.</h2>
            <div class="principles">
                <div class="principle">
                    <strong>COMPASS-ready</strong>
                    <span>Prepared files for the next stage of analysis.</span>
                </div>
                <div class="principle">
                    <strong>Deterministic</strong>
                    <span>Defined transformations designed for repeatable analysis.</span>
                </div>
                <div class="principle">
                    <strong>Reproducible</strong>
                    <span>A clear path from source dataset to prepared input.</span>
                </div>
                <div class="principle">
                    <strong>Coding-free</strong>
                    <span>Accessible workflows without scripting prerequisites.</span>
                </div>
            </div>
        </section>

        <footer class="site-footer">
            <div><span class="footer-brand">COMPASS Prep™</span> · Data preparation for COMPASS</div>
            <div class="footer-links">
                <a href="#top">Back to top</a>
                <a href="https://geo2compass.precsn.com/" target="_blank" rel="noopener noreferrer">GEO-2-COMPASS ↗</a>
            </div>
        </footer>
    </main>
    """
)
