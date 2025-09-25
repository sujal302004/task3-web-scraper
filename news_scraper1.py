import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"  # Change if you want another site

response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Grab <h2> and <h3> headlines
headlines = soup.find_all(["h2", "h3"])

headline_list = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:
        headline_list.append(text)

# Save to .txt file
with open("news_headlines.txt", "w", encoding="utf-8") as file:
    for idx, headline in enumerate(headline_list, start=1):
        file.write(f"{idx}. {headline}\n")

print(f"Scraped {len(headline_list)} headlines. Saved to 'news_headlines.txt'.")
 