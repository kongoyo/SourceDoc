import re
import json
import requests
from bs4 import BeautifulSoup

HTML_PARSER = "html.parser"
ROOT_URL = "https://ifoodie.tw/"
list_url = "https://ifoodie.tw/ranking/monthly/%E5%8F%B0%E5%8C%97/"
SHOP_PATH = "support/advertise/"
SPACE_RE = re.compile(r"\s+")

# Function will return a list of dictionaries
# each containing information of books.
def get_shop_name_list(): 
    # requests.get(url) returns a response that is saved
    # in a response object called page(list_req).
    list_req = requests.get(list_url)

    # page.text gives us access to the web data in text
    # format, we pass it as an argument to BeautifulSoup
    # along with the html.parser which will create a
    # parsed tree in soup.
    if list_req.status_code == requests.codes.ok:
        soup = BeautifulSoup(list_req.text, 'html.parser')

    # soup.find_all finds the div's, all having the same
    # class "col-xs-6 col-sm-4 col-md-3 col-lg-3" that is
    # stored in books








        shop_links_a_tags = soup.find('script').get_text()
        relevant = list_req[list_req.index('=')+1:] #removes = and the part before it

        shop_links = []
        for link in shop_links_a_tags:
            shop_link = ROOT_URL + link["href"]
            print(shop_link)
            shop_links.append(shop_link)
            parse_shop_information(shop_link)


def parse_shop_information(shop_link):
    shop_id = re.sub(re.compile(r"^.*/" + SHOP_PATH), "", shop_link).split("-")[0]
    print(shop_id)

    req = requests.get(shop_link)
    if req.status_code == requests.codes.ok:
        soup = BeautifulSoup(req.content, HTML_PARSER)
        shop_header_tag = soup.find("div", id="shop-header")
        name_tag = shop_header_tag.find("span", attrs={"itemprop": "name"})
        print(re.sub(SPACE_RE, "", name_tag.text))
        category_tag = shop_header_tag.find("p", class_={"cate i"})
        print(re.sub(SPACE_RE, "", category_tag.a.text))
        address_tag = shop_header_tag.find("a", attrs={"data-label": "上方地址"})
        print(re.sub(SPACE_RE, "", address_tag.text))

        gps_str = address_tag["href"]
        # print(gps_str)
        gps_str = re.search("/c=(\d+.\d*),(\d+.\d*)/", gps_str).group().replace("/", "")
        # print(gps_str)
        lat = gps_str.split(",")[0]
        lng = gps_str.split(",")[1]
        print(lat.split("=")[1], lng)


if __name__ == "__main__":
    get_shop_link_list()
