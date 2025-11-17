import requests
from bs4 import BeautifulSoup

# URL of the news website you want to scrape
URL = "https://www.bbc.com/news"

def fetch_headlines():
    # Send a GET request to the website
    response = requests.get(URL)

    # Check if request was successful
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return []
                 
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all <h2> tags (headlines)
    headline_tags = soup.find_all("h2")

    # Extract text from each <h2>
    headlines = [tag.get_text(strip=True) for tag in headline_tags]

    return headlines


def save_to_file(headlines):
    # Save headlines to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            file.write(h + "\n")
    print("Headlines saved to headlines.txt")


if __name__ == "__main__":
    headlines = fetch_headlines()

    if headlines:
        print("Headlines found:", len(headlines))
        save_to_file(headlines)
    else:
        print("No headlines found.")
