from tateti import Tateti
from tablero import PosOcupadaException

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    while True:
        print("Tablero: ")
        # Lógica para dibujar el tablero
        print("-------------")
        for i, row in enumerate(juego.tablero.contenedor):
            print(f"| {row[0] if row[0] else ' '} | {row[1] if row[1] else ' '} | {row[2] if row[2] else ' '} |")
            print("-------------")

        # Lógica para verificar ganador o empate
        if juego.hay_ganador():
            print(f"¡El jugador {juego.turno} ha ganado!")
            break

        if juego.hay_empate():
            print("¡Empate! El juego ha terminado.")
            break

        print(f"Turno: {juego.turno}")
        try:
            # Lógica para manejar la entrada del usuario
            fila_str = input("Ingrese fila (0, 1, 2): ")
            col_str = input("Ingrese col (0, 1, 2): ")

            # Validación de entrada
            if not fila_str.isdigit() or not col_str.isdigit():
                print("Error: Por favor, ingrese un número válido.")
                continue

            fil = int(fila_str)
            col = int(col_str)

            if not (0 <= fil <= 2 and 0 <= col <= 2):
                print("Error: Fila o columna fuera de rango. Inténtelo de nuevo.")
                continue

            juego.ocupar_una_de_las_casillas(fil, col)
        except PosOcupadaException as e:
            print(e)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()