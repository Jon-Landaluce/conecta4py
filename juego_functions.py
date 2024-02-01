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

def esta_llena(tab,columna):
    
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
    