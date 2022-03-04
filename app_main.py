import streamlit as st
import numpy as np
import pandas as pd
import app_df_gene
import app_df_detect
import app_api

PAGES = {
    "Deepfake generation": app_df_gene,
    "Deepfake detection": app_df_detect,
    "API Example":app_api
}

st.title("Deepfake Tryhard")


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
