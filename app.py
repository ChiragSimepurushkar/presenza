import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main():
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
main()