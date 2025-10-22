import difflib

def buscar_pais_nombre(lista_paises, nombre_pais):
    """
    Busca países cuyo nombre coincida exactamente, parcialmente o sea similar
    al nombre proporcionado, incluso si está mal escrito.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios con claves 'nombre', 'poblacion', 'superficie', 'continente'.
        nombre_pais (str): Nombre (o parte del nombre) del país a buscar.
    
    Retorna:
        list: Lista de países que coinciden o son similares al nombre dado.
              Si no hay coincidencias, devuelve una lista vacía.
    
    Lanza:
        TypeError: Si 'lista_paises' no es una lista o 'nombre_pais' no es una cadena.
    """
    try:
        # Validaciones iniciales
        if not isinstance(lista_paises, list):
            raise TypeError("El primer argumento debe ser una lista de países.")
        if not isinstance(nombre_pais, str):
            raise TypeError("El nombre del país debe ser una cadena de texto.")
        
        nombre_pais = nombre_pais.strip().lower()
        if not nombre_pais:
            return []  # Búsqueda vacía

        # 1. Primero intentamos coincidencias parciales/exactas (más rápidas)
        coincidencias_directas = []
        for pais in lista_paises:
            if not isinstance(pais, dict) or "nombre" not in pais:
                continue  # Saltea entradas mal formadas
            if nombre_pais in pais["nombre"].lower():
                coincidencias_directas.append(pais)

        # Si ya hay resultados directos, los devolvemos (prioridad)
        if coincidencias_directas:
            return coincidencias_directas

        # 2. Si no hay coincidencias directas, buscamos nombres similares
        nombres_paises = [pais["nombre"] for pais in lista_paises if isinstance(pais, dict) and "nombre" in pais]
        nombres_similares = difflib.get_close_matches(nombre_pais, [n.lower() for n in nombres_paises], n=5, cutoff=0.6)

        # Recuperamos los países completos cuyos nombres coinciden con las sugerencias
        resultados_similares = []
        for nombre_sim in nombres_similares:
            for pais in lista_paises:
                if isinstance(pais, dict) and "nombre" in pais:
                    if pais["nombre"].lower() == nombre_sim:
                        resultados_similares.append(pais)
                        break  # Evita duplicados si hay nombres repetidos

        return resultados_similares

    except Exception as e:
        # Manejo genérico de errores (puedes personalizar según necesidad)
        print(f"Error en la búsqueda del país: {e}")
        return []