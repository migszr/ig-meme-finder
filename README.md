# IG Real Hashtag Scraper

This app searches real Instagram posts using hashtags and displays live data.

## Features
- Scrapes public posts from real hashtags
- Displays media (image/video)
- Shows likes/views
- Provides download and IG post links

## Setup

1. Add your IG sessionid to `.streamlit/secrets.toml`:
    IG_SESSIONID = "your_session_id_here"

2. Run:
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    streamlit run app.py
