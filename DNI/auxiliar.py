def add_letter(number):

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni_letter = letters[int(number) % 23]

    return number + dni_letter


# Una vez se le da la entrada (number) siempre dara la misma salida, sin efectos secundarios.