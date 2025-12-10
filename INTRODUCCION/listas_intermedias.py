notas = [4.5, 6.0, 8.2, 9.5, 3.7, 7.0]

# Podemos sumar los elementos de una lista de estas dos maneras:
# sumatorio_de_notas = sum(notas)
# print("La suma total de las notas es:", sumatorio_de_notas)

sumatorio_de_notas_2 = 0
# for i in notas:
#     # sumatorio_de_notas_2 += i
#     sumatorio_de_notas_2 = sumatorio_de_notas_2 + i
# print("La suma total de las notas es:", sumatorio_de_notas_2)

# for i in range(len(notas)):
    # sumatorio_de_notas_2 = sumatorio_de_notas_2 + notas[i]
# print("La suma total de las notas es:", sumatorio_de_notas_2)


# Podemos crear una nueva lista con los elementos que cumplan una condición:
aprobados = [n for n in notas if n >= 5.0] # Recorremos y aplicamos la condicion

# Aunque se podria hacer con un bucle for, es mas largo:
aprobados_2 = []
for i in notas:
    if i >= 5.0:
        aprobados_2.append(i)

aprobados.sort(reverse=True) # Asi los ordenamos de mayor a menor
print("Aprobados:", aprobados)
