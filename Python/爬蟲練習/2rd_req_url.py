import requests
from bs4 import BeautifulSoup

url = "https://www.ibm.com/docs/api/v1/search/announcements?query=2072%2006&type=salesManual&start=0&limit=20"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
article = soup.select("topics")
article_str = str(article)
print(article_str)
