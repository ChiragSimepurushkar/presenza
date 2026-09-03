import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
    page_title="PRESENZA — AI-Powered Face & Voice Attendance",
    page_icon="assets/logo_icon.jpg"
      )
#at start :- session_state is empty disctionary {}
    if 'login_type' not in st.session_state:   # check if it doesn't exist or else will give issue
          st.session_state['login_type'] = None  #initialize it

    match st.session_state['login_type']:
          case 'teacher':
                teacher_screen() #render teacher screen

          case 'student':
                student_screen()

          case None:
                home_screen()   ## By default -when seesion_state is None

    join_code = st.query_params.get('join-code')

    if join_code:
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

main()