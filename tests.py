import unittest
from yams import Player

class TestYams(unittest.TestCase):
    
    def test_create_player(self):
        player1 = Player()
        player2 = Player()
        self.assertEqual(player1.score,0)



if __name__ == '__main__':
    unittest.main()