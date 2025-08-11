import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        p = Player("Juan", "X")
        self.assertEqual(p.name, "Juan")
        self.assertEqual(p.symbol, "X")
        self.assertEqual(p.score, 0)

    def test_score_update(self):
        p = Player("Ana", "O")
        p.score += 1
        self.assertEqual(p.score, 1)

if __name__ == "__main__":
    unittest.main()