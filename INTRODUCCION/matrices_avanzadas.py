# 1. Calcula la suma de cada fila y devuelve una lista con esas sumas
# 2. Calcula la suma de cada columna y devuelve otra lista con esas sumas

tablero = [
    [3, 5, 1, 2],
    [7, 4, 6, 8],
    [9, 0, 2, 3],
    [5, 6, 1, 4]
]

# 1. Calcula la suma de cada fila y devuelve una lista con esas sumas.
def suma_filas(tablero):
    sumas = []
    for i in range(len(tablero)):
        sumas.append(sum(tablero[i]))
    return sumas

print(suma_filas(tablero))

# 2. Calcula la suma de cada columna y devuelve otra lista con esas sumas
def suma_columnas(tablero):
    sumas = []
    for j in range(len(tablero[0])):
        suma_columna = 0
        for i in range(len(tablero)):
            suma_columna += tablero[i][j]
        sumas.append(suma_columna)
    return sumas

print(suma_columnas(tablero))