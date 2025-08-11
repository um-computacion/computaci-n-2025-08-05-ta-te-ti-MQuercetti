import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from cli import hay_ganador
import unittest

class TestCli(unittest.TestCase):
    def test_hay_ganador_fila(self):
        casillas = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(hay_ganador(casillas), "X")

    def test_hay_ganador_columna(self):
        casillas = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        self.assertEqual(hay_ganador(casillas), "O")

    def test_hay_ganador_diagonal(self):
        casillas = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertEqual(hay_ganador(casillas), "X")

    def test_no_ganador(self):
        casillas = ["X", "O", "X", "X", "O", "O", "O", "X", "O"]
        self.assertIsNone(hay_ganador(casillas))

if __name__ == "__main__":
    unittest.main()