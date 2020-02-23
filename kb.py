
import requests as rq
from bs4 import BeautifulSoup
import re

url = r"https://www.key.com/personal/checking/checking-accounts-options.jsp"
page = rq.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
checking_accts = soup.find_all("div", class_=re.compile("listing__group-item"))

checking_names = []

for checking_acct in checking_accts:
    try:
        account = checking_acct.find("div", class_="kds-card__content")
        header = account.find("h3")
        account_title = header.find("a").text
        checking_names.append(re.sub('[^A-Za-z0-9]+', ' ', account_title))
    except AttributeError:
        pass
    
