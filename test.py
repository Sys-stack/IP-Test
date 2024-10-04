import streamlit as st
import requests

# Title for the Streamlit app
st.title("Anime Information Fetcher")

# Create a text input field in Streamlit to get anime name from the user
anime_name = st.text_input("Enter the name of the anime:", "")

# If an anime name is provided, proceed to fetch the data
if anime_name:
    # Jikan API URL to search for the anime
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
    
    # Make a GET request to the Jikan API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the first anime's data (if it exists)
        if data['data']:
            anime_info = data['data'][0]

            # Display the anime information
            st.subheader(anime_info['title'])
            st.image(anime_info['images']['jpg']['large_image_url'])
            st.write(f"Type: {anime_info['type']}")
            st.write(f"Episodes: {anime_info['episodes']}")
            st.write(f"Status: {anime_info['status']}")
            st.write(f"Aired: {anime_info['aired']['string']}")
            st.write(f"Score: {anime_info['score']}")
            st.write(f"Synopsis: {anime_info['synopsis']}")
        else:
            st.error("Anime not found! Please check the spelling or try another anime.")
    else:
        st.error(f"Failed to fetch data. Error code: {response.status_code}")

