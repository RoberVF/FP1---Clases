matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])  # segunda fila, tercera columna → 6

matriz[1][1] = 0     # cambiar el 5 por 0

for fila in matriz:
    print(fila)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"El elemento en la posicion [{i}][{j}] es {matriz[i][j]}")