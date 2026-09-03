import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
<div style="
    background: rgba(255, 255, 255, 0.9); 
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-left: 4px solid;
    border-image: linear-gradient(180deg, #7c3aed, #06b6d4) 1;
    padding: 24px 28px; 
    border-radius: 0 1.2rem 1.2rem 0; 
    border-top: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
    margin-bottom: 16px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
">
    <div style="
        position: absolute;
        top: 0;
        right: 0;
        width: 120px;
        height: 120px;
        background: radial-gradient(circle, rgba(124, 58, 237, 0.04) 0%, transparent 70%);
        pointer-events: none;
    "></div>
    <h3 style="margin:0; color:#1e293b; font-size:1.2rem; font-family: 'Climate Crisis', cursive; font-weight: 400;">{name}</h3>
    <p style="color:#64748b; margin:10px 0; font-family: 'Inter', sans-serif; font-size: 0.9rem;">
        Code: <span style="
            background: rgba(124, 58, 237, 0.1); 
            color: #6d28d9; 
            padding: 3px 10px; 
            border-radius: 6px;
            font-weight: 500;
            font-size: 0.85rem;
        ">{code}</span> 
        <span style="color: #cbd5e1; margin: 0 6px;">|</span> 
        Section: <span style="color: #475569; font-weight: 500;">{section}</span>
    </p>
"""

    if stats:
        html += """
<div style="display:flex; gap:10px; flex-wrap:wrap; margin-top: 12px;">
"""

        for icon, label, value in stats:
            html += f"""<div style="
                background: rgba(124, 58, 237, 0.06); 
                border: 1px solid rgba(124, 58, 237, 0.1);
                padding: 6px 14px; 
                border-radius: 10px; 
                font-size: 0.85rem;
                font-family: 'Inter', sans-serif;
                color: #475569;
            ">{icon} <b style="color: #6d28d9;">{value}</b> {label}</div>"""

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()