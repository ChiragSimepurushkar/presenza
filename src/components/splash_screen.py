import streamlit as st
import base64
import os


def _get_logo_base64():
    """Load the local logo and return a base64 data URI."""
    logo_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'logo_icon.jpg')
    logo_path = os.path.abspath(logo_path)
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/jpeg;base64,{data}"
    return ""


def show_splash():
    """
    Renders a full-screen animated splash overlay that plays once per session.
    Features cycling icons, logo reveal, tagline typewriter, and fade-out.
    """
    if st.session_state.get('splash_shown'):
        return

    st.session_state['splash_shown'] = True

    logo_url = _get_logo_base64()

    st.markdown(f"""
    <style>
        /* ===== SPLASH SCREEN ===== */
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
            animation: splashFadeOut 0.8s ease-in 3.8s forwards;
            pointer-events: auto;
            overflow: hidden;
        }}

        /* Animated background mesh */
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

        /* Floating particles */
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

        /* Icon cycling container */
        .splash-icon-cycle {{
            position: relative;
            width: 100px; height: 100px;
            margin-bottom: 30px;
            z-index: 2;
        }}

        .splash-icon {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            opacity: 0;
            transform: scale(0.5) rotate(-15deg);
            filter: drop-shadow(0 0 20px rgba(124, 58, 237, 0.4));
        }}

        .splash-icon:nth-child(1) {{
            animation: splashIconIn 0.6s ease-out 0.1s forwards, splashIconOut 0.4s ease-in 0.6s forwards;
        }}
        .splash-icon:nth-child(2) {{
            animation: splashIconIn 0.6s ease-out 0.7s forwards, splashIconOut 0.4s ease-in 1.2s forwards;
        }}
        .splash-icon:nth-child(3) {{
            animation: splashIconIn 0.6s ease-out 1.3s forwards, splashIconOut 0.4s ease-in 1.8s forwards;
        }}
        .splash-icon:nth-child(4) {{
            animation: splashIconIn 0.6s ease-out 1.9s forwards, splashIconOut 0.4s ease-in 2.4s forwards;
        }}

        /* Logo reveal */
        .splash-logo {{
            width: 90px;
            height: 90px;
            border-radius: 22px;
            opacity: 0;
            transform: scale(0.3);
            z-index: 2;
            box-shadow: 0 0 40px rgba(124, 58, 237, 0.4), 0 0 80px rgba(124, 58, 237, 0.15);
            animation: splashLogoReveal 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 2.5s forwards;
            margin-bottom: 16px;
        }}

        /* Title */
        .splash-title {{
            font-family: 'Climate Crisis', cursive;
            font-size: 2.8rem;
            font-weight: 400;
            background: linear-gradient(135deg, #7c3aed 0%, #a855f7 30%, #06b6d4 70%, #7c3aed 100%);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: splashTitleIn 0.7s ease-out 2.8s forwards, gradientShift 3s ease infinite;
            opacity: 0;
            transform: translateY(20px);
            z-index: 2;
            letter-spacing: -0.01em;
        }}

        /* Tagline with typewriter */
        .splash-tagline {{
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: rgba(148, 163, 184, 0.9);
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-top: 6px;
            z-index: 2;
            opacity: 0;
            animation: splashTaglineIn 0.6s ease-out 3.2s forwards;
            overflow: hidden;
            white-space: nowrap;
            border-right: 2px solid rgba(124, 58, 237, 0.6);
        }}

        /* Glow ring behind icons */
        .splash-glow-ring {{
            position: absolute;
            width: 160px; height: 160px;
            border-radius: 50%;
            border: 2px solid rgba(124, 58, 237, 0.15);
            top: 50%; left: 50%;
            transform: translate(-50%, -50%) scale(0.5);
            opacity: 0;
            animation: splashRingPulse 2s ease-in-out 0.2s infinite;
            z-index: 1;
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

        @keyframes splashIconIn {{
            0% {{ opacity: 0; transform: scale(0.5) rotate(-15deg); }}
            100% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
        }}

        @keyframes splashIconOut {{
            0% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
            100% {{ opacity: 0; transform: scale(1.3) rotate(10deg); }}
        }}

        @keyframes splashLogoReveal {{
            0% {{ opacity: 0; transform: scale(0.3); }}
            60% {{ opacity: 1; transform: scale(1.08); }}
            100% {{ opacity: 1; transform: scale(1); }}
        }}

        @keyframes splashTitleIn {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes splashTaglineIn {{
            0% {{ opacity: 0; width: 0; }}
            100% {{ opacity: 1; width: auto; }}
        }}

        @keyframes splashRingPulse {{
            0% {{ transform: translate(-50%, -50%) scale(0.6); opacity: 0; }}
            50% {{ transform: translate(-50%, -50%) scale(1.2); opacity: 0.3; }}
            100% {{ transform: translate(-50%, -50%) scale(1.5); opacity: 0; }}
        }}

        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
    </style>

    <div class="splash-overlay">
        <!-- Cycling icons -->
        <div class="splash-icon-cycle">
            <div class="splash-glow-ring"></div>
            <div class="splash-icon">🎓</div>
            <div class="splash-icon">👨‍🏫</div>
            <div class="splash-icon">📸</div>
            <div class="splash-icon">🧠</div>
        </div>

        <!-- Logo reveal -->
        <img src="{logo_url}" class="splash-logo" alt="Presenza Logo" />

        <!-- Title -->
        <div class="splash-title">PRESENZA</div>

        <!-- Tagline -->
        <div class="splash-tagline">AI-Powered Attendance System</div>
    </div>
    """, unsafe_allow_html=True)
