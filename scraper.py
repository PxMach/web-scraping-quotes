from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes  = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})
tags = soup.find_all("a", class_="tag")

for quote, author, tag in zip(quotes, authors, tags):
    print(quote.text + " . " + author.text + tag.text) 