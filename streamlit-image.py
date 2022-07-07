import streamlit as st
import hopsworks


st.title("Lahinch Surf Forecast")
st.subheader('CJSurf')

project = hopsworks.login()

dataset_api = project.get_dataset_api()
downloaded_file_path = dataset_api.download("Resources/latest_lahinch.png", overwrite=True)

st.image(downloaded_file_path, caption='Lahinch Surf Forecast')
