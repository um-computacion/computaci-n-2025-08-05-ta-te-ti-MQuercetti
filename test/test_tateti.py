import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from player import Player
from tateti import Tateti
import unittest

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("A", "X")
        self.p2 = Player("B", "O")
        self.game = Tateti(self.p1, self.p2)

    def test_turn_change(self):
        self.assertEqual(self.game.turn, 0)
        self.game.cambiar_turno()
        self.assertEqual(self.game.turn, 1)
        self.game.cambiar_turno()
        self.assertEqual(self.game.turn, 0)

    def test_jugar(self):
        result = self.game.jugar(0, "X")
        self.assertTrue(result)
        self.assertEqual(self.game.tablero.casillas[0], "X")
        result2 = self.game.jugar(0, "O")
        self.assertFalse(result2)

if __name__ == "__main__":
    unittest.main()