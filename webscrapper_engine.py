import requests
from bs4 import BeautifulSoup

class ws_engine():
    
    #Obtiene el codigo HTML de una pagina web
    def obtener_codigo_html(self, url:str):
        try:
            cabeceras_html= {
                "User-Agent": "MarcoPMCReader/1.0 (mailto:tu_correo@dominio.com)",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "es-MX,es;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
            }
            response=requests.get(url, headers=cabeceras_html)
            response.raise_for_status()
            codigo_web=response.text
            return codigo_web
        
        except requests.exceptions.RequestException as error:
            print(f"Error al entrar a la URL {url}")
            print(f"Error: {error}")
            return False

    #Obtiene todas los href de una pagina en particular cuando los a están en clase
    def obtener_lista_href_clase(self, pagina_web:str, clase:str):
        try:
            codigo_web=self.obtener_codigo_html(pagina_web)
            lista_href=[]

            soup = BeautifulSoup(codigo_web, 'html.parser')
            enlaces = soup.find_all('a', class_=clase)

            for href in enlaces:
                lista_href.append(href.get('href'))

            return lista_href
        
        except requests.exceptions.RequestException as error:
            print(f"No se pudo contectar a: {pagina_web}")
            print(f"Error: {error}")

    #Obtiene todas los href de una pagina en particular cuando los a están en atributos
    def obtener_lista_href_atributos(self, pagina_web:str, atributo:str, nombre_atributo:str):
        try:
            codigo_web=self.obtener_codigo_html(pagina_web)
            lista_href=[]

            soup = BeautifulSoup(codigo_web, 'html.parser')
            enlaces = soup.find_all('a', attrs={atributo: nombre_atributo})

            for href in enlaces:
                lista_href.append(href.get('href'))

            return lista_href
        
        except requests.exceptions.RequestException as error:
            print(f"No se pudo conectar a: {pagina_web}")
            print(f"Error: {error}")