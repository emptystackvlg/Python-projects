from re import T
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
URL = "https://eos2.vstu.ru/grade/report/overview/index.php"
r = requests.get (URL)
soup = bs (r.text,"html.parser")
titles = soup.find_all("td",class_ = "cell c0")
for name in titles:
    print(name.a)