import webscrapper_engine

ws = webscrapper_engine.ws_engine()

#pagina_web = "https://www.vademecum.es/principios-activos-atc-mx-d_1"
#pagina_web = "https://www.vademecum.es/mexico/mx/alfa/m/a"
pagina_web = "https://drmarcopalacios.com"
nombre_txt = "hola.txt"
tag = "a"
clase = ""
atributo = "target"
nombre_atributo = "_top"
clase_div = "e-con-inner"


#print(ws.obtener_codigo_html(pagina_web))
print(ws.obtener_lista_href_atributos(pagina_web, atributo, nombre_atributo))
print(ws.obtener_div_clase(pagina_web, clase_div))