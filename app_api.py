import requests
import streamlit as st


def app():
    st.title("Dogs Fact")

    bt = st.button("Get Me a fact")

    if bt:
        response = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")

        st.write(response.json()[0]['fact'])
