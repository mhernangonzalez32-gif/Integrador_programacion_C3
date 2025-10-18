def buscar_pais_nombre(lista_paises, nombre_pais):
    resultados = []
    nombre_pais = nombre_pais.lower()
    for pais in lista_paises:
        if nombre_pais in pais["nombre"].lower():
            resultados.append(pais)
    return resultados