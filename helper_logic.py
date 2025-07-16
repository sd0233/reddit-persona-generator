import praw
import os
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Reddit credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")

# ✅ Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Initialize Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="RedditPersonaScript/1.0"
)

# ✅ Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

def extract_username_from_url(profile_url: str) -> str:
    """
    Extracts Reddit username from profile URL.
    Example: https://www.reddit.com/user/kojied/ → kojied
    """
    return profile_url.rstrip("/").split("/")[-1]

def scrape_reddit_data(username: str, limit: int = 30):
    """
    Scrapes a user's recent posts & comments.
    Returns a list of (type, text) tuples.
    """
    print(f"✅ Scraping Reddit user: {username}")
    user = reddit.redditor(username)
    scraped_data = []

    # Recent posts
    for post in user.submissions.new(limit=limit):
        content = f"TITLE: {post.title}\nBODY: {post.selftext}"
        scraped_data.append(("Post", content))

    # Recent comments
    for comment in user.comments.new(limit=limit):
        scraped_data.append(("Comment", comment.body))

    return scraped_data

def build_persona_with_citations(scraped_data):
    """
    Sends scraped data to Gemini and generates a persona.
    Includes citations for each characteristic.
    """
    combined_text = "\n\n".join([f"{t.upper()}: {c}" for t, c in scraped_data])

    prompt = f"""
    You are an AI that analyzes Reddit profiles.
    Based on the following Reddit posts & comments, create a detailed user persona with:

    1. **Name (if possible)**
    2. **Interests & hobbies**
    3. **Personality traits**
    4. **Occupation or education clues**
    5. **Writing style & tone**
    6. **Possible location or demographics (if inferred)**
    7. **Final one-paragraph summary**

    For **each characteristic**, also provide **citations (quote a relevant post/comment)** used to infer it.

    ---
    Reddit User Data:
    {combined_text}
    """

    print("✅ Sending data to Gemini for persona generation...")
    response = gemini_model.generate_content(prompt)

    return response.text
