# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="David Leon - Personnal Experience", layout="wide")

# load data
with open('data.json', "r", encoding="latin-1") as f:
    data = f.read()

# render timeline
timeline(data, height=800)