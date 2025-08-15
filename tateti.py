from tablero import Tablero

class Tateti:
    def __init__(self):
        self.jugadores = ['X', 'O']
        self.turno = self.jugadores[0]
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fila, columna):
        jugador_actual = self.turno
        # Corrección: Se llama al método correcto 'poner_la_ficha'
        self.tablero.poner_la_ficha(fila, columna, jugador_actual)
        if not self.hay_ganador() and not self.hay_empate():
            self.cambiar_turno()

    def cambiar_turno(self):
        # Corrección: Se agrega el método para cambiar el turno.
        if self.turno == self.jugadores[0]:
            self.turno = self.jugadores[1]
        else:
            self.turno = self.jugadores[0]

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
