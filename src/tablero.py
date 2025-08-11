class Tablero:
    def __init__(self, player1=None, player2=None):
        self.casillas = [" " for _ in range(9)] 
        self.player1 = player1                   
        self.player2 = player2                   

    def play(self, posicion, symbol):
        if self.casillas[posicion] == " ":
            self.casillas[posicion] = symbol
            return True
        else:
            return False 

    def reset(self):
        self.casillas = [" " for _ in range(9)]