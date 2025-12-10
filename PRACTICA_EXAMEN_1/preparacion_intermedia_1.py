# Cuantos y cuales son los nombres con MAS de 4 letras?

nombres = ["Rober", "Mati", "Alberto", "Santi"]

nombres_mayores_de_cuatro_letras = []
cuantos_nombres_tienen_mas_de_cuatro_letras = 0

for nombre in nombres:
    if(len(nombre) >= 5):
        nombres_mayores_de_cuatro_letras.append(nombre)
        cuantos_nombres_tienen_mas_de_cuatro_letras += 1

print(nombres_mayores_de_cuatro_letras)

# Podemos saber cuantos nombres tienen mas de 4 letras midiendo el tamanio de la lista o con un contador
print(cuantos_nombres_tienen_mas_de_cuatro_letras)
print(len(nombres_mayores_de_cuatro_letras))