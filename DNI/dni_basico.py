import string_utils

datos = {
    "11111111": "Mati",
    "12345678": "Rober",
}

print("Dic sin alterar:", datos)

string_utils.change_dict(datos)

print("Dic alterado:", datos)
