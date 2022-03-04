import streamlit as st
import pandas as pd
import numpy as np
import requests

import streamlit as st

def app():

    st.title("Deepfake generation")

    uploaded_file = st.file_uploader("Gimme some model",type=["mp4","mov","mkv","wmv"])

    if uploaded_file is not None:
        st.video(uploaded_file)

    st.title("Choose a mask to apply")

    columns = st.columns(3)
    with columns[0]:
        ck_1 = st.checkbox("Tom Cruise")
    with columns[1]:
        ck_2 = st.checkbox("Tom Hanks")
    with columns[2]:
        ck_3 = st.checkbox("Tom Holland")

    if ck_1:
        response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")

        st.write(response.json()[0]['fact'])

    if ck_2:
        response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")

        st.write(response.json()[0]['fact'])

    if ck_3:
        response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")

        st.write(response.json()[0]['fact'])

    bt_generate = st.button("Generate your deepfake")

    st.text("")

    if bt_generate:
        response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")

        st.write(response.json()[0]['fact'])
