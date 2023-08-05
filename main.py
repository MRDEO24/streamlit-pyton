import streamlit as st

st.title("Ini Aplikasi pertamaku")
st.header("Ini adalah aku")

nama = st.text_input("Masukkan nama Anda:")
if not nama :
    st.stop()
st.markdown(f'Selamat <b>datang</b> {nama}',unsafe_allow_html=True)