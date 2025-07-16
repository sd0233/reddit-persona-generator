Reddit Persona Generator
A Python-based tool that scrapes Reddit posts & comments for a given user profile, then uses Google Gemini AI to generate a detailed User Persona with citations for each insight.
This project was built as part of a 48-hour coding assignment to showcase problem-solving skills, API integration, and LLM-powered data analysis.

🚀 Features

✅ Scrape Reddit Posts & Comments for any user
✅ Build a User Persona with insights like:

Interests & hobbies

Personality traits

Frequently discussed topics

Writing style
✅ Citations → Each persona trait is linked to actual posts/comments
✅ AI-powered summarization using Google Gemini
✅ Output as a text file for easy review
✅ PEP-8 Compliant & Modular Code Structure

🛠️ Tech Stack
Python 3.10+

PRAW → Reddit API wrapper for scraping posts & comments

Google Gemini API → To analyze text and generate persona

dotenv → To securely load API keys

Virtual Environment for isolated dependencies

📂 Project Structure

reddit-persona-generator/
│── main.py              # Entry point – runs full persona generation
│── helper_logic.py      # Helper functions for scraping & AI analysis
│── output/              # Stores generated persona text files
│── requirements.txt     # Dependencies
│── .env.example         # Example env file with placeholders
│── .gitignore           # Ignores secrets & cache
│── README.md            # You are here!


🔑 How It Works
1️⃣ Input a Reddit Profile URL (e.g., https://www.reddit.com/user/kojied/)
2️⃣ Scrape recent posts & comments using praw
3️⃣ Send scraped text to Gemini AI for summarization
4️⃣ AI builds a User Persona → “This user seems to like gaming & tech…”
5️⃣ Save Output in output/username_persona.txt with citations

🖥️ Setup & Usage
1️⃣ Clone Repo

git clone https://github.com/sd0233/reddit-persona-generator.git
cd reddit-persona-generator

2️⃣ Setup Virtual Environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
bash

pip install -r requirements.txt
4️⃣ Configure API Keys
Copy .env.example → .env and fill in your keys:


REDDIT_CLIENT_ID=xxxx
REDDIT_CLIENT_SECRET=xxxx
GEMINI_API_KEY=xxxx

5️⃣ Run Script

python main.py

✅ Output will be saved in output/ folder.

📄 Sample Output
Example User Persona for kojied:

Persona Summary:
- Loves discussing tech & open-source
- Active in gaming communities
- Shares opinions in thoughtful, long comments

Citations:
- Post: "My Linux setup experience..."
- Comment: "I think AI will change gaming..."



🎯 Why This Project?
This assignment allowed me to:

✅ Integrate multiple APIs (Reddit + Gemini AI)
✅ Practice data scraping, cleaning & summarization
✅ Use LLMs to generate meaningful insights
✅ Showcase problem-solving in a short 48-hour deadline

I approached this project with modular, scalable code so it can be extended later (e.g., multi-user analysis, JSON export, web UI).

🌟 Future Improvements
Add sentiment analysis

Deploy as a web app (Flask/Streamlit)

Store personas in a database for historical tracking

👨‍💻 About Me
I’m Sahil Dhote, a passionate Python & AI enthusiast with an interest in LLM applications, web development, and API integrations.
This project reflects my curiosity, structured thinking, and ability to deliver under deadlines.

📬 Contact:8459332362
📧 Email: sddhote23@gmail.com
🔗 LinkedIn: linkedin.com/in/sahil-dhote-116191206
🐙 GitHub: github.com/sd0233

