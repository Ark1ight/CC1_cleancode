import unittest
from Player import Player
from Yams import Yams

class TestYams(unittest.TestCase):
    
    def test_create_player(self):
        player1 = Player()
        self.assertEqual(player1.score,0)
          
    def test_is_brelan(self):
        player_rolls = [[1,1,1,3,5],
                        [1,1,1,3,5],
                        [1,1,1,3,5]
                        ]
        sum = 0
        for throws in player_rolls:
            sum += Yams.is_brelan(throws)
        self.assertEqual(sum,84)
    
    def test_is_carre(self):
        player_rolls = [[1,1,1,1,5],
                        [1,1,1,1,5],
                        [1,1,1,1,5],
                        [1,1,1,1,5]]
        sum = 0
        for throws in player_rolls:
            sum += Yams.is_carre(throws)
        self.assertEqual(sum,140)
        
    def test_is_full(self):
        player_rolls = [[1,1,1,5,5],
                        [1,1,1,5,5],
                        [1,1,1,5,5],
                        [2,1,1,5,5]
                        ]
        sum = 0
        for throws in player_rolls:
            sum += Yams.is_full(throws)
        self.assertEqual(sum,120)
    
    def test_is_yams(self):
        player_rolls = [3,3,3,3,3]
        yams = Yams.is_yams(player_rolls)
        self.assertEqual(yams,50)
        

        


if __name__ == '__main__':
    unittest.main()