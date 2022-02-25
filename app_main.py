import streamlit as st
import numpy as np
import pandas as pd
import app_df
import app_image
import app_api

PAGES = {
    "DataFrame Example": app_df,
    "Image Example": app_image,
    "API Example":app_api
}

st.title("Streamlit Lecture")


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
