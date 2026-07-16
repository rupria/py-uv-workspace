import streamlit as st


with st.form('form'):
    chk1 = st.checkbox('낚시')
    chk2 = st.checkbox('골프')
    chk3 = st.checkbox('영화')
    submit = st.form_submit_button('확인')
    if submit:
        if chk1:
            st.write('낚시선택')
        if chk2:
            st.write('골프선택')
        if chk3:
            st.write("영화선택")
