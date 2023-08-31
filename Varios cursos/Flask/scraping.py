import urllib.request
datos = urllib.request.urlopen("https://www.dolarsi.com").read().decode()
from bs4 import BeautifulSoup
soup =  BeautifulSoup(datos)
tags = soup("a")


for tag in tags:
		print(tag.get("href"))