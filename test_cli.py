import unittest
from tateti import Tateti
from tablero import PosOcupadaException, Tablero

class TestTateti(unittest.TestCase):

    def setUp(self):
        # Se prepara un nuevo juego en el Tateti antes de cada prueba.
        self.juego = Tateti()

    def test_inicializacion_juego(self):
        # Verifica que el juego se inicia correctamente.
        self.assertIsInstance(self.juego, Tateti)
        self.assertIsInstance(self.juego.tablero, Tablero)
        self.assertEqual(self.juego.turno, 'X')
        self.assertEqual(self.juego.jugadores, ['X', 'O'])

    def test_ocupar_casilla_valida(self):
        # Verifica que se puede ocupar una casilla vacía.
        self.juego.ocupar_una_de_las_casillas(0, 0)
        # Corrección: Acceso directo a la matriz del tablero.
        self.assertEqual(self.juego.tablero.contenedor[0][0], 'X')
        self.assertEqual(self.juego.turno, 'O')

    def test_ocupar_casilla_ocupada_lanza_excepcion(self):
        # Verifica que se usa PosOcupadaException al ocupar una casilla que ya esta ocupada.
        self.juego.ocupar_una_de_las_casillas(1, 1)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(1, 1)

    def test_cambio_de_turno(self):
        # Verifica que el turno cambia correctamente entre jugadores.
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, 'O')
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, 'X')

    def test_victoria_en_fila(self):
        # Verifica que se detecta la victoria en una fila.
        self.juego.ocupar_una_de_las_casillas(0, 0) # X
        self.juego.ocupar_una_de_las_casillas(1, 0) # O
        self.juego.ocupar_una_de_las_casillas(0, 1) # X
        self.juego.ocupar_una_de_las_casillas(2, 0) # O
        self.juego.ocupar_una_de_las_casillas(0, 2) # X
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.turno, 'X') # El turno del ganador se mantiene

    def test_victoria_en_columna(self):
        # Verifica que se detecta la victoria en una columna.
        self.juego.ocupar_una_de_las_casillas(0, 0) # X
        self.juego.ocupar_una_de_las_casillas(0, 1) # O
        self.juego.ocupar_una_de_las_casillas(1, 0) # X
        self.juego.ocupar_una_de_las_casillas(1, 1) # O
        self.juego.ocupar_una_de_las_casillas(2, 0) # X
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.turno, 'X')

    def test_victoria_en_diagonal_principal(self):
        # Verifica que se detecta la victoria en la diagonal principal.
        self.juego.ocupar_una_de_las_casillas(0, 0) # X
        self.juego.ocupar_una_de_las_casillas(0, 1) # O
        self.juego.ocupar_una_de_las_casillas(1, 1) # X
        self.juego.ocupar_una_de_las_casillas(0, 2) # O
        self.juego.ocupar_una_de_las_casillas(2, 2) # X
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.turno, 'X')

    def test_victoria_en_diagonal_secundaria(self):
        # Verifica que se detecta la victoria en la diagonal secundaria.
        self.juego.ocupar_una_de_las_casillas(0, 2) # X
        self.juego.ocupar_una_de_las_casillas(0, 0) # O
        self.juego.ocupar_una_de_las_casillas(1, 1) # X
        self.juego.ocupar_una_de_las_casillas(1, 0) # O
        self.juego.ocupar_una_de_las_casillas(2, 0) # X
        self.assertTrue(self.juego.hay_ganador())
        self.assertEqual(self.juego.turno, 'X')

    def test_empate(self):
        # Verifica que se detecta un empate cuando no hay casillas libres ni ganador.
        self.juego.ocupar_una_de_las_casillas(0, 0) # X
        self.juego.ocupar_una_de_las_casillas(0, 1) # O
        self.juego.ocupar_una_de_las_casillas(0, 2) # X
        self.juego.ocupar_una_de_las_casillas(1, 1) # O
        self.juego.ocupar_una_de_las_casillas(1, 0) # X
        self.juego.ocupar_una_de_las_casillas(1, 2) # O
        self.juego.ocupar_una_de_las_casillas(2, 1) # X
        self.juego.ocupar_una_de_las_casillas(2, 0) # O
        self.juego.ocupar_una_de_las_casillas(2, 2) # X
        self.assertFalse(self.juego.hay_ganador())
        self.assertTrue(self.juego.hay_empate())

    def test_juego_no_terminado_sin_ganador_ni_empate(self):
        # Verifica que el juego no se marca como terminado em algun momento.
        self.juego.ocupar_una_de_las_casillas(0, 0) # X
        self.juego.ocupar_una_de_las_casillas(1, 1) # O
        self.assertFalse(self.juego.hay_ganador())
        self.assertFalse(self.juego.hay_empate())

if __name__ == '__main__':
    unittest.main()