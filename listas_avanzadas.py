# 1. Crear una funcion que devuelva la media de las notas
# 2. Crear una funcion que devuelva las notas suspendidas
# 3. Ordena la lista de notas de mayor a menor, sin modificar la lista original
notas = [7, 4, 10, 6, 8, 5, 9, 3, 7]

# 1. Crear una funcion que devuelva la media de las notas
def calcular_media(notas):
    return sum(notas) / len(notas) 

print(calcular_media(notas))

# 2. Crear una funcion que devuelva las notas suspendidas
def notas_suspendidas(notas):
    return [nota for nota in notas if nota < 5]

print(notas_suspendidas(notas))

# O tambien podria valer una forma mas clara y sencilla pero menos optima:
def notas_suspendidas_v2(notas):
    suspendidas = []
    for nota in notas:
        if nota < 5:
            suspendidas.append(nota)
    return suspendidas

print(notas_suspendidas_v2(notas))

# 3. Ordena la lista de notas de mayor a menor, sin modificar la lista original
def ordenar_notas_desc(notas):
    return sorted(notas, reverse=True)

print(ordenar_notas_desc(notas))

print(notas)