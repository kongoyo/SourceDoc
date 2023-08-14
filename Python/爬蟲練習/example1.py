import json
import re

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
        soup = BeautifulSoup(list_req.text, "html.parser")

    # soup.find_all finds the div's, all having the same
    # class "col-xs-6 col-sm-4 col-md-3 col-lg-3" that is
    # stored in book
