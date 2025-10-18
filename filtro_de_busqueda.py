import mis_funciones

menu_con = ("Elije algun continente\n"
    "1. América del Sur\n"
    "2. América del norte\n"
    "3. Europa\n"
    "4. África\n"
    "5. Asia\n"
    "6. Oceanía\n")
n_min = "a"
n_max = "a"



def buscar_por_continente(lista_paises):
    print(menu_con)
    opcion = mis_funciones.numero_opcion(6)
    match opcion:
        case 1:
            continente = "américa del sur"
        case 2:
            continente = "américa del norte"
        case 3:
            continente = "europa"
        case 4:
            continente = "áfrica"
        case 5:
            continente = "asia"
        case 6:
            continente = "oceanía"
    resutados = []
    for pais in lista_paises:
        if continente in pais["continente"].lower():
            resutados.append(pais)
    return print(resutados)

