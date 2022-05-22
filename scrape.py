import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.reddit.com/r/wallstreetbets/top/?t=all"
page = requests.get(URL).text
doc = BeautifulSoup(page, "html.parser")
with open("test.html", "w") as test_html_file:
    test_html_file.write(str(doc))
