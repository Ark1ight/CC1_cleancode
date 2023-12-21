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