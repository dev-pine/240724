import streamlit as st
st.title('나의 첫 웹서비스')
name = st.text_input("이름을 입력하세요: ")
menu = st.selectbox("좋아하는 음식 선택하세요!",[빙수,치킨,징거버거])
if st.button('인사말 생성'):
  sf.write(f"안녕하세요 {name}님이 좋아하는 음식은 {menu}이군요.")
