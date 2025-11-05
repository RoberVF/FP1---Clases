# Calcular y estructurar las ventas anuales que ha tenido cada vendedor
# Cada fila de la matriz sera un vendedor y cada columna un trimestre

ventas = [
    [213, 421, 463, 535],
    [241, 275, 967, 942],
    [634, 632, 754, 214]
]

ventas_estructuradas = {}

for i in range(len(ventas)):
    ventas_vendedor = ventas[i] 
    total_ventas_anual_vendedor = sum(ventas_vendedor)

    # Para el diccionario
    clave_vendedor = f"vendedor_{i}"
    ventas_estructuradas[clave_vendedor] = total_ventas_anual_vendedor

print(ventas_estructuradas)


