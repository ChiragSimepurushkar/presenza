import streamlit as st
import base64
import os
from PIL import Image
import io


def _load_splash_images_base64():
    """
    Load the 10 splash PNG images from assets/, resize to 512px max
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
            # Resize to max 512px while preserving aspect ratio and alpha
            img.thumbnail((512, 512), Image.LANCZOS)
            buf = io.BytesIO()
            # Save as WebP with transparency for much smaller size
            img.save(buf, format='WEBP', quality=80, method=4)
            b64 = base64.b64encode(buf.getvalue()).decode()
            data_uris.append(f"data:image/webp;base64,{b64}")
        else:
            data_uris.append("")

    return data_uris


@st.cache_data
def _get_cached_splash_images():
    """Cache the base64 images so they're only generated once."""
    return _load_splash_images_base64()


def show_splash():
    """
    Renders a full-screen animated splash overlay that plays once per session.
    Features cycling PNG image carousel, title reveal, tagline, and fade-out.
    """
    if st.session_state.get('splash_shown'):
        return

    st.session_state['splash_shown'] = True

    images = _get_cached_splash_images()

    # Build the 10 <img> tags
    img_tags = ""
    for i, uri in enumerate(images, 1):
        img_tags += f'        <img src="{uri}" class="splash-image splash-image-{i}" alt="Splash {i}" />\n'

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Inter:wght@400;600&display=swap');

        .splash-overlay {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: linear-gradient(135deg, #0f0a1e 0%, #1a1040 30%, #0d1b2a 60%, #0f0a1e 100%);
            z-index: 999999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            animation: splashFadeOut 0.8s ease-in 4.8s forwards;
            pointer-events: auto;
            overflow: hidden;
        }}

        .splash-overlay::before {{
            content: '';
            position: absolute;
            width: 200%; height: 200%;
            top: -50%; left: -50%;
            background:
                radial-gradient(circle 600px at 20% 30%, rgba(124, 58, 237, 0.15) 0%, transparent 70%),
                radial-gradient(circle 500px at 80% 70%, rgba(6, 182, 212, 0.12) 0%, transparent 70%),
                radial-gradient(circle 400px at 60% 20%, rgba(168, 85, 247, 0.1) 0%, transparent 70%);
            animation: splashMeshRotate 8s ease-in-out infinite;
        }}

        .splash-overlay::after {{
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
        }}

        /* ===== IMAGE CAROUSEL CONTAINER ===== */
        .splash-image-cycle {{
            position: relative;
            width: 250px;
            height: 250px;
            margin-bottom: 24px;
            z-index: 2;
        }}

        @media (max-width: 600px) {{
            .splash-image-cycle {{
                width: min(250px, 60vw);
                height: min(250px, 60vw);
            }}
        }}

        /* ===== INDIVIDUAL IMAGES ===== */
        .splash-image {{
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
        }}

        /* Each image: fade in over 0.25s, hold ~0.1s, fade out over 0.2s = ~0.45s per image */
        .splash-image-1  {{ animation: splashImgIn 0.25s ease-out 0.0s  forwards, splashImgOut 0.2s ease-in 0.35s forwards; }}
        .splash-image-2  {{ animation: splashImgIn 0.25s ease-out 0.45s forwards, splashImgOut 0.2s ease-in 0.80s forwards; }}
        .splash-image-3  {{ animation: splashImgIn 0.25s ease-out 0.90s forwards, splashImgOut 0.2s ease-in 1.25s forwards; }}
        .splash-image-4  {{ animation: splashImgIn 0.25s ease-out 1.35s forwards, splashImgOut 0.2s ease-in 1.70s forwards; }}
        .splash-image-5  {{ animation: splashImgIn 0.25s ease-out 1.80s forwards, splashImgOut 0.2s ease-in 2.15s forwards; }}
        .splash-image-6  {{ animation: splashImgIn 0.25s ease-out 2.25s forwards, splashImgOut 0.2s ease-in 2.60s forwards; }}
        .splash-image-7  {{ animation: splashImgIn 0.25s ease-out 2.70s forwards, splashImgOut 0.2s ease-in 3.05s forwards; }}
        .splash-image-8  {{ animation: splashImgIn 0.25s ease-out 3.15s forwards, splashImgOut 0.2s ease-in 3.50s forwards; }}
        .splash-image-9  {{ animation: splashImgIn 0.25s ease-out 3.60s forwards, splashImgOut 0.2s ease-in 3.95s forwards; }}
        .splash-image-10 {{ animation: splashImgIn 0.25s ease-out 4.05s forwards, splashImgOut 0.2s ease-in 4.40s forwards; }}

        /* ===== GLOW RING — behind images ===== */
        .splash-glow-ring {{
            position: absolute;
            width: 280px; height: 280px;
            border-radius: 50%;
            border: 2px solid rgba(124, 58, 237, 0.15);
            top: 50%; left: 50%;
            transform: translate(-50%, -50%) scale(0.5);
            opacity: 0;
            animation: splashRingPulse 2s ease-in-out 0.2s infinite;
            z-index: 1;
        }}

        @media (max-width: 600px) {{
            .splash-glow-ring {{
                width: min(280px, 70vw);
                height: min(280px, 70vw);
            }}
        }}

        /* ===== TITLE ===== */
        .splash-title {{
            font-family: 'Climate Crisis', cursive;
            font-size: 3rem;
            font-weight: 400;
            background: linear-gradient(135deg, #7c3aed 0%, #a855f7 30%, #06b6d4 70%, #7c3aed 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: splashTitleIn 0.7s ease-out 3.2s forwards, splashGradientShift 3s ease infinite;
            opacity: 0;
            transform: translateY(20px);
            z-index: 2;
            letter-spacing: -0.01em;
        }}

        @media (max-width: 600px) {{
            .splash-title {{
                font-size: 2rem;
            }}
        }}

        /* ===== TAGLINE ===== */
        .splash-tagline {{
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: rgba(148, 163, 184, 0.9);
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-top: 8px;
            z-index: 2;
            opacity: 0;
            animation: splashTaglineIn 0.6s ease-out 3.7s forwards;
        }}

        @media (max-width: 600px) {{
            .splash-tagline {{
                font-size: 0.7rem;
                letter-spacing: 0.12em;
            }}
        }}

        /* ===== KEYFRAMES ===== */
        @keyframes splashFadeOut {{
            0% {{ opacity: 1; pointer-events: auto; }}
            100% {{ opacity: 0; pointer-events: none; visibility: hidden; }}
        }}
        @keyframes splashMeshRotate {{
            0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
            50% {{ transform: translate(-2%, 2%) rotate(3deg); }}
        }}
        @keyframes splashParticleDrift {{
            0% {{ transform: translateY(0); }}
            100% {{ transform: translateY(-30px); }}
        }}

        /* Image fade in: scale 0.85 → 1.0, opacity 0 → 1, subtle float up */
        @keyframes splashImgIn {{
            0% {{
                opacity: 0;
                transform: scale(0.85) translateY(4px);
            }}
            100% {{
                opacity: 1;
                transform: scale(1.0) translateY(0px);
            }}
        }}

        /* Image fade out: scale 1.0 → 1.05, opacity 1 → 0 */
        @keyframes splashImgOut {{
            0% {{
                opacity: 1;
                transform: scale(1.0) translateY(0px);
            }}
            100% {{
                opacity: 0;
                transform: scale(1.05) translateY(-4px);
            }}
        }}

        @keyframes splashTitleIn {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes splashTaglineIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes splashRingPulse {{
            0% {{ transform: translate(-50%, -50%) scale(0.6); opacity: 0; }}
            50% {{ transform: translate(-50%, -50%) scale(1.2); opacity: 0.3; }}
            100% {{ transform: translate(-50%, -50%) scale(1.5); opacity: 0; }}
        }}
        @keyframes splashGradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
    </style>

    <div class="splash-overlay">
        <div class="splash-image-cycle">
            <div class="splash-glow-ring"></div>
{img_tags}
        </div>
        <div class="splash-title">PRESENZA</div>
        <div class="splash-tagline">AI-Powered Attendance System</div>
    </div>
    """, unsafe_allow_html=True)
