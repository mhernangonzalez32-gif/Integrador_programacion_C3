import mis_funciones
<<<<<<< HEAD
import filtro_de_busqueda
import busqueda_por_nombre
=======
#import pandas as pd
>>>>>>> 4035f803ac34cfe54ca27a213ba370a5989e116e


menu = ("------ Menu ------\n\n"
    "1. Buscar pais por nombre\n"
    "2. Filtro de paises\n"
    "3. Ordenar lista de paises\n"
    "4. Mostrar estadisticas\n"
    "5. Sair\n"
<<<<<<< HEAD
)

paises = mis_funciones.cargar_datos_desde_csv("paises_mundo.csv")

while True:
    print(menu)
    opcion = mis_funciones.numero_opcion(5)
    match opcion:
        case 1:
            nombre_pais = input("Que pais esta buscando?\n")
            print(busqueda_por_nombre.buscar_pais_nombre(paises, nombre_pais))
        case 2:
            filtro_de_busqueda.buscar_por_continente(paises)
=======
    #agregar paises
    #guardar modificaciones
)
opcion = 0

while opcion != 5:
    print(menu)
    opcion = input("Ingrese una opción: ")
    opcion_int = mis_funciones.verificar_num(opcion)
    match opcion_int:
        case 1:
            pass
        case 2:
            pass
>>>>>>> 4035f803ac34cfe54ca27a213ba370a5989e116e
        case 3:
            pass
        case 4:
            pass
<<<<<<< HEAD
        case 5:
            print("Adios")
=======

>>>>>>> 4035f803ac34cfe54ca27a213ba370a5989e116e
