import funciones.mis_funciones as mis_funciones
import funciones.filtro_de_busqueda as filtro_de_busqueda
import funciones.busqueda_por_nombre as busqueda_por_nombre
import funciones.ordenar_países as ordenar_países
import funciones.mostrar_estadísticas as mostrar_estadísticas


paises = mis_funciones.cargar_datos_desde_csv("csv\\paises_mundo.csv")

while True:
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
            pass
        case 6:
            pass
        case 7:
            print("Adios")
            break