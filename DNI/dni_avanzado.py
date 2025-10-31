import string_utils

datos = {
    "11111111": "Mati",
    "12345678": "Rober",
}

string_utils.change_dict(datos)

name_list = []
dni_full_list = []
dni_full_name_list = []

for key, value in datos.items():
    dni_full, name = value

    name_list.append(name)
    dni_full_list.append(dni_full)
    dni_full_name_list.append((dni_full, name))

print("Los nombres que aparecen son:", name_list)
print("Los DNIs completos son:", dni_full_list)
print("Los DNIs completos junto con los nombres son:", dni_full_name_list)