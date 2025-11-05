# Cuantos numeros estan repetidos?

numeros = (1, 2, 3, 3, 3, 4, 5, 4, 5, 6)

cantidad_de_numeros_repetidos = 0
numeros_sin_repetir = []

for numero in numeros:
    if numero not in numeros_sin_repetir:
        numeros_sin_repetir.append(numero)
    else:
        cantidad_de_numeros_repetidos += 1

print(numeros_sin_repetir)
print(cantidad_de_numeros_repetidos)