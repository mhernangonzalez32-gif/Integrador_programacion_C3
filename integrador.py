import mis_funciones
import filtro_de_busqueda
import busqueda_por_nombre



with open('paises_mundo.csv', 'w', newline="") as archivo:
    escritor = csv.writer(archivo)
    
menu = ("------ Menu ------\n\n"
    "1. Buscar pais por nombre\n"
    "2. Filtro de paises\n"
    "3. Ordenar lista de paises\n"
    "4. Mostrar estadisticas\n"
    "5. Sair\n")

paises = mis_funciones.cargar_datos_desde_csv("paises_mundo.csv")

while True:
    print(menu)
    opcion = mis_funciones.numero_opcion(5)
    match opcion:
        case 1:
            nombre_pais = input("Que pais esta buscando?\n")
            print(busqueda_por_nombre.buscar_pais_nombre(paises, nombre_pais))
        case 2:
            filtro_de_busqueda.menu_de_filtros(paises)
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Adios")
