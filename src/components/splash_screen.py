import streamlit as st
import base64
import os
from PIL import Image
import io


def _load_splash_images_base64():
    """
    Load the 10 splash PNG images from assets/, resize to 384px max
    and compress to WebP for compact base64 embedding.
    Returns a list of 10 base64 data URIs.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')
    assets_dir = os.path.abspath(assets_dir)
    data_uris = []

    for i in range(1, 11):
        img_path = os.path.join(assets_dir, f'image{i}.png')
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img.thumbnail((384, 384), Image.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format='WEBP', quality=65, method=4)
            b64 = base64.b64encode(buf.getvalue()).decode()
            data_uris.append(f"data:image/webp;base64,{b64}")
        else:
            data_uris.append("")

    return data_uris


def _load_logo_base64():
    """Load the logo_icon.jpg for the final splash reveal."""
    logo_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'logo_icon.jpg')
    logo_path = os.path.abspath(logo_path)
    if os.path.exists(logo_path):
        img = Image.open(logo_path)
        img.thumbnail((256, 256), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format='WEBP', quality=75, method=4)
        b64 = base64.b64encode(buf.getvalue()).decode()
        return f"data:image/webp;base64,{b64}"
    return ""


@st.cache_data
def _get_cached_splash_data():
    """Cache all splash assets so they're only generated once."""
    return _load_splash_images_base64(), _load_logo_base64()


def show_splash():
    """
    Renders a full-screen animated splash overlay that plays once per session.
    Features cycling PNG image carousel, logo reveal, title, tagline, and fade-out.
    """
    if st.session_state.get('splash_shown'):
        return

    st.session_state['splash_shown'] = True

    images, logo_uri = _get_cached_splash_data()

    # --- PART 1: Inject CSS only (small payload) ---
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Inter:wght@400;600&display=swap');

        .splash-overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: linear-gradient(135deg, #0f0a1e 0%, #1a1040 30%, #0d1b2a 60%, #0f0a1e 100%);
            z-index: 999999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            animation: splashFadeOut 0.8s ease-in 5.6s forwards;
            pointer-events: auto;
            overflow: hidden;
        }

        .splash-overlay::before {
            content: '';
            position: absolute;
            width: 200%; height: 200%;
            top: -50%; left: -50%;
            background:
                radial-gradient(circle 600px at 20% 30%, rgba(124, 58, 237, 0.15) 0%, transparent 70%),
                radial-gradient(circle 500px at 80% 70%, rgba(6, 182, 212, 0.12) 0%, transparent 70%),
                radial-gradient(circle 400px at 60% 20%, rgba(168, 85, 247, 0.1) 0%, transparent 70%);
            animation: splashMeshRotate 8s ease-in-out infinite;
        }

        .splash-overlay::after {
            content: '';
            position: absolute;
            width: 100%; height: 100%;
            background-image:
                radial-gradient(1.5px 1.5px at 10% 20%, rgba(124, 58, 237, 0.5) 50%, transparent 50%),
                radial-gradient(1px 1px at 30% 60%, rgba(6, 182, 212, 0.4) 50%, transparent 50%),
                radial-gradient(1.5px 1.5px at 50% 40%, rgba(168, 85, 247, 0.3) 50%, transparent 50%),
                radial-gradient(1px 1px at 70% 80%, rgba(124, 58, 237, 0.4) 50%, transparent 50%),
                radial-gradient(1.5px 1.5px at 90% 30%, rgba(6, 182, 212, 0.5) 50%, transparent 50%),
                radial-gradient(1px 1px at 20% 90%, rgba(168, 85, 247, 0.3) 50%, transparent 50%),
                radial-gradient(1.5px 1.5px at 60% 10%, rgba(124, 58, 237, 0.4) 50%, transparent 50%),
                radial-gradient(1px 1px at 80% 50%, rgba(6, 182, 212, 0.3) 50%, transparent 50%);
            animation: splashParticleDrift 6s linear infinite;
        }

        /* ===== IMAGE CAROUSEL CONTAINER ===== */
        .splash-image-cycle {
            position: relative;
            width: 250px;
            height: 250px;
            margin-bottom: 24px;
            z-index: 2;
        }

        @media (max-width: 600px) {
            .splash-image-cycle {
                width: min(220px, 55vw);
                height: min(220px, 55vw);
            }
        }

        /* ===== INDIVIDUAL CAROUSEL IMAGES ===== */
        .splash-image {
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            object-fit: contain;
            opacity: 0;
            transform: scale(0.85) translateY(4px);
            filter:
                drop-shadow(0 0 12px rgba(124, 58, 237, 0.35))
                drop-shadow(0 0 24px rgba(6, 182, 212, 0.20));
            z-index: 2;
        }

        /* Image timing: 0.25s in + 0.1s hold + 0.2s out ≈ 0.45s per image */
        .splash-image-1  { animation: splashImgIn 0.25s ease-out 0.0s  forwards, splashImgOut 0.2s ease-in 0.35s forwards; }
        .splash-image-2  { animation: splashImgIn 0.25s ease-out 0.45s forwards, splashImgOut 0.2s ease-in 0.80s forwards; }
        .splash-image-3  { animation: splashImgIn 0.25s ease-out 0.90s forwards, splashImgOut 0.2s ease-in 1.25s forwards; }
        .splash-image-4  { animation: splashImgIn 0.25s ease-out 1.35s forwards, splashImgOut 0.2s ease-in 1.70s forwards; }
        .splash-image-5  { animation: splashImgIn 0.25s ease-out 1.80s forwards, splashImgOut 0.2s ease-in 2.15s forwards; }
        .splash-image-6  { animation: splashImgIn 0.25s ease-out 2.25s forwards, splashImgOut 0.2s ease-in 2.60s forwards; }
        .splash-image-7  { animation: splashImgIn 0.25s ease-out 2.70s forwards, splashImgOut 0.2s ease-in 3.05s forwards; }
        .splash-image-8  { animation: splashImgIn 0.25s ease-out 3.15s forwards, splashImgOut 0.2s ease-in 3.50s forwards; }
        .splash-image-9  { animation: splashImgIn 0.25s ease-out 3.60s forwards, splashImgOut 0.2s ease-in 3.95s forwards; }
        .splash-image-10 { animation: splashImgIn 0.25s ease-out 4.05s forwards, splashImgOut 0.2s ease-in 4.40s forwards; }

        /* ===== LOGO REVEAL (after all images) ===== */
        .splash-logo {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%) scale(0.3);
            width: 100px;
            height: 100px;
            border-radius: 22px;
            object-fit: contain;
            opacity: 0;
            z-index: 3;
            box-shadow: 0 0 40px rgba(124, 58, 237, 0.4), 0 0 80px rgba(124, 58, 237, 0.15);
            animation: splashLogoReveal 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 4.5s forwards;
        }

        /* ===== GLOW RING ===== */
        .splash-glow-ring {
            position: absolute;
            width: 280px; height: 280px;
            border-radius: 50%;
            border: 2px solid rgba(124, 58, 237, 0.15);
            top: 50%; left: 50%;
            transform: translate(-50%, -50%) scale(0.5);
            opacity: 0;
            animation: splashRingPulse 2s ease-in-out 0.2s infinite;
            z-index: 1;
        }

        @media (max-width: 600px) {
            .splash-glow-ring {
                width: min(260px, 65vw);
                height: min(260px, 65vw);
            }
        }

        /* ===== TITLE ===== */
        .splash-title {
            font-family: 'Climate Crisis', cursive;
            font-size: 3rem;
            font-weight: 400;
            background: linear-gradient(135deg, #7c3aed 0%, #a855f7 30%, #06b6d4 70%, #7c3aed 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: splashTitleIn 0.7s ease-out 4.5s forwards, splashGradientShift 3s ease infinite;
            opacity: 0;
            transform: translateY(20px);
            z-index: 2;
            letter-spacing: -0.01em;
        }

        @media (max-width: 600px) {
            .splash-title {
                font-size: 2rem;
            }
        }

        /* ===== TAGLINE ===== */
        .splash-tagline {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: rgba(148, 163, 184, 0.9);
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-top: 8px;
            z-index: 2;
            opacity: 0;
            animation: splashTaglineIn 0.6s ease-out 4.9s forwards;
        }

        @media (max-width: 600px) {
            .splash-tagline {
                font-size: 0.7rem;
                letter-spacing: 0.12em;
            }
        }

        /* ===== KEYFRAMES ===== */
        @keyframes splashFadeOut {
            0% { opacity: 1; pointer-events: auto; }
            100% { opacity: 0; pointer-events: none; visibility: hidden; }
        }
        @keyframes splashMeshRotate {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            50% { transform: translate(-2%, 2%) rotate(3deg); }
        }
        @keyframes splashParticleDrift {
            0% { transform: translateY(0); }
            100% { transform: translateY(-30px); }
        }
        @keyframes splashImgIn {
            0% { opacity: 0; transform: scale(0.85) translateY(4px); }
            100% { opacity: 1; transform: scale(1.0) translateY(0px); }
        }
        @keyframes splashImgOut {
            0% { opacity: 1; transform: scale(1.0) translateY(0px); }
            100% { opacity: 0; transform: scale(1.05) translateY(-4px); }
        }
        @keyframes splashLogoReveal {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0.3); }
            60% { opacity: 1; transform: translate(-50%, -50%) scale(1.08); }
            100% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        }
        @keyframes splashTitleIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes splashTaglineIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        @keyframes splashRingPulse {
            0% { transform: translate(-50%, -50%) scale(0.6); opacity: 0; }
            50% { transform: translate(-50%, -50%) scale(1.2); opacity: 0.3; }
            100% { transform: translate(-50%, -50%) scale(1.5); opacity: 0; }
        }
        @keyframes splashGradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
    """, unsafe_allow_html=True)

    # --- PART 2: Inject HTML with images (separate call to avoid size limit) ---
    # Build image tags — each one is a separate small chunk
    img_tags = []
    for i, uri in enumerate(images, 1):
        img_tags.append(f'<img src="{uri}" class="splash-image splash-image-{i}" alt="" />')

    # Split images into two groups to stay well under Streamlit's HTML size limit
    half = len(img_tags) // 2
    group1 = "\n".join(img_tags[:half])
    group2 = "\n".join(img_tags[half:])

    # First 5 images + structure open
    st.markdown(f"""<div class="splash-overlay">
<div class="splash-image-cycle">
<div class="splash-glow-ring"></div>
{group1}
{group2}
<img src="{logo_uri}" class="splash-logo" alt="Presenza Logo" />
</div>
<div class="splash-title">PRESENZA</div>
<div class="splash-tagline">AI-Powered Attendance System</div>
</div>""", unsafe_allow_html=True)
