estudiante = ("Andrea", 22, 8.5)

# if estudiante[1] > 5:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

for dato in estudiante:
    print(f"El dato es {dato}")

for dato in range(len(estudiante)):
    print(f"El dato en la posicion {dato} es {estudiante[dato]}")
