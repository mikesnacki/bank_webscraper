
import requests as rq
from bs4 import BeautifulSoup

mtb_url = r"https://www.mtb.com/banking/checking-accounts"
page = rq.get(mtb_url)
soup = BeautifulSoup(page.content, 'html.parser')
print("hi")