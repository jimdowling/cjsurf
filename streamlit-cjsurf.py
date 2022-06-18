import streamlit as st
import hopsworks
import datetime
import pandas as pd

# Set the environment variable when you run this program:
# HOPSWORKS_API_KEY

st.title('Lahinch Surf Prediction ')
st.subheader('CJSurf')

project = hopsworks.login()
fs = project.get_feature_store()

fg = fs.get_feature_group("wave_predictions")
df = fg.read(online=True)
df.sort_values("hits_at", inplace=True)
df.drop(["beach_id"], axis=1, inplace=True)
df['hits_at'] = pd.to_datetime(df['hits_at']) 
df['wave_height'] = pd.to_numeric(df['wave_height'] , errors='coerce')
df = df.set_index('hits_at')

st.line_chart(df)