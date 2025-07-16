import sys
import os
from helper_logic import extract_username_from_url, scrape_reddit_data, build_persona_with_citations

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username_from_url(profile_url)

    # ✅ Scrape Reddit user data
    scraped_data = scrape_reddit_data(username)

    if not scraped_data:
        print(f"❌ No data found for user {username}")
        return

    # ✅ Build persona with Gemini AI
    persona_text = build_persona_with_citations(scraped_data)

    # ✅ Save output
    os.makedirs("output", exist_ok=True)
    output_file = f"output/persona_{username}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"✅ Persona generated and saved → {output_file}")

if __name__ == "__main__":
    main()
