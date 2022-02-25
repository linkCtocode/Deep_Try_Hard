import streamlit as st

def app():
    
    st.title("Streamlit Lecture")
    
    uploaded_file = st.file_uploader("Gimme some image",type=["jpg","jpeg","png","gif"])

    if uploaded_file is not None:
        st.image(uploaded_file)
