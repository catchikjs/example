import streamlit as st

st.write("사랑해요, 정숙님")
st.write(st.secrets["api_key"])
openai_api_key = st.secrets["api_key"]
st.write(openai_api_key)
