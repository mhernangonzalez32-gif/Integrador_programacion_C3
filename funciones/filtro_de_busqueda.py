import funciones.mis_funciones as mis_funciones

def buscar_por_continente(lista_paises):
    try:
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return []
        mis_funciones.menu_con()
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
        mis_funciones.imprimir_resutados(resultados)

        if not resultados:
            print("No se encontraron países para ese continente.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por continente: {e}")
        return []


def buscar_por_rango_poblacion(lista_paises):
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
        mis_funciones.imprimir_resutados(resultados)

        if not resultados:
            print("No se encontraron países en ese rango de población.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por rango de población: {e}")
        return []


def buscar_por_rango_superficie(lista_paises):
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
        mis_funciones.imprimir_resutados(resultados)

        if not resultados:
            print("No se encontraron países en ese rango de superficie.")
        return resultados

    except Exception as e:
        print(f"Error en la búsqueda por rango de superficie: {e}")
        return []


def menu_de_filtros(lista_paises):
    try:
        paises_filtrados = lista_paises.copy()  # Trabaja sobre una copia para no modificar la original

        while True:
            mis_funciones.menu_filtros()
            opcion = mis_funciones.numero_opcion(4)

            match opcion:
                case 1:
                    paises_filtrados = buscar_por_continente(paises_filtrados)
                case 2:
                    paises_filtrados = buscar_por_rango_poblacion(paises_filtrados)
                case 3:
                    paises_filtrados = buscar_por_rango_superficie(paises_filtrados)
                case 4:
                    break
                case _:
                    print("Opción no válida.")
    except Exception as e:
        print(f"Error en el menú de filtros: {e}")