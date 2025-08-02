import streamlit as st
from utils import scrape_instagram_posts

st.set_page_config(page_title="IG Meme Finder", layout="wide")
st.title("Find Instagram Content Similar to @mexvines")

seed_username = st.text_input("Start with an account:", "@mexvines")

if st.button("Find Similar Content"):
    with st.spinner("Scraping content..."):
        results = scrape_instagram_posts(seed_username)

    for item in results:
        if item["image"]:
            st.image(item["image"], width=300)
        st.markdown(f"**@{item['username']}**")
        st.markdown(f"Caption: {item['caption']}")
        st.markdown(f"Similarity Score: `{item['score']}`")
