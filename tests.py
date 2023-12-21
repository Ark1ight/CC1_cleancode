import unittest
from Player import Player
from Yams import Yams

class TestYams(unittest.TestCase):
    
    def test_create_player(self):
        player1 = Player()
        self.assertEqual(player1.score,0)
          
    def test_is_brelan(self):
        player_rolls = [1,1,1,3,5]
        brelan = Yams.is_brelan(player_rolls)
        self.assertEqual(brelan,28)
    
    def test_is_carre(self):
        player_rolls = [1,1,1,1,5]
        carre = Yams.is_carre(player_rolls)
        self.assertEqual(carre,35)
        
    def test_is_full(self):
        player_rolls = [1,1,1,5,5]
        full = Yams.is_full(player_rolls)
        self.assertEqual(full,30)
        

        


if __name__ == '__main__':
    unittest.main()