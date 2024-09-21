
from PIL import Image

#def image
def scale_img(image_path,x_axis,y_axis):
  img = Image.open(image_path)
  resized_image = img.resize((x_axis,y_axis))
  return resized_image

import streamlit as st

st.set_page_config(page_title = 'omg')
#C:/Users/shiva/Downloads/japanese-background-digital-art.jpg

st.image("C:/Users/shiva/Downloads/japan-background-digital-art.jpg")
st.image(scale_img("C:/Users/shiva/Downloads/japan-background-digital-art.jpg", 800,40))
