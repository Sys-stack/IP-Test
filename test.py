import streamlit as st
if st.checkbox("Show"):
  st.title("DrAni List")
  st.header("Introduction")
  st.subheader("Why DrAni List?")
st.text('A free website/tool to track your Animes, Series, Manda and Dramas in one website!')
st.markdown('test')
from PIL import Image as im
img = im.open("https://shiv.tixte.co/wallpaperflare.com_wallpaper_(2).jpg")
st.img(img, width = 200)

