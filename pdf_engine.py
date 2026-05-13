import os
import re
import json
import pypdf
import unicodedata

class pdf_engine():
    
    #Obtiene el contenido de uno de los documentos PDF
    def obtener_contenido_pdf(self, metadata_libro:dict):
        pdf_lector = pypdf.PdfReader(metadata_libro["ruta_archivo_PDF"])
        pdf_lista_paginas = []
        caracteres_bloqueados = ["\n", "\\n", "\r", "\'", '\"', "'", '"', "\\x"]

        for pagina in pdf_lector.pages:
            pdf_contenido_pagina = pagina.extract_text()
            pdf_contenido_pagina_limpio = self.limpiar_caracteres_adicionales_pdf(pdf_contenido_pagina, caracteres_bloqueados)
            pdf_lista_paginas.append(pdf_contenido_pagina_limpio)
        
        return pdf_lista_paginas

    #Limpia un texto de caracteres adicionales 
    def limpiar_caracteres_adicionales_pdf(self, texto_pdf:str, caracteres_bloqueados:list):
        for caracter in caracteres_bloqueados:
            texto_pdf = texto_pdf.replace(caracter, "")

        return texto_pdf
    
    #***Crea un archivo TXT por cada pagina de un PDF que se le pasa
    def crear_paginasPDF_a_txt(self, pdf_lista_paginas:list, metadata_libro:dict):
        ruta_carpeta_paginasPDF_txt = f"{metadata_libro["titulo_libro"]}/paginasTXT"

        if not os.path.exists(ruta_carpeta_paginasPDF_txt):
            os.makedirs(ruta_carpeta_paginasPDF_txt)
        
        contador_de_paginas = 1

        for pagina in pdf_lista_paginas:
            try:
                ruta_archivo_paginasPDF_txt = f"{ruta_carpeta_paginasPDF_txt}/{contador_de_paginas}.txt"
                archivo_txt = open(ruta_archivo_paginasPDF_txt, "w+", encoding="utf-8")
                archivo_txt.write(pagina)
                archivo_txt.close()
                contador_de_paginas += 1
            
            except:
                print(f"Error al crear el archivo TXT {contador_de_paginas}")

        print("Se crearon las páginas en TXT")

    #***Crea un archivo TXT por cada pagina de un PDF que se le pasa, pero le da formato JSON
    def crear_paginasPDF_a_json(self, pdf_lista_paginas:list, metadata_libro:dict):
        ruta_carpeta_paginasPDF_json = f"{metadata_libro["titulo_libro"]}/paginasJSON"

        if not os.path.exists(ruta_carpeta_paginasPDF_json):
            os.makedirs(ruta_carpeta_paginasPDF_json)

        contador_de_paginas = 1

        for pagina in pdf_lista_paginas:
            try:
                ruta_archivo_paginasPDF_json = f"{ruta_carpeta_paginasPDF_json}/{contador_de_paginas}.json"
                archivo_json = open(ruta_archivo_paginasPDF_json, "w+", encoding="utf-8")
                formato_json = {
                    "titulo_libro":metadata_libro["titulo_libro"],
                    "año":metadata_libro["año"],
                    "edicion":metadata_libro["edicion"],
                    "numero_de_pagina":contador_de_paginas,
                    "contenido_pagina":pagina
                }
                pagina_json = json.dumps(formato_json, ensure_ascii=False)
                archivo_json.write(pagina_json)
                archivo_json.close()
                contador_de_paginas += 1
            
            except:
                print(f"Error al crear el archivo JSON {contador_de_paginas}")

        print("Se crearon las páginas en JSON")