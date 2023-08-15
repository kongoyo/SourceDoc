import requests
from bs4 import BeautifulSoup

url = "https://www.ibm.com/storage/products"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    storage_products = soup.find_all("div", class_="product-card")

    for product in storage_products:
        product_name = product.find("h3", class_="product-card__name").text.strip()
        announced_date = product.find(
            "p", class_="product-card__releasedate"
        ).text.strip()

        print(f"Product: {product_name}\nAnnounced Date: {announced_date}\n")
else:
    print("Failed to retrieve data from the IBM website.")
