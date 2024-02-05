def crea_tablero(fila, columna):

    salida = []

    for element in range(columna):

        lista2 = []

        for i in range(fila):

            lista2.append(0)

        salida.append(lista2)
    return salida


def juega(tablero, columna, valor_ficha):
    '''

    # elegir la columna

    c = tablero[2]

    indice = len(c) - 1

    # recorro la columna de atras a adelante

    for hueco in c[::-1]:

    # al encontrar el primer cero, lo sustituyo por valor ficha

        if hueco == 0:

            c[indice] = valor_ficha

            break

        indice -= 1


    for indice in range(len(c)-1, -1, -1):

        if c[indice] == 0

            c[indice] == valor_ficha

            break

    '''

    c = tablero[columna]

    indice = len(c) - 1

    while indice >= 0:

        if c[indice] == 0:

            c[indice] = valor_ficha

            break

        indice -= 1


def esta_llena(tab, columna):

    # seleccionar columna que queremos comprobar (columna)

    # comprobar si la columna tiene huecos con un in

    # o recprrer la columna posicion a posicion con un bucle

    c = tab[columna]

    '''

    if 0 not in c:

        return True
    
    else:

        return False

    '''

    return 0 not in c


def victoria_vertical_col(tablero, pos_columna, valor_ficha):

    contador_iguales = 0

    columna = tablero[pos_columna]

    indice = 0

    while indice < len(columna):

        if columna[indice] == valor_ficha:

            contador_iguales += 1
        else:

            contador_iguales = 0

        if contador_iguales == 4:

            return True

        indice += 1

    return False


def victoria(tablero, valor_ficha):
    '''
    Obtener el numero de columnas de mi tablero
    Iterar sobre range(num_columnas)
        para cada columna si es True devolver True
        si es False pasar a la siguiente

    Si salgo del bucle, devolver False
    '''

    num_columnas = len(tablero)
    for num_col in range(num_columnas):
        if victoria_vertical_col(tablero, num_col, valor_ficha):
            return True

    '''
    Obtener el numero de filas
    iterar sobre range(num_filas)
        para cada fila si la victoria_horizontal es True, devuelvo True
        sigo con otro caso

    Si salgo del bucle devolver false
    '''

    num_filas = len(tablero[0])
    for num_fila in range(num_filas):
        if victoria_horizontal_fila(tablero, num_fila, valor_ficha):
            return True


    return False

def victoria_horizontal_fila(tab, pos_fila, valor_ficha):
    
    contador_iguales = 0
    
    for columna in tab:
        if columna[pos_fila] == valor_ficha:
            contador_iguales += 1
        else:
            contador_iguales = 0
        if contador_iguales == 4:
            return True

    return False




