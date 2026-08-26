import streamlit as st

def main():
    st.header("This is Title")
    name = st.text_input("Enter name:")

    col1, col2 = st.columns(2,gap="small")

    with col1:
        if st.button("Hi: ",type='primary', key="btn1"):
            print("Hi",name)

    with col2:
        if st.button("Bye: ",type='secondary', key="btn2"):
                    print("Bye",name)

    st.markdown("""
    <style>
    button{
      background:green !important,
    }
    </style>
            <div>

            </div>
    """,unsafe_allow_html=True)
main()