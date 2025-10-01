puntos = [(2, 3), (5, -1), (0, 0), (-3, 4)] # Lista de tuplas
sumas = []


# Podemos printear los elementos de la lista, aunque sean tuplas, de estas dos maneras:
# for punto in puntos:
#     for i in range(len(punto)):
#         print(punto[i])

# for x, y in puntos:
    # print(f"Punto en ({x}, {y})")

# Tambien podemos trabajar con los elementos de las tuplas dentro de la lista:
for x, y in puntos:
    suma = x + y
    sumas.append(suma)

print("Suma de los elementos de la tupla:", sumas)
print(sum(sumas))  # Suma de la primera y tercera tupla
print(max(sumas))  # Maximo de la segunda y cuarta tupla
print(min(sumas))  # Minimo de la segunda y cuarta tupla