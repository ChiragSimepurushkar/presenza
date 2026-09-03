import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():
    style_base_layout()
    style_background_home()
    header_home()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%;">
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 2.5rem;">🎓</span>
                </div>
                <h2 style="text-align: center; margin-bottom: 8px; font-family: 'Climate Crisis', cursive;">I'm a Student</h2>
                <p style="color: #64748b; font-family: 'Inter', sans-serif; font-size: 0.9rem; text-align:center; margin-bottom: 24px; padding: 0 10px;">
                    Login with your face, view attendance & enroll in courses
                </p>
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" width="120" style="margin-bottom: 24px;">
            </div>
        """, unsafe_allow_html=True)
        if st.button('🎓 Student Portal', type='primary', use_container_width=True):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%;">
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 2.5rem;">👨‍🏫</span>
                </div>
                <h2 style="text-align: center; margin-bottom: 8px; font-family: 'Climate Crisis', cursive;">I'm a Teacher</h2>
                <p style="color: #64748b; font-family: 'Inter', sans-serif; font-size: 0.9rem; text-align:center; margin-bottom: 24px; padding: 0 10px;">
                    Take AI attendance, manage subjects & track records
                </p>
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" width="145" style="margin-bottom: 24px;">
            </div>
        """, unsafe_allow_html=True)
        if st.button('👨‍🏫 Teacher Portal', type='primary', use_container_width=True):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()