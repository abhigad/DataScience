import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    
    if response.text.__contains__("403" or "50") :
        return response.text
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all paragraph texts
    paragraphs = soup.find_all('p')
    texts = [p.text for p in paragraphs]
    
    return texts

# Usage
url = 'https://www.barrons.com/articles/amazon-stock-price-apple-ai-spending-0b4b25e0'
scraped_texts = scrape_website(url)
for text in scraped_texts:
    print(text)