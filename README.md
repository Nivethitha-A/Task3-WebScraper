# 📰 News Headlines Web Scraper

This project is a simple Python script that scrapes top news headlines from a public news website and saves them into a text file. It demonstrates basic web scraping using the `requests` library and `BeautifulSoup`.

---

## 🚀 Features
- Fetches HTML content from a news website (BBC News by default)
- Extracts all `<h2>` tags containing headlines
- Saves headlines to `headlines.txt`
- Lightweight, fast, and beginner-friendly

---

## 🛠️ Technologies Used
- Python
- Requests
- BeautifulSoup (bs4)

---

## 📦 Installation

Install required libraries:

```bash
pip install requests beautifulsoup4
```
---

## ▶️ How to Run

```bash
python scraper.py
```

After running, the script will:

1. Fetch top headlines

2. Parse them from the HTML

3. Save them into a file called headlines.txt

## 📁 Project Structure

```text
.
├── scraper.py         # Main script
└── headlines.txt      # Auto-generated file containing scraped headlines
```


## 🎯 Objective

1. This project automates data collection from a public website and helps you learn:

2. How to fetch HTML content

3. How to parse webpages using BeautifulSoup

4. How to extract specific tags 

5. How to store data in a text file
                  
---  

## 📌 Notes

Use this project only for educational purposes.

Follow website terms of service when scraping.

--- 

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

