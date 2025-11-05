# Hacer una media entre las ventas de los vendedores por trimestres
# Cada fila de la matriz sera un vendedor y cada columna un trimestre

ventas = [
    [213, 421, 463, 535],
    [241, 275, 967, 942],
    [634, 632, 754, 214]
]

ventas_por_trimestres = {}

numero_vendedores = len(ventas)

numero_trimestres = len(ventas[0])

for trimestre in range(numero_trimestres):
    ventas_por_trimestre = 0
    
    for vendedor in range(numero_vendedores):
        ventas_por_trimestre += ventas[vendedor][trimestre]
        
    media_ventas_trimestre = ventas_por_trimestre / numero_trimestres
    
    # Para el diccionario:
    key_trimestre = f"Trimestre_{trimestre + 1}"
    ventas_por_trimestres[key_trimestre] = media_ventas_trimestre
    
print(ventas_por_trimestres)
