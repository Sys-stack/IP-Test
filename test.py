import requests
from io import BytesIO as by
from PIL import Image

#def image
def scale_img(image_path,x_axis,y_axis):
  res = requests.get(image_path)
  img = Image.open(by(res.content))
  resized_image = img.resize((x_axis,y_axis))
  return resized_image

import streamlit as st



st.set_page_config(
  page_title = "DrAniList",
  page_icon = "",
  layout = 'wide',
  initial_sidebar_state = 'collapsed',
  )
st.image("https://raw.githubusercontent.com/Sys-stack/IP-Test/test/japan-background-digital-art.jpg")
st.image(scale_img("https://raw.githubusercontent.com/Sys-stack/IP-Test/test/japan-background-digital-art.jpg", 2000,40))
