import webscrapper_engine
import vademecum_ws_engine

ws = webscrapper_engine.ws_engine()
v_ws = vademecum_ws_engine.v_ws_engine()

pagina_web = "https://www.vademecum.es/principios-activos-atc-mx-d_1"
#pagina_web = "https://www.vademecum.es/mexico/mx/alfa/m/a"
nombre_txt = "hola.txt"
tag = "a"
clase = ""
atributo = "target"
nombre_atributo = "_top"


#print(ws.obtener_codigo_html(pagina_web))
print(ws.obtener_lista_href_atributos(pagina_web, atributo, nombre_atributo))