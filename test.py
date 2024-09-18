import streamlit as st
import requests
from io import BytesIO
from PIL import Image

if st.checkbox("Show"):
    st.title("DrAni List")
    st.header("Introduction")
    st.subheader("Why DrAni List?")
    st.text('A free website/tool to track your Animes, Series, Manga and Dramas in one website!')
    st.markdown('test')

    # Fetch the image
    url = "https://shiv.tixte.co/wallpaperflare.com_wallpaper_(2).jpg"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using Pillow
        img = Image.open(BytesIO(response.content))
        # Display the image in Streamlit
        st.image(img, width=200)
    else:
        st.error(f"Failed to retrieve image. Status code: {response.status_code}")

