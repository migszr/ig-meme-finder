import instaloader
from instaloader import Post, Hashtag
import streamlit as st

def search_hashtag_posts(hashtags, max_posts=5):
    sessionid = st.secrets["IG_SESSIONID"]
    L = instaloader.Instaloader()
    L.context._session.cookies.set("sessionid", sessionid)
    L.context.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

    posts_seen = []
    seen_ids = set()

    for tag in hashtags:
        try:
            hashtag = Hashtag.from_name(L.context, tag.lstrip("#"))
            for post in hashtag.get_posts():
                if post.shortcode in seen_ids:
                    continue
                seen_ids.add(post.shortcode)

                media_type = "image"
                if post.typename == "GraphVideo":
                    media_type = "video"

                post_data = {
                    "username": post.owner_username,
                    "caption": post.caption or "No caption",
                    "likes": post.likes,
                    "views": post.video_view_count if post.typename == "GraphVideo" else None,
                    "media_type": media_type,
                    "media_url": post.url,
                    "post_url": f"https://www.instagram.com/p/{post.shortcode}/",
                    "score": 1.0,  # placeholder for future ML scoring
                    "matched_tag": tag
                }
                posts_seen.append(post_data)

                if len(posts_seen) >= max_posts:
                    return posts_seen
    
        except Exception as e:
            st.error(f"Error loading #{tag}: {e}")

        except Exception as e:
            posts_seen.append({
                "username": "error",
                "caption": f"Error loading #{tag}: {str(e)}",
                "likes": 0,
                "views": None,
                "media_type": "image",
                "media_url": "",
                "post_url": "",
                "score": 0,
                "matched_tag": tag
            })
    return posts_seen
