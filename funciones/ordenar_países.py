import funciones.mis_funciones as mis_funciones

# Menú visual para elegir el criterio de ordenamiento
menu_orden = (
    "Nombre",
    "Población",
    "Superficie"
)


def orden_paises(lista_paises):
    
    mis_funciones.limpiar_pantalla()
    
    """
    Permite al usuario ordenar la lista de países por nombre, población o superficie,
    en orden ascendente o descendente, y muestra los resultados formateados.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios, cada uno con claves:
        'nombre', 'poblacion', 'superficie', 'continente'.
    
    No retorna nada, pero imprime los países ordenados en consola.
    Si ocurre un error o no hay datos, muestra un mensaje informativo.
    """
    try:
        # Validación inicial de la entrada
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return

        if not lista_paises:
            print("No hay países para ordenar.")
            return
        
        print("=" * mis_funciones.ancho_total())
        print(mis_funciones.menu_centro("Ordenar países por:"))
        print("-" * mis_funciones.ancho_total())
        for i, opcion_texto in enumerate(menu_orden, start=1):
            linea = f"  {i}. {opcion_texto}"
            print(f"{linea:<{mis_funciones.ancho_total() - 6}}  ") 
        print("=" * mis_funciones.ancho_total())

        criterio = mis_funciones.numero_entero("Ingrese la opción de cómo desea ordenar: ")

        # Mapeo de opciones a claves del diccionario (¡corregido: 'superficie' en minúscula!)
        claves = {
            1 : 'nombre',
            2 : 'poblacion',
            3 : 'superficie'
        }
        
        if criterio not in claves:
            print("❌ Criterio de ordenamiento inválido.")
            return

        clave = claves[criterio]

        # Preguntar si desea orden descendente (True/False)
        descendente = mis_funciones.si_o_no(True, "¿Querés mostrarlo en orden descendente? (s/n): ")

        # Validar que todos los países tengan la clave necesaria y sean comparables
        # Convertimos a entero si es población o superficie (por si vienen como str del CSV)
        def obtener_valor(pais):
            if clave not in pais:
                return "" if clave == "nombre" else 0  # valor por defecto
            valor = pais[clave]
            if clave in ("poblacion", "superficie"):
                try:
                    return int(valor)
                except (ValueError, TypeError):
                    return 0
            return str(valor).lower()  # para nombre, orden alfabético

        # Ordenar usando la función auxiliar segura
        try:
            paises_ordenados = sorted(lista_paises, key=obtener_valor, reverse=descendente)
        except Exception as e:
            print(f"Error al ordenar los países: {e}")
            return

        # Mostrar resultados formateados
        if not paises_ordenados:
            print("No se pudieron mostrar países (lista vacía tras ordenar).")
            return

        print("\n" + "="*mis_funciones.ancho_total())
        print(mis_funciones.menu_centro(f"🌎 Países ordenados por {clave} ({'descendente' if descendente else 'ascendente'})"))
        print("="*mis_funciones.ancho_total())

        mis_funciones.imprimir_resultados(paises_ordenados)

    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado en el ordenamiento: {e}")
