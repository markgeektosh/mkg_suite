import pdf_engine

pdf_ = pdf_engine.pdf_engine()
pdf_path = "MIP3.pdf"

metadata_libro = {
    "titulo_libro":"MIP 3",
    "año":"2016",
    "edicion":"3ra edicion",
    "ruta_archivo_PDF":"MIP3.pdf",
    "nombre_PDF_capitulos":"MIP3"
}

marcadores_capitulos = {
    "Capitulo de muestra": 3+68,
    "Capitulo de muerta 5": 68+142
}

lista_de_paginas = pdf_.obtener_contenido_pdf(metadata_libro)

#pdf_.crear_paginasPDF_a_txt(lista_de_paginas, metadata_libro)
#pdf_.crear_paginasPDF_a_json(lista_de_paginas, metadata_libro)
#pdf_.agregar_marcador_capitulos(metadata_libro, marcadores_capitulos)
pdf_.obtener_marcadores_capitulos_PDF(metadata_libro)