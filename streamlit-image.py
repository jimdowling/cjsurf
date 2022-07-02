import streamlit as st
import hopsworks
#from PIL import Image


st.title("Lahinch Surf Forecast")
st.subheader('CJSurf')

project = hopsworks.login()

dataset_api = project.get_dataset_api()
downloaded_file_path = dataset_api.download("Resources/latest_lahinch.png", overwrite=True)

#image = Image.open(downloaded_file_path)

#st.image(image, caption='Lahinch Surf Forecast')
st.image(downloaded_file_path, caption='Lahinch Surf Forecast')
