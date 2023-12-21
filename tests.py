import unittest
from Player import Player

class TestYams(unittest.TestCase):
    
    def test_create_player(self):
        player1 = Player()
        player2 = Player()
        self.assertEqual(player1.score,0)
    
    def test_one_roll(self):
        player1 = Player()
        self.assertGreater(player1.roll(),0)
       



if __name__ == '__main__':
    unittest.main()