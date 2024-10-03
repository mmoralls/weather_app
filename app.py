from api_v3 import extract_data
from email_with_msg import send_mail
import streamlit as st

st.write('This app uses an api connected to weather.gov and extracts local weather data in my city.')   
st.write ('Check email for response.')
    
with st.container():

    col1 = st.columns([6])

extract_data()

send_mail()
