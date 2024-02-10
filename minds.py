import pandas as pd
import streamlit as st
import mindsdb_sdk

LOGIN = 'mindsdb@klopmp.com'
#PASSWORD = st.secrets["password"]
PASSWORD = "c*.Jp6!7xb9"


# option 1
server = mindsdb_sdk.connect(login="david.fraser+jan24@mindsdb.com", password="c*.Jp6!7xb9")

# option 2
#server = mindsdb_sdk.connect('https://cloud.mindsdb.com', login=LOGIN, password=PASSWORD)
