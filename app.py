import streamlit as st
import time

st.write("My portfolio is available at: [rutujdhodapkar.vercel.app](https://rutujdhodapkar.vercel.app)")

if st.button("Go to Portfolio"):
    st.markdown('<meta http-equiv="refresh" content="0; url=https://rutujdhodapkar.vercel.app">', unsafe_allow_html=True)

st.image("https://rutujdhodapkar.vercel.app/preview.png", caption="Preview of my portfolio site")  # Replace with actual preview image URL

# Display the web preview using an iframe
st.markdown(
    """
    <iframe src="https://rutujdhodapkar.vercel.app" width="700" height="500" frameborder="0"></iframe>
    """,
    unsafe_allow_html=True
)

# Wait for 5 seconds and then show the message
time.sleep(5)
st.write("Taking longer than usual")
