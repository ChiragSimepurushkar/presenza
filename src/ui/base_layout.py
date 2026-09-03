import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background: linear-gradient(135deg, #f8f9ff 0%, #f0f2ff 40%, #e8f4ff 70%, #f8f9ff 100%) !important;
                    min-height: 100vh;
                    position: relative;
                    overflow: hidden;
                }

                /* Animated floating orbs - soft light version */
                .stApp::before {
                    content: '';
                    position: fixed;
                    top: -50%;
                    left: -50%;
                    width: 200%;
                    height: 200%;
                    background: radial-gradient(circle 400px at 20% 30%, rgba(124, 58, 237, 0.05) 0%, transparent 100%),
                                radial-gradient(circle 300px at 80% 70%, rgba(6, 182, 212, 0.04) 0%, transparent 100%),
                                radial-gradient(circle 250px at 50% 50%, rgba(139, 92, 246, 0.03) 0%, transparent 100%);
                    animation: floatOrbs 20s ease-in-out infinite;
                    pointer-events: none;
                    z-index: 0;
                }

                @keyframes floatOrbs {
                    0%, 100% { transform: translate(0, 0) rotate(0deg); }
                    25% { transform: translate(2%, -3%) rotate(5deg); }
                    50% { transform: translate(-1%, 2%) rotate(-3deg); }
                    75% { transform: translate(3%, 1%) rotate(2deg); }
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255, 255, 255, 0.85) !important;
                    backdrop-filter: blur(20px) !important;
                    -webkit-backdrop-filter: blur(20px) !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(124, 58, 237, 0.1) !important;
                    box-shadow: 0 8px 32px rgba(124, 58, 237, 0.06),
                                0 1px 3px rgba(0, 0, 0, 0.04) !important;
                    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
                }

                .stApp div[data-testid="stColumn"]:hover {
                    border-color: rgba(124, 58, 237, 0.2) !important;
                    box-shadow: 0 12px 40px rgba(124, 58, 237, 0.1),
                                0 4px 12px rgba(0, 0, 0, 0.05) !important;
                    transform: translateY(-2px);
                }
        </style>  
                """,
            unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp {
                    background: linear-gradient(180deg, #f8f9ff 0%, #f3f4f9 50%, #f8f9ff 100%) !important;
                    min-height: 100vh;
                }

                /* Subtle dot pattern overlay */
                .stApp::before {
                    content: '';
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-image: 
                        radial-gradient(rgba(124, 58, 237, 0.04) 1px, transparent 1px);
                    background-size: 40px 40px;
                    pointer-events: none;
                    z-index: 0;
                }

        </style>  
                """,
            unsafe_allow_html=True)
    



def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');

            /* Hide Streamlit top bar */
            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            /* ===== TYPOGRAPHY ===== */
            h1, .stMarkdown h1 {
                font-family: 'Climate Crisis', cursive !important;
                font-size: 2.6rem !important;
                font-weight: 400 !important;
                line-height: 1.2 !important;
                margin-bottom: 0.5rem !important;
                color: #1e293b !important;
                letter-spacing: -0.01em !important;
            }

            h2, .stMarkdown h2 {
                font-family: 'Climate Crisis', cursive !important;
                font-size: 1.5rem !important;
                font-weight: 400 !important;
                line-height: 1.3 !important;
                margin-bottom: 0.3rem !important;
                color: #334155 !important;
            }

            h3, .stMarkdown h3 {
                font-family: 'Climate Crisis', cursive !important;
                font-weight: 400 !important;
                font-size: 1.2rem !important;
                color: #1e293b !important;
            }

            h4, p, span, label, li, a, button, input, 
            .stMarkdown p, .stMarkdown span, .stButton p, .stButton span, 
            div[data-testid="stWidgetLabel"] p {
                font-family: 'Inter', sans-serif !important;
            }
            
            /* Body text color */
            p, span, label, li, .stMarkdown p {
                color: #475569;
            }

            /* Ensure text inside buttons ar always inherited from the button itself */
            .stButton p, .stButton span {
                color: inherit !important;
            }

            /* ===== INPUT FIELDS ===== */
            div[data-baseweb="input"] {
                background: rgba(255, 255, 255, 0.95) !important;
                backdrop-filter: blur(12px) !important;
                border-radius: 0.85rem !important;
                border: 1.5px solid #e2e8f0 !important;
                transition: all 0.3s ease !important;
                padding: 0.4rem 0.6rem !important;
                box-shadow: 0 2px 5px rgba(0,0,0,0.02) !important;
            }

            div[data-baseweb="input"]:focus-within {
                border-color: rgba(124, 58, 237, 0.6) !important;
                box-shadow: 0 0 0 4px rgba(124, 58, 237, 0.1),
                            0 4px 12px rgba(124, 58, 237, 0.08) !important;
                transform: translateY(-1px);
            }

            div[data-baseweb="input"] input {
                color: #1e293b !important;
                background: transparent !important;
                font-family: 'Inter', sans-serif !important;
                font-size: 1.05rem !important;
                padding: 0.4rem !important;
            }

            div[data-baseweb="input"] input::placeholder {
                color: #94a3b8 !important;
                font-size: 1rem !important;
            }

            /* Input labels */
            div[data-testid="stWidgetLabel"] p {
                color: #475569 !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 500 !important;
                font-size: 0.9rem !important;
            }

            /* Password input */
            div[data-baseweb="input"] div {
                background: transparent !important;
            }

            /* Select boxes */
            div[data-baseweb="select"] > div {
                background: rgba(255, 255, 255, 0.9) !important;
                backdrop-filter: blur(10px) !important;
                border-radius: 1rem !important;
                border: 1.5px solid #e2e8f0 !important;
                color: #1e293b !important;
            }

            div[data-baseweb="select"] > div:focus-within {
                border-color: rgba(124, 58, 237, 0.5) !important;
                box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1) !important;
            }

            /* ===== BUTTONS ===== */

            /* Primary button - purple gradient */
            button[kind="primary"] {
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
                color: white !important;
                padding: 0.65rem 1.8rem !important;
                border: none !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.9rem !important;
                letter-spacing: 0.01em !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 14px rgba(124, 58, 237, 0.25) !important;
                gap: 8px !important;
            }

            button[kind="primary"]:hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 6px 20px rgba(124, 58, 237, 0.35) !important;
            }

            /* Secondary button */
            button[kind="secondary"] {
                border-radius: 0.85rem !important;
                background: white !important;
                color: #6d28d9 !important;
                padding: 0.65rem 1.8rem !important;
                border: 1.5px solid #e2e8f0 !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.9rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
                gap: 8px !important;
            }

            button[kind="secondary"]:hover {
                border-color: #c4b5fd !important;
                background: #faf5ff !important;
                transform: translateY(-1px) !important;
                box-shadow: 0 4px 12px rgba(124, 58, 237, 0.08) !important;
            }

            /* Tertiary button */
            button[kind="tertiary"] {
                border-radius: 0.85rem !important;
                background: #f8fafc !important;
                color: #475569 !important;
                padding: 0.65rem 1.8rem !important;
                border: 1px solid #e2e8f0 !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 500 !important;
                font-size: 0.9rem !important;
                transition: all 0.3s ease !important;
                box-shadow: none !important;
                gap: 8px !important;
            }

            button[kind="tertiary"]:hover {
                background: #f1f5f9 !important;
                border-color: #cbd5e1 !important;
                color: #1e293b !important;
            }

            /* Default/unstyled buttons — catch-all */
            button:not([kind]) {
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
                color: white !important;
                padding: 0.65rem 1.8rem !important;
                border: none !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                font-size: 0.9rem !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 14px rgba(124, 58, 237, 0.25) !important;
                gap: 8px !important;
            }

            button:not([kind]):hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 6px 20px rgba(124, 58, 237, 0.35) !important;
            }

            /* ===== MATERIAL ICON FIX ===== */
            /* Ensure Material Symbols font renders properly inside buttons */
            button span[data-testid="stIconMaterial"] {
                font-family: 'Material Symbols Rounded' !important;
                font-size: 1.2rem !important;
                vertical-align: middle !important;
                -webkit-font-feature-settings: 'liga' !important;
                font-feature-settings: 'liga' !important;
            }

            /* ===== DIVIDERS ===== */
            hr {
                border-color: #e2e8f0 !important;
                margin: 1.5rem 0 !important;
            }

            /* ===== CONTAINERS / BORDERS ===== */
            div[data-testid="stVerticalBlock"] > div[data-testid="stExpander"],
            .stAlert {
                background: rgba(255, 255, 255, 0.8) !important;
                backdrop-filter: blur(10px) !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 1rem !important;
            }

            /* Bordered containers */
            div[data-testid="stVerticalBlockBorderWrapper"] {
                background: rgba(255, 255, 255, 0.7) !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 1.5rem !important;
                backdrop-filter: blur(10px) !important;
            }

            /* ===== DATA FRAMES ===== */
            .stDataFrame {
                border-radius: 1rem !important;
                overflow: hidden !important;
            }

            /* ===== TOAST / ALERTS ===== */
            div[data-testid="stToast"] {
                background: rgba(255, 255, 255, 0.95) !important;
                backdrop-filter: blur(20px) !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 1rem !important;
                color: #1e293b !important;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08) !important;
            }

            /* Success alert */
            div[data-testid="stAlert"][data-baseweb*="positive"],
            .element-container .stSuccess {
                background: rgba(34, 197, 94, 0.08) !important;
                border: 1px solid rgba(34, 197, 94, 0.25) !important;
            }

            /* Warning alert */
            div[data-testid="stAlert"][data-baseweb*="warning"],
            .element-container .stWarning {
                background: rgba(234, 179, 8, 0.08) !important;
                border: 1px solid rgba(234, 179, 8, 0.25) !important;
            }

            /* Error alert */
            div[data-testid="stAlert"][data-baseweb*="negative"],
            .element-container .stError {
                background: rgba(239, 68, 68, 0.08) !important;
                border: 1px solid rgba(239, 68, 68, 0.25) !important;
            }

            /* Info alert */
            div[data-testid="stAlert"][data-baseweb*="info"],
            .element-container .stInfo {
                background: rgba(6, 182, 212, 0.08) !important;
                border: 1px solid rgba(6, 182, 212, 0.25) !important;
            }

            /* ===== DIALOGS ===== */
            div[data-testid="stModal"] > div {
                background: rgba(255, 255, 255, 0.98) !important;
                backdrop-filter: blur(30px) !important;
                border: 1px solid #e2e8f0 !important;
                border-radius: 1.5rem !important;
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.1),
                            0 4px 16px rgba(0, 0, 0, 0.05) !important;
            }

            /* ===== CAMERA INPUT ===== */
            div[data-testid="stCameraInput"] > div {
                border-radius: 1rem !important;
                border: 2px dashed rgba(124, 58, 237, 0.25) !important;
                background: rgba(248, 249, 255, 0.5) !important;
            }

            /* ===== FILE UPLOADER ===== */
            div[data-testid="stFileUploader"] > div {
                background: rgba(248, 249, 255, 0.5) !important;
                border: 2px dashed rgba(124, 58, 237, 0.25) !important;
                border-radius: 1rem !important;
            }

            /* ===== SPINNER ===== */
            .stSpinner > div {
                border-top-color: #7c3aed !important;
            }

            /* ===== SCROLLBAR ===== */
            ::-webkit-scrollbar {
                width: 6px;
            }
            ::-webkit-scrollbar-track {
                background: rgba(241, 245, 249, 0.5);
            }
            ::-webkit-scrollbar-thumb {
                background: rgba(124, 58, 237, 0.2);
                border-radius: 3px;
            }
            ::-webkit-scrollbar-thumb:hover {
                background: rgba(124, 58, 237, 0.4);
            }

            /* ===== ANIMATIONS ===== */
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            @keyframes pulseGlow {
                0%, 100% { filter: drop-shadow(0 0 12px rgba(124, 58, 237, 0.15)); }
                50% { filter: drop-shadow(0 0 24px rgba(124, 58, 237, 0.3)); }
            }

            .block-container > div {
                animation: fadeInUp 0.6s ease-out;
            }

        </style>
    """, unsafe_allow_html=True)