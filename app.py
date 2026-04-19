import time
import streamlit as st
from logic import debug_error

st.set_page_config(page_title="CS Debug Assistant", page_icon="🧠")

st.title("🧠 CS Debug Assistant")

st.markdown("### Debug your Python errors instantly")

user_input = st.text_input("Enter your error message:")

if user_input:
    with st.spinner("Analyzing error..."):
        time.sleep(1)
        result = debug_error(user_input)
    
    st.success("### Explanation")
    st.write(result["explanation"])
    
    st.info("### Suggested Fix")
    st.write(result["fix"])