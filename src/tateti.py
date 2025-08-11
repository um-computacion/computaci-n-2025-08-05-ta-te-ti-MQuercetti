from tablero import Tablero

class Tateti:
    def __init__(self, player1, player2):
        self.turn = 0
        self.tablero = Tablero()

    def cambiar_turno(self):
        self.turn = 1 if self.turn == 0 else 0

    def jugar(self, posicion, symbol):
        return self.tablero.play(posicion, symbol)