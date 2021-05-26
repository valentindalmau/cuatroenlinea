def tablero_vacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]


# Esta función devuelve un tablero de 6 filas y 7 columnas, en donde todos los valores son 0
# tablero=[fila][columna]
def contenido_columna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna-1]
        columna.append(celda)
    return columna
def contenido_fila(nro_fila, tablero):
    fila = []
    for columna in tablero[nro_fila-1]:
        fila.append(columna)
    return fila
def devolver_todas_las_columnas(tablero):
    columnas = []
    for columna in range(1,8):
        columnas.append(contenido_columna(columna,tablero))
    return columnas
def devolver_todas_las_filas(tablero):
    filas = []
    for fila in tablero:
        filas.append(fila)
    return filas

def secuencia_correcta(secuencia):
    c = 0
    while c < len(secuencia):
        if (secuencia[c] > 7 or secuencia[c] < 1):
            return 1
        c += 1
    return 0


# Esta función toma la secuencia y se fija si todos sus valores están entre 1 y 7
# En ese caso devuelve 0, caso contrario devuelve 1

def soltar_ficha_en_tablero(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if (tablero[fila - 1][columna - 1] == 0):
            tablero[fila - 1][columna - 1] = ficha
            return


# Esta función tiene 3 parámetros, la ficha, que sera 1 o 2 dependiendo del jugador,
# la columna que sera la secuencia, y finalmente el tablero.
# Está diseñada para que la ficha "caiga" en la última fila vacía (con un 0)
# para eso, se fija de abajo hacia arriba hasta encontrar una posición vacía
# y termina la funcion posicionando la ficha en dicha posición.

def completar_tablero_en_orden(secuencia, tablero):
    c = 0
    while (c < len(secuencia)):
        if (c % 2 == 0):
            soltar_ficha_en_tablero(1, secuencia[c], tablero)
        else:
            soltar_ficha_en_tablero(2, secuencia[c], tablero)

        c += 1
    return


# En esta función se determina si la ficha será un 1 o un 2, dependiendo del jugador

def dibujar_tablero(tablero):
    print("+---------------+")
    for fila in tablero:
        print("|", end=" ")
        for celda in fila:
            if celda == 0:
                print("0", end = " ")
            else:
                print("%s" % celda, end = " ")
        print("|")
    print("+---------------+")

    return


# Esta función dibuja el tablero en la terminal con bordes, imprimiendo fila a fila
# y celda a celda en un for adentro de un for

secuencia_texto = input("introduzca la secuencia: ")
secuencia = []
for items in secuencia_texto.split(','):
    secuencia.append(int(items))
tablero = tablero_vacio()
if (secuencia_correcta(secuencia) == 0):
    completar_tablero_en_orden(secuencia, tablero)
    dibujar_tablero(tablero)
else:
    print(f'La secuencia es incorrecta, ingrese valores entre 1 y 7')
print(contenido_columna(2,tablero))
print(contenido_fila(1, tablero))
print(devolver_todas_las_columnas(tablero))
print(devolver_todas_las_filas(tablero))