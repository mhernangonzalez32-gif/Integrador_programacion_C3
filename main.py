from funciones import (
    mis_funciones,
    filtro_de_busqueda,
    busqueda_por_nombre,
    ordenar_países,
    mostrar_estadísticas,
    manejo_csv
)


paises = mis_funciones.cargar_datos_desde_csv("csv\\paises_mundo.csv")

while True:
    mis_funciones.inicializar_archivo()
    mis_funciones.menu_principal()
    opcion = mis_funciones.numero_opcion(7)
    match opcion:
        case 1:
            busqueda_por_nombre.buscar_pais_nombre(paises)
        case 2:
            filtro_de_busqueda.menu_de_filtros(paises)
        case 3: 
            ordenar_países.orden_paises(paises)
        case 4:
            mostrar_estadísticas.mostrar_estadisticas(paises)
        case 5:
            manejo_csv.agregar_pais(paises, "csv\\paises_mundo.csv")
        case 6:
            manejo_csv.editar_pais(paises, manejo_csv.encabezados, "csv\\paises_mundo.csv")
        case 7:
            print("Adiós")
        case _:
            print (mis_funciones.menu_centro("🤭 Error. Intentelo nuevamente.🤭"))