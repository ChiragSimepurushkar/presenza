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
    # Fallback to the dark-bg logo if icon not found
    logo_path2 = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'logo.png')
    logo_path2 = os.path.abspath(logo_path2)
    if os.path.exists(logo_path2):
        with open(logo_path2, 'rb') as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{data}"
    return ""


def header_home():

    logo_url = _get_logo_base64()
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px; animation: fadeInUp 0.8s ease-out;">
            <img src='{logo_url}' style='height:110px; border-radius: 20px; animation: pulseGlow 3s ease-in-out infinite;' />
            <h1 style='
                text-align:center; 
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 30%, #06b6d4 70%, #7c3aed 100%);
                background-size: 300% 300%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: gradientShift 4s ease infinite;
                font-family: "Climate Crisis", cursive !important;
                font-size: 3rem !important;
                font-weight: 400;
                letter-spacing: -0.01em;
                margin-top: 12px;
                text-shadow: none;
            '>PRESENZA</h1>
            <p style='
                text-align:center; 
                color: #64748b; 
                font-family: Inter, sans-serif;
                font-size: 1rem;
                font-weight: 400;
                letter-spacing: 0.15em;
                text-transform: uppercase;
                margin-top: -4px;
            '>AI-Powered Attendance System</p>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = _get_logo_base64()
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-start; gap:14px;">
            <img src='{logo_url}' style='height:50px; border-radius: 12px; box-shadow: 0 2px 12px rgba(124, 58, 237, 0.15);' />
            <div>
                <h2 style='
                    text-align:left; 
                    background: linear-gradient(135deg, #7c3aed, #06b6d4);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                    font-family: "Climate Crisis", cursive !important;
                    font-size: 1.3rem !important;
                    font-weight: 400;
                    margin: 0;
                    line-height: 1.2;
                    letter-spacing: 0em;
                '>PRESENZA</h2>
            </div>
        </div>   
                
                """, unsafe_allow_html=True)