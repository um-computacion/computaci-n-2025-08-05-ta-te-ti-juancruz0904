from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno)

        # Change the turn only if the move was successful
        if not self.hay_ganador() and not self.hay_empate():
            if self.turno == "X":
                self.turno = "0"
            else:
                self.turno = "X"

    def hay_ganador(self):
        # Check rows
        for row in self.tablero.contenedor:
            if row[0] == row[1] == row[2] and row[0] != "":
                return True

        # Check columns
        for col in range(3):
            if self.tablero.contenedor[0][col] == self.tablero.contenedor[1][col] == self.tablero.contenedor[2][col] and \
                    self.tablero.contenedor[0][col] != "":
                return True

        # Check diagonals
        if self.tablero.contenedor[0][0] == self.tablero.contenedor[1][1] == self.tablero.contenedor[2][2] and \
                self.tablero.contenedor[0][0] != "":
            return True

        if self.tablero.contenedor[0][2] == self.tablero.contenedor[1][1] == self.tablero.contenedor[2][0] and \
                self.tablero.contenedor[0][2] != "":
            return True

        return False

    def hay_empate(self):
        for row in self.tablero.contenedor:
            for cell in row:
                if cell == "":
                    return False
        return not self.hay_ganador()