
import streamlit as st

st.set_page_config(page_title="DevFest Hyderabad", page_icon="🚀")

st.title("🚀 Hello, DevFest Hyderabad!")
st.write("My first live app for Google DevFest Hyderabad 2026.")

if st.button("Say hello"):
    st.success("Hello from my live demo! 🎉")

st.caption("Built with Python and Streamlit.")
