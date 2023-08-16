import html.parser
import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

product_key = "M2498-06"
url = (
    "https://www.ibm.com/docs/api/v1/content/"
    + product_key
    + "?announcement="
    + product_key
    + "&parsebody=true&lang=en&role="
)
rsp = requests.get(
    "https://www.ibm.com/docs/api/v1/content/M2498-06?announcement=M2498-06&parsebody=true&lang=en&role="
)
soup = BeautifulSoup(rsp.text, "html.parser")
title_element = soup.find("h1", attrs={"id": "Sales-Manual__title__1"})
title_text = title_element.text.strip()
print(title_text)
