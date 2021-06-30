# Streamlit Timeline Component Example
import datetime as dt
import streamlit as st
from streamlit_timeline import timeline

_now = dt.datetime.now()
_now_str = '{"year": "'+str(_now.year)+'","month": "'+str(_now.month)+'","display_date": "now"}'


# use full page width
st.set_page_config(page_title="David Leon - Personnal Experience", layout="wide")

# load data
with open('data.json', "r", encoding="latin-1") as f:
    data = f.read()

data = data.replace('"#NOW#"',_now_str)

# render timeline
timeline(data, height=800)