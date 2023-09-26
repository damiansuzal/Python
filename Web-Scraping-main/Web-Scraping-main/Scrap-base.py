#instalar: pip install lxml
from bs4 import BeautifulSoup
import requests

# Obtener el documento HTML/ ver la posibilidad de hacer un input para ingresar la pelicula
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# Localizar la caja (box) que contiene el titulo (title) y transcript
box = soup.find('article', class_='main-article')
# Localizar el titulo (title) y transcript
title = box.find('h1').get_text()
print(title)
