import funciones.mis_funciones as mis_funciones
def agregar_pais(lista_paises):
    
    nombre_nuevo = input("¿Cómo se llama el nuevo país? \n")
    
    # 1. Verificamos si ya existe
    duplicado_encontrado = False
    for pais in lista_paises:
        if pais['nombre'] == nombre_nuevo:
            duplicado_encontrado = True
            break # Rompemos el bucle
            
    if duplicado_encontrado:
        print(f"Error: El país '{nombre_nuevo}' ya existe.")
        return

    # 2. Pedimos los OTROS datos
    try:
        poblacion_nueva = int(input(f"¿Población de {nombre_nuevo}? \n"))
        superficie_nueva = int(input(f"¿Población de {nombre_nuevo}? \n"))
        continente_nuevo = mis_funciones.menu_con()
        opcion = mis_funciones.numero_opcion(6)
    except ValueError:
        poblacion_nueva = 0
        superficie_nueva = 0

    # 3. Creamos el nuevo "país" (el diccionario)
    nuevo_pais = {
        "nombre": nombre_nuevo,
        "poblacion": poblacion_nueva,
        "superficie": superficie_nueva,
        "continente": continente_nuevo
    }
    
    # 4. Lo añadimos a la lista
    lista_paises.append(nuevo_pais)
    print(f"¡País '{nombre_nuevo}' agregado con éxito!")





