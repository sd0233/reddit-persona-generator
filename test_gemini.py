import os
import praw
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv()

# ✅ Get credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Test Reddit API
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent="RedditPersonaScript/1.0"
)

print("✅ Reddit connected:", reddit.read_only)

# Try fetching some data from Reddit
test_user = "spez"  # Reddit co-founder
user = reddit.redditor(test_user)

print(f"🔎 Testing Reddit user: {test_user}")
print("Recent posts:")
for submission in user.submissions.new(limit=2):
    print(f"  - {submission.title}")

print("Recent comments:")
for comment in user.comments.new(limit=2):
    print(f"  - {comment.body[:50]}...")
# Load the key from .env
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)

# List available models
print("✅ Available models:")
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(" -", m.name)

# Test Gemini with a supported model
model = genai.GenerativeModel("models/gemini-1.5-flash")
response = model.generate_content("Say hello in one line!")
print("✅ Gemini Response:", response.text)

