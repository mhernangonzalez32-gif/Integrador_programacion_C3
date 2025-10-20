import mis_funciones


menu_orden = (
    "Ordenar países por:"
    " A. Nombre "
    " B. Población "
    " C. Superficie "
    )


def orden_paises(lista_paises, criterio, desendente = False):

    print(menu_orden)
    criterio = input('Ingrese la opcion de como desea ordenar?').strip().lower()
    claves = {'a':'nombre', 'b':'poblacion', 'c':'Superficie'}
    if criterio not in claves:
        print('Criterio de ordenamiento invalido')
        return lista_paises
    clave = claves[criterio]
    for pais in sorted(lista_paises, key=lambda x: x[clave], reverse=desendente):    
        print(f"🌍 {pais['nombre']}")
        print(f"   Población : {pais['poblacion']:,}, {pais['superficie']:,} km², {pais['continente']}")
        print("-" * 40)

    #return sorted(lista_paises, key=lambda x: x[clave], reverse=desendente)
    

    