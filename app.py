
import streamlit as st
import pandas as pd

header = ['학번','이름','전공']
if "students" not in st.session_state:
    st.session_state.students = [
        ["202601", "홍길동", "컴퓨터공학"],
        ["202602", "이순신", "데이터사이언스"],
        ["202603", "유관순", "인공지능학"],
    ]

st.title("통계")

num = st.text_input('학번을 입력하세요.')
name = st.text_input('이름을 입력하세요.')
jungong = st.text_input('전공을 입력하세요.')

if st.button("등록"):
    if num and name and jungong:
        st.session_state.students.append([num, name, jungong])
        st.success(f"{name} 학생이 등록되었습니다.")

df = pd.DataFrame(st.session_state.students, columns=header)
st.table(df)
