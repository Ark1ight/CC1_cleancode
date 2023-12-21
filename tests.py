import unittest
from Player import Player
from Yams import Yams

class TestYams(unittest.TestCase):
    
    def test_create_player(self):
        player1 = Player()
        self.assertEqual(player1.score,0)
          
    def test_is_brelan(self):
        player1_rolls = [1,1,1,3,5]
        brelan = Yams.is_brelan(player1_rolls)
        self.assertEqual(brelan,28)
        

        


if __name__ == '__main__':
    unittest.main()