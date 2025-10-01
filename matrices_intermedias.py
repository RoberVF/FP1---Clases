tablero = [
    ["O", "O", "X"],
    ["O", " ", " "],
    ["O", " ", "X"]
]

def check_winner(tab):
    # Filas
    for fila in tab:
        if fila[0] == fila[1] == fila[2] != " ":
            return fila[0] # Devolvemos en simbolo ganador. Como los tres seran iguales, da igual cual devolver.
    
    # Columnas
    for columna in range(3):
        if tab[0][columna] == tab[1][columna] == tab[2][columna] != " ":
            return tab[0][columna]
    
    # Diagonales
    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        return tab[0][0]
    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return tab[0][2]
    
    return "Empate"

print("Ganador:", check_winner(tablero))
