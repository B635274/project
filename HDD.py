import requests
import re
from bs4 import BeautifulSoup

url = "https://easy-laptop.tistory.com/36"
headers = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class":"tt_article_useless_p_margin"})
#print(items[0].find("div", attrs={"class":"head_info"}).get_text())
body = items.find_all("tbody")
#realbody1 : SSD/HDD 순위 상위권
realbody1 = body[1]
trs1 = realbody1.find_all("tr")
for idx, tr in enumerate(trs1):
    if idx > 0:
        tds = tr.find_all("td")
        rank = tds[0].get_text()
        name = tds[1].get_text()
        score = tds[2].get_text()
        print(rank, name, score)


url = "https://easy-laptop.tistory.com/37"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class":"tt_article_useless_p_margin"})
#print(items[0].find("div", attrs={"class":"head_info"}).get_text())
body = items.find_all("tbody")
#realbody2 : SSD/HDD 순위 중상위권
realbody2 = body[1]
trs2 = realbody2.find_all("tr")
for idx, tr in enumerate(trs2):
    if idx > 0:
        tds = tr.find_all("td")
        rank = tds[0].get_text()
        name = tds[1].get_text()
        score = tds[2].get_text()
        print(rank, name, score)


url = "https://easy-laptop.tistory.com/38"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class":"tt_article_useless_p_margin"})
#print(items[0].find("div", attrs={"class":"head_info"}).get_text())
body = items.find_all("tbody")
#realbody3 : SSD/HDD 순위 중하위권
realbody3 = body[1]
trs3 = realbody3.find_all("tr")
for idx, tr in enumerate(trs3):
    if idx > 0:
        tds = tr.find_all("td")
        rank = tds[0].get_text()
        name = tds[1].get_text()
        score = tds[2].get_text()
        print(rank, name, score)

url = "https://easy-laptop.tistory.com/39"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class":"tt_article_useless_p_margin"})
#print(items[0].find("div", attrs={"class":"head_info"}).get_text())
body = items.find_all("tbody")
#realbody4 : SSD/HDD 순위 하위권
realbody4 = body[1]
trs4 = realbody4.find_all("tr")
for idx, tr in enumerate(trs4):
    if idx > 0:
        tds = tr.find_all("td")
        rank = tds[0].get_text()
        name = tds[1].get_text()
        score = tds[2].get_text()
        print(rank, name, score)
