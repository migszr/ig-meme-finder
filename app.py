import streamlit as st
from utils import search_hashtag_posts

st.set_page_config(page_title="IG Real Hashtag Scraper", layout="wide")
st.title("Find Real IG Content by Hashtag (Style Match)")

default_tags = "#mexicohumor, #chingon, #latinhumor"
tag_input = st.text_input("Enter hashtags (comma separated):", default_tags)

if st.button("Search IG Content"):
    tag_list = [tag.strip().lstrip("#").lower() for tag in tag_input.split(",") if tag.strip()]
    st.markdown(f"**Searching posts using hashtags:** {', '.join(tag_list)}")

    results = search_hashtag_posts(tag_list)

    for item in results:
        st.markdown("---")
        if item["media_url"]:
            if item["media_type"] == "image":
                st.image(item["media_url"], width=300)
            else:
                st.video(item["media_url"])

        st.markdown(f"**@{item['username']}** | Hashtag: #{item['matched_tag']}")
        st.markdown(f"Caption: {item['caption']}")
        if item["views"]:
            st.markdown(f"▶️ {item['views']:,} views")
        st.markdown(f"❤️ {item['likes']:,} likes")
        if item["post_url"]:
            st.markdown(f"[🔗 View Post]({item['post_url']})")
        if item["media_url"]:
            st.markdown(f"[📥 Download Media]({item['media_url']})")
