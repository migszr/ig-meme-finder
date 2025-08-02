import instaloader
from instaloader import Profile
import random
import streamlit as st

def scrape_instagram_posts(username, max_posts=5):
    L = instaloader.Instaloader()

    # Use sessionid from Streamlit secrets
    sessionid = st.secrets["IG_SESSIONID"]
    L.context._session.cookies.set("sessionid", sessionid)
    L.context.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # Optional: spoof desktop browser

    try:
        profile = Profile.from_username(L.context, username.strip("@"))
        posts = profile.get_posts()

        results = []
        for i, post in enumerate(posts):
            if i >= max_posts:
                break
            results.append({
                "username": username,
                "caption": post.caption or "No caption",
                "score": round(random.uniform(0.8, 0.95), 2),
                "image": post.url
            })

        return results

    except Exception as e:
        return [{
            "username": username,
            "caption": f"Error: {str(e)}",
            "score": 0,
            "image": ""
        }]
