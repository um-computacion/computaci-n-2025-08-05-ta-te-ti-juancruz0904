import unittest
from tablero import Tablero, PosOcupadaException


class TestTablero(unittest.TestCase):

    def setUp(self):
        # Iniciar un nuevo objeto Tablero antes de cada prueba.
        self.tablero = Tablero()

    def test_poner_ficha_en_posicion_vacia(self):
        # Verifica que se puede poner una ficha en una posición vacía.
        self.tablero.poner_la_ficha(0, 0, 'X')
        self.assertEqual(self.tablero.contenedor[0][0], 'X')

    def test_poner_ficha_en_posicion_vacia_con_O(self):
        # Verifica que se puede poner una ficha en una posición vacía.
        self.tablero.poner_la_ficha(1, 1, 'O')
        self.assertEqual(self.tablero.contenedor[1][1], 'O')

    def test_poner_ficha_en_posicion_ocupada_lanza_excepcion(self):
        # Verifica que se usa PosOcupadaException al poner una ficha en una posición ocupada.
        # Coloca una ficha 'X' primero
        self.tablero.poner_la_ficha(0, 0, 'X')

        # Intenta colocar otra ficha 'O' en la misma posición y verifica la excepción
        with self.assertRaises(PosOcupadaException) as context:
            self.tablero.poner_la_ficha(0, 0, 'O')

        self.assertEqual(str(context.exception), "pos ocupada!")

    def test_el_tablero_se_inicia_vacio(self):
        # Verifica que el tablero está vacío al iniciar.
        for fila in self.tablero.contenedor:
            for casilla in fila:
                self.assertEqual(casilla, "")


if __name__ == '__main__':
    unittest.main()