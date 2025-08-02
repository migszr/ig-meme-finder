import instaloader
from instaloader import Profile
import random
import streamlit as st

def scrape_instagram_posts(username, max_posts=5):
    # Create an Instaloader instance
    L = instaloader.Instaloader()

    # Get credentials from Streamlit secrets
    IG_USERNAME = st.secrets["IG_USERNAME"]
    IG_PASSWORD = st.secrets["IG_PASSWORD"]

    try:
        # Login to Instagram
        L.login(IG_USERNAME, IG_PASSWORD)

        # Get the profile
        profile = Profile.from_username(L.context, username.strip("@"))

        # Fetch posts
        posts = profile.get_posts()

        results = []
        for i, post in enumerate(posts):
            if i >= max_posts:
                break
            results.append({
                "username": username,
                "caption": post.caption or "No caption",
                "score": round(random.uniform(0.8, 0.95), 2),  # Mock similarity score
                "image": post.url  # Image or thumbnail URL
            })

        return results

    except Exception as e:
        return [{
            "username": username,
            "caption": f"Error: {str(e)}",
            "score": 0,
            "image": ""
        }]
