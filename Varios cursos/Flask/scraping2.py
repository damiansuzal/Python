import urllib.request
datos = urllib.request.urlopen("https://www.dolarsi.com").read().decode()
from bs4 import BeautifulSoup
		
# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontrar el div con el id "contenido"
contenido_div = soup.find("div", class="venta")

# Encontrar el párrafo dentro del div
parrafo = contenido_div.find("Venta")
# parrafo = contenido_div.find("p")

# Imprimir el contenido del párrafo
if parrafo:
    print(parrafo.text)
else:
    print("No se encontró el párrafo.")