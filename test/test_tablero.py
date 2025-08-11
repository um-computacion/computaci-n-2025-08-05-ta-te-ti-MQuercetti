import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from tablero import Tablero
import unittest

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
    
    def test_tablero_init(self):
        self.assertEqual(self.tablero.casillas, [" "] * 9)
    
    def test_play_valid(self):
        result = self.tablero.play(0, "X")
        self.assertTrue(result)
        self.assertEqual(self.tablero.casillas[0], "X")
    
    def test_play_invalid(self):
        self.tablero.casillas[1] = "O"
        result = self.tablero.play(1, "X")
        self.assertFalse(result)
        self.assertEqual(self.tablero.casillas[1], "O")
    
    def test_reset(self):
        self.tablero.casillas = ["X"] * 9
        self.tablero.reset()
        self.assertEqual(self.tablero.casillas, [" "] * 9)

if __name__ == "__main__":
    unittest.main()