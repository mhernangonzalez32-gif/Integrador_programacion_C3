import mis_funciones
#import pandas as pd


menu = ("------ Menu ------\n\n"
    "1. Buscar pais por nombre\n"
    "2. Filtro de paises\n"
    "3. Ordenar lista de paises\n"
    "4. Mostrar estadisticas\n"
    "5. Sair\n"
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
        case 3:
            pass
        case 4:
            pass

