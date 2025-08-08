import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

titles = soup.find_all(class_="tpl-lbl css-5mgoji")

for title in titles:
    text = title.get_text(strip=True)
    if text:
        print(text)