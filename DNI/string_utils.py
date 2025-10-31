import auxiliar

def change_dict(dnis_dict: dict):

    for key, value in dnis_dict.items():
        dnis_dict[key] = (auxiliar.add_letter(key), value)

# Dejando la key como referencia, hace una tupla para cada key tipo key: (key con letra, nombre)