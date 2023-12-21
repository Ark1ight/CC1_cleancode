from enum import Enum
import random 
class Figure(Enum):
    Brelan : 28
    Carre : 35
    Full : 30
    GrandeSuite : 40
    Yams : 50



class Player:
    def __init__(self) -> None:
        self.score = 0

    def roll(self):
        throws = [random.randint(1, 6) for _ in range(5)]
        final_score = 0
        for throw in throws:
            final_score+=throw
        return final_score
            