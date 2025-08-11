from tateti import Tateti
from player import Player

def mostrar_tablero(casillas):
    for i in range(3):
        fila = casillas[i*3:(i+1)*3]
        print(" | ".join(fila))
        if i < 2:
            print("--+---+--")

def hay_ganador(casillas):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]           
    ]
    for combo in combinaciones:
        a, b, c = combo
        if casillas[a] != " " and casillas[a] == casillas[b] == casillas[c]:
            return casillas[a]
    return None

def mostrar_puntajes(player1, player2):
    print(f"Puntaje {player1.name}: {player1.score}")
    print(f"Puntaje {player2.name}: {player2.score}")

def main():
    print("Bienvenidos al Tateti")
    player1 = Player("Jugador 1", "X")
    player2 = Player("Jugador 2", "O")
    juego = Tateti(player1, player2)
    while True:
        print("\nTablero:")
        mostrar_tablero(juego.tablero.casillas)
        print(f"Turno de: {player1.name if juego.turn == 0 else player2.name}")
        try:
            fil = int(input("Ingrese fila (0, 1 o 2): "))
            col = int(input("Ingrese columna (0, 1 o 2): "))
            if fil not in [0,1,2] or col not in [0,1,2]:
                print("Fila y columna deben ser 0, 1 o 2.")
                continue
            posicion = fil * 3 + col
            symbol = player1.symbol if juego.turn == 0 else player2.symbol
            if juego.jugar(posicion, symbol):
                ganador = hay_ganador(juego.tablero.casillas)
                if ganador:
                    mostrar_tablero(juego.tablero.casillas)
                    if ganador == player1.symbol:
                        print(f"¡Ganó {player1.name}!")
                        player1.score += 1
                    else:
                        print(f"¡Ganó {player2.name}!")
                        player2.score += 1
                    mostrar_puntajes(player1, player2)
                    juego.tablero.reset()
                    juego.turn = 0
                    continue
                elif " " not in juego.tablero.casillas:
                    mostrar_tablero(juego.tablero.casillas)
                    print("¡Empate!")
                    mostrar_puntajes(player1, player2)
                    juego.tablero.reset()
                    juego.turn = 0
                    continue
                juego.cambiar_turno()
            else:
                print("Casilla ocupada, intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()