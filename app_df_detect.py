import streamlit as st

def app():

    st.title("Deepfake detection")

    uploaded_file = st.file_uploader("Gimme some video",type=["mp4","mov","mkv","wmv"])

    if uploaded_file is not None:
        st.video(uploaded_file)
