import instaloader
from instaloader import Profile
import random

def scrape_instagram_posts(username, max_posts=5):
    L = instaloader.Instaloader()
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
                "score": round(random.uniform(0.8, 0.95), 2),  # Mock score
                "image": post.url  # URL to post image or thumbnail
            })
        return results
    except Exception as e:
        return [{"username": username, "caption": f"Error: {str(e)}", "score": 0, "image": ""}]
