import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import csv

# Vamos a crear una función que permite obtener información de algo que busquemos en wikipedia mediante el webscraping

def extraer_datos_wiki(url):
    """Función que extrae información de una pagina web, de wikipedia en este caso 

    Args:
        url (string): url de la página web de la que se quiere extarer la información.
    """
    # Encabezado que simula la solicitud realizada por un navegador web real, y cuya utilidad es evitar el bloqueo de ciertos servidores 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

    # Creamos la colicitud HTTP, de tipo get, es decir le pedimos que nos coja cierta información de la página web.
    r = requests.get(url, headers=headers)

    # Creamos la condición en la que se comprueba que no ha habido problemas en la solicitud
    if r.status_code != 200:
        print(f"Error en la solicitud: {r.status_code}")
    else:
        ...

    # Creamos una variable que va a contener todo el contenido del html de la página web. Para ello usamos la clase BeautifulSoup.
    soup = BeautifulSoup(r.content, "html.parser") 
    # Buscamos las tablas en el html
    tablas = soup.find_all("table", {"class" : "wikitable"})

    # 
    emperadores = []
    for tabla in tablas: 
        filas = tabla.find_all("tr") # Encontramos todas las filas de cada tabla
        for fila in filas[1:]:
            columnas = fila.find_all("td") # Encontramos todas las celdas de cada tabla
            if len(columnas) >= 5:
                nombre = columnas[2].get_text(strip = True) # Extraemos y limpiamos el texto de la celda correspondiente
                inicio = columnas[3].get_text(strip = True)
                fin = columnas[4].get_text(strip = True)
                emperadores.append({"nombre": nombre, "inicio": inicio, "fin": fin})

    # Creamos el código para guardar el csv la información extraída
    campos = ["nombre", "inicio", "fin"]
    with open("emperadores_romanos.csv", "w", encoding = "utf-8") as archivo:
        csv_writer = csv.DictWriter(archivo, fieldnames = campos)
        csv_writer.writeheader()
        csv_writer.writerows(emperadores)
    

    # Con el siguiente código nos creamos un archivo que contiene todo el html de la web
    ruta_guardado = "HTML emperadores romanos"
    with open(ruta_guardado, "w", encoding = "utf-8") as archivo:
        archivo.write(soup.prettify())

if __name__ == "__main__":
    #sys.stdout.reconfigure(encoding = "utf-8")
    extraer_datos_wiki("https://es.wikipedia.org/wiki/Anexo:Emperadores_romanos")

# Le pedimos que nos printee los primeros 500 caracteres del HTML.
# print(soup.prettify()[:500])
# dinastias = soup.find_all("p", {"class": "mw-heading mw-heading3"})