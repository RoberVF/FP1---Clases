# 1. Calcular el salario medio de cada departamento.
# 2. Diccionario con clave: departamento, valor: lista con los empleados de ese departamento
# 3. Imprimir los empleados que ganas mas que la media de su departamento.

empleados = [
    ("Ana", "Ventas", 2500),
    ("Luis", "IT", 3200),
    ("Marta", "IT", 2800),
    ("Juan", "Ventas", 3000),
    ("Sofía", "Marketing", 2700)
]

# 1. Calcular el salario medio de cada departamento.

# En primer lugar, tenemos que sacar los departamentos pero sin que se repitan los duplicados:
departamentos = []
for x,y,z in empleados:
    if y not in departamentos:
        departamentos.append(y)
print("Departamentos:", departamentos)

# Ahora, para cada departamento, sacamos el valor medio de sus salarios:
medias = []

for departamento in departamentos:
    suma_salarios = 0
    contador = 0
    for nombre, depto, salario in empleados:
        if depto == departamento:
            suma_salarios += salario
            contador += 1
    media = suma_salarios / contador
    medias.append((departamento, media))

print("Media de salarios por departamento:", medias)


# 2. Diccionario con clave: departamento, valor: lista con los empleados de ese departamento
empleados_dep = {}
for nombre, dep, salario in empleados:
    if dep not in empleados_dep:
        empleados_dep[dep] = []
    empleados_dep[dep].append(nombre)
    
print(empleados_dep)


# 3. Imprimir los empleados que ganas mas que la media de su departamento.
for nombre, dep, salario in empleados:
    # Buscamos la media del departamento del empleado
    media_dep = 0
    for d, media in medias:
        if d == dep:
            media_dep = media
    # Comparamos salario con la media
    if salario > media_dep:
        print(f"{nombre} ({dep}) → {salario}")