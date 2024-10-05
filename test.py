import streamlit as st
import pandas as pd

# Example DataFrame with image URLs
data = {
    'Anime': ['Naruto', 'One Piece', 'Attack on Titan'],
    'Image URL': [
        'https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg',
        'https://upload.wikimedia.org/wikipedia/en/5/50/OnePieceCover01.jpg',
        'https://upload.wikimedia.org/wikipedia/en/7/79/Shingeki_no_Kyojin_Volume_1.jpg'
    ]
}

df = pd.DataFrame(data)

# Create HTML table with embedded images
html_table = """
<table>
    <thead>
        <tr>
            <th>Anime</th>
            <th>Cover</th>
        </tr>
    </thead>
    <tbody>
"""
# Add each row with an image
for index, row in df.iterrows():
    html_table += f"""
    <tr>
        <td>{row['Anime']}</td>
        <td><img src="{row['Image URL']}" width="100"></td>
    </tr>
    """

html_table += """
    </tbody>
</table>
"""

# Render the table with images
st.markdown(html_table, unsafe_allow_html=True)
