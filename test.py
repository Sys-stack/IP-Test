import streamlit as st
from io import BytesIO as bi
if st.checkbox("Show"):
  st.title("DrAni List")
  st.header("Introduction")
  st.subheader("Why DrAni List?")
st.text('A free website/tool to track your Animes, Series, Manda and Dramas in one website!')
st.markdown('test')
from PIL import Image as im
res = response.("https://shiv.tixte.co/wallpaperflare.com_wallpaper_(2).jpg")
img = im.open(bi(response.content))
st.img(img, width = 200)

