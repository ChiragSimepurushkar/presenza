import streamlit as st


def footer_home():

    st.markdown(f"""
        <div style="
            margin-top: 3rem; 
            padding-top: 1.5rem;
            border-top: 1px solid #e2e8f0;
            display: flex; 
            gap: 6px; 
            justify-content: center; 
            align-items: center;
        ">
            <p style="
                font-weight: 400; 
                color: #94a3b8;
                font-family: 'Inter', sans-serif;
                font-size: 0.85rem;
                letter-spacing: 0.03em;
            ">Created with ❤️ by</p>  
            <p style="
                font-weight: 600;
                background: linear-gradient(135deg, #7c3aed, #06b6d4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-family: 'Inter', sans-serif;
                font-size: 0.85rem;
            ">Chirag Nikant Simepurushkar</p>
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    
    st.markdown(f"""
        <div style="
            margin-top: 3rem; 
            padding-top: 1.5rem;
            border-top: 1px solid #e2e8f0;
            display: flex; 
            gap: 6px; 
            justify-content: center; 
            align-items: center;
        ">
            <p style="
                font-weight: 400; 
                color: #94a3b8;
                font-family: 'Inter', sans-serif;
                font-size: 0.85rem;
                letter-spacing: 0.03em;
            ">Created with ❤️ by</p>  
            <p style="
                font-weight: 600;
                background: linear-gradient(135deg, #7c3aed, #06b6d4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-family: 'Inter', sans-serif;
                font-size: 0.85rem;
            ">Chirag Nikant Simepurushkar</p>
        </div>
                
                """, unsafe_allow_html=True)