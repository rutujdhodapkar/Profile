import streamlit as st

# Set page config
st.set_page_config(page_title="Index.html Viewer", layout="wide")

# Title of the app
st.title("Display HTML File in Streamlit")

# Path to the HTML file
html_file = "index.html"

# Read the HTML file
try:
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Display the HTML file
    st.markdown(html_content, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("The file 'index.html' was not found. Please ensure it's in the same directory as this script.")
