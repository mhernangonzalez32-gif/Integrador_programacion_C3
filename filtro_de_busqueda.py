import mis_funciones

menu_con = (
    "Elije algun continente\n"
    "1. América del Sur\n"
    "2. América del norte\n"
    "3. Europa\n"
    "4. África\n"
    "5. Asia\n"
    "6. Oceanía\n"
    )
menu_filtros = (
    "Que tipo de filtros desea usar:\n"
    "1. Buscar por continente \n"
    "2. Buscar por rango de pobación \n"
    "3. Buscar por rango de superficie \n"
    "4. Mostrar lista"
)

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
    return resutados

def buscar_por_rango_poblacion(lista_paises):
    resutados = []
    while True:
        n_min = int(mis_funciones.numero_entero("Ingrese el numero minimo: "))
        n_max = int(mis_funciones.numero_entero("Ingrese el numero maximo: "))
        if n_min > n_max:
            print("Los datos no coinciden. El mínimo no puede ser mayor al máximo.")
        else:
            break
    for pais in lista_paises:
        if n_min <= pais["poblacion"] <= n_max:
            resutados.append(pais)
    return resutados

def buscar_por_rango_superficie(lista_paises):
    resutados = []
    while True:
        n_min = int(mis_funciones.numero_entero("Ingrese el numero minimo: "))
        n_max = int(mis_funciones.numero_entero("Ingrese el numero maximo: "))
        if n_min > n_max:
            print("Los datos no coinciden. El mínimo no puede ser mayor al máximo.")
        else:
            break
    for pais in lista_paises:
        if n_min <= pais["superficie"] <= n_max:
            resutados.append(pais)
    return resutados

def menu_de_filtros(lista_paises):
    paises_fitrados = lista_paises
    while True:
        print(menu_filtros)
        opcion = mis_funciones.numero_opcion(4)
        match opcion:
            case 1:
                paises_fitrados = buscar_por_continente(paises_fitrados)
            case 2:
                paises_fitrados = buscar_por_rango_poblacion(paises_fitrados)
            case 3:
                paises_fitrados = buscar_por_rango_superficie(paises_fitrados)
            case 4:
                print(paises_fitrados)

