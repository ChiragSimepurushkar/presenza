import streamlit as st
import time
from src.database.db import delete_subject


@st.dialog("Confirm Deletion")
def delete_subject_dialog(subject_name, subject_id):
    st.write(f"Are you sure you want to remove **{subject_name}**?")
    st.caption("⚠️ This will permanently delete this subject, all student enrollments, and recorded attendance logs.")

    st.markdown(f"To confirm deletion, please type **`{subject_name}`** below:")
    entered_name = st.text_input(
        "Confirm Subject Name",
        placeholder=f"Type '{subject_name}' here",
        label_visibility="collapsed"
    )

    is_match = entered_name.strip() == subject_name.strip()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Cancel", width="stretch", type="secondary"):
            st.rerun()
    with col2:
        if st.button("🗑️ Confirm Delete", width="stretch", type="primary", disabled=not is_match):
            try:
                delete_subject(subject_id)
                st.success(f"'{subject_name}' removed successfully!")
                time.sleep(0.8)
                st.rerun()
            except Exception as e:
                st.error(f"Failed to remove subject: {str(e)}")
