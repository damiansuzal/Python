import requests # https://docs.python-requests.org/en/v2.0.0/
from bs4 import BeautifulSoup as bs # https://tedboy.github.io/bs4_doc/
response = requests.get("https://dolarhoy.com/")
html = response.text
page=bs(html,"html.parser")
dolar_div=page.find("div",attrs={"class":"tile dolar"})
childs= dolar_div.find_all("div",attrs={"class":"tile is-child"})
for x in childs:
  print(x.a.text,":")
  values=x.div.find_all("div",attrs={"class":"val"})
  try:
    print("\tPrecio de venta: ",values[1].text)
    print("\tPrecio de compra: ",values[0].text)
    print("")
  except:
    print("\tPrecio de venta: ",values[0].text)
    print("")