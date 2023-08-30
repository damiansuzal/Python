from bs4 import BeautifulSoup
import requests
# URL de la página web a la que deseamos hacer scraping
url = "https://www.lanacion.com.ar"
# Realizamos la solicitud GET a la página web
response = requests.get(url)
# Parseamos el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# En este ejemplo, supongamos que los títulos de las noticias están dentro de etiquetas <h2>
# Iteramos a través de todas las etiquetas <h2> y extraemos el texto
content_title= soup.find_all("h2","title")
for tit in content_title:
    sub= tit.find_all("a")
    print(sub[0].attrs.get("title"))




