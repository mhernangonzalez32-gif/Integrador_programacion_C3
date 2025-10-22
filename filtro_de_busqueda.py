import mis_funciones

# Menú para elegir continente (usado en buscar_por_continente)
menu_con = (
    "Elige algún continente:\n"
    "1. América del Sur\n"
    "2. América del Norte\n"
    "3. Europa\n"
    "4. África\n"
    "5. Asia\n"
    "6. Oceanía\n"
)

# Menú principal de filtros
menu_filtros = (
    "¿Qué tipo de filtros deseas usar?\n"
    "1. Buscar por continente\n"
    "2. Buscar por rango de población\n"
    "3. Buscar por rango de superficie\n"
    "4. Mostrar lista filtrada\n"
)


def buscar_por_continente(lista_paises):
    """
    Filtra países por continente según la opción elegida por el usuario.
    Usa una lista predefinida de continentes para evitar errores de escritura.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios con datos de países.
    
    Retorna:
        list: Lista de países que pertenecen al continente seleccionado.
            Devuelve una lista vacía si no hay coincidencias o hay error.
    """
    try:
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return []

        print(menu_con)
        opcion = mis_funciones.numero_opcion(6)

        # Mapeo de opción a continente (normalizado en minúsculas)
        continentes = {
            1: "américa del sur",
            2: "américa del norte",
            3: "europa",
            4: "áfrica",
            5: "asia",
            6: "oceanía"
        }

        continente_buscado = continentes.get(opcion, "").lower()
        if not continente_buscado:
            print("Opción de continente no válida.")
            return []

        resultados = []
        for pais in lista_paises:
            if not isinstance(pais, dict) or "continente" not in pais:
                continue  # Saltea entradas mal formadas
            if continente_buscado in pais["continente"].lower():
                resultados.append(pais)

        if not resultados:
            print("No se encontraron países para ese continente.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por continente: {e}")
        return []


def buscar_por_rango_poblacion(lista_paises):
    """
    Filtra países cuya población esté dentro de un rango dado por el usuario.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios con datos de países.
    
    Retorna:
        list: Países con población dentro del rango [mín, máx].
    """
    try:
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return []

        while True:
            try:
                n_min = int(mis_funciones.numero_entero("Ingrese el número mínimo de población: "))
                n_max = int(mis_funciones.numero_entero("Ingrese el número máximo de población: "))
                if n_min > n_max:
                    print("El valor mínimo no puede ser mayor que el máximo. Inténtelo de nuevo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese números enteros válidos.")

        resultados = []
        for pais in lista_paises:
            if not isinstance(pais, dict) or "poblacion" not in pais:
                continue
            try:
                if n_min <= int(pais["poblacion"]) <= n_max:
                    resultados.append(pais)
            except (ValueError, TypeError):
                # Saltea países con datos de población inválidos
                continue

        if not resultados:
            print("No se encontraron países en ese rango de población.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por rango de población: {e}")
        return []


def buscar_por_rango_superficie(lista_paises):
    """
    Filtra países cuya superficie (en km²) esté dentro de un rango dado.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios con datos de países.
    
    Retorna:
        list: Países con superficie dentro del rango [mín, máx].
    """
    try:
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return []

        while True:
            try:
                n_min = int(mis_funciones.numero_entero("Ingrese el número mínimo de superficie (km²): "))
                n_max = int(mis_funciones.numero_entero("Ingrese el número máximo de superficie (km²): "))
                if n_min > n_max:
                    print("El valor mínimo no puede ser mayor que el máximo. Inténtelo de nuevo.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese números enteros válidos.")

        resultados = []
        for pais in lista_paises:
            if not isinstance(pais, dict) or "superficie" not in pais:
                continue
            try:
                if n_min <= int(pais["superficie"]) <= n_max:
                    resultados.append(pais)
            except (ValueError, TypeError):
                # Saltea países con datos de superficie inválidos
                continue

        if not resultados:
            print("No se encontraron países en ese rango de superficie.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por rango de superficie: {e}")
        return []


def menu_de_filtros(lista_paises):
    """
    Menú interactivo que permite aplicar múltiples filtros en cadena.
    Cada filtro se aplica sobre el resultado del anterior.
    
    Parámetros:
        lista_paises (list): Lista original o ya filtrada de países.
    """
    try:
        paises_filtrados = lista_paises.copy()  # Trabaja sobre una copia para no modificar la original

        while True:
            print(menu_filtros)
            opcion = mis_funciones.numero_opcion(4)

            match opcion:
                case 1:
                    paises_filtrados = buscar_por_continente(paises_filtrados)
                case 2:
                    paises_filtrados = buscar_por_rango_poblacion(paises_filtrados)
                case 3:
                    paises_filtrados = buscar_por_rango_superficie(paises_filtrados)
                case 4:
                    if not paises_filtrados:
                        print("No hay países para mostrar.")
                    else:
                        # Formato legible para mostrar los países
                        for pais in paises_filtrados:
                            print(f"- {pais.get('nombre', 'Desconocido')}: "
                                f"Población={pais.get('poblacion', 'N/A')}, "
                                f"Superficie={pais.get('superficie', 'N/A')} km², "
                                f"Continente={pais.get('continente', 'N/A')}")
                    break  # Sale del menú de filtros después de mostrar
                case _:
                    print("Opción no válida.")
    except Exception as e:
        print(f"Error en el menú de filtros: {e}")