import funciones.mis_funciones as mis_funciones

def buscar_pais_nombre(lista_paises):
    # Pedimos que ingrese el nombre o alguna similitud
    print("-" * mis_funciones.ANCHO_TOTAL)
    nombre_buscado = input("Que pais esta buscando?\n")
    print("-" * mis_funciones.ANCHO_TOTAL)
    
    # Normalizar el término de búsqueda del usuario
    termino_normalizado = mis_funciones.normalizar_manual(nombre_buscado)
    
    if not termino_normalizado:
        return print(mis_funciones.menu_centro(f"--- Error: No ingresó un término de búsqueda ---"))
    resultados = []
    
    # Iterar sobre la lista de países
    for pais in lista_paises:
        # Obtener el nombre del país del diccionario [cite: 20]
        nombre_pais_actual = pais.get('nombre', '') 
        
        # Normalizar el nombre del país para la comparación
        nombre_actual_normalizado = mis_funciones.normalizar_manual(nombre_pais_actual)
        
        # Comprobar si el término buscado está DENTRO del nombre del país
        # Esto cumple con la "coincidencia parcial" 
        if termino_normalizado in nombre_actual_normalizado:
            resultados.append(pais)
            
    #  Devolver los resultados 
    if not resultados:
        # Cumplir con "Mensajes claros de éxito/error" [cite: 69]
        return print(mis_funciones.menu_centro(f"--- No se encontraron resultados para '{nombre_buscado}' ---"))
    
    print(mis_funciones.menu_centro(f"--- Resultados para '{nombre_buscado}' ({len(resultados)} encontrados) ---"))
    
    return mis_funciones.imprimir_resutados(resultados)