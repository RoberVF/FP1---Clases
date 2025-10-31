import string_utils

datos = {
    "11111111": "Mati",
    "12345678": "Rober",
}

string_utils.change_dict(datos)

for dni_num, valor_tupla in datos.items():
    dni_full, name = valor_tupla
    dni_letter = dni_full[-1]

    print(f"Para el DNI {dni_num} con letra {dni_letter} (quedando el dni completo como {dni_full}), el nombre es {name}.")
