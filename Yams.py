from enum import Enum
from Player import Player

class Yams():
    
    def __init__(self):
        pass
    
    def is_brelan(throws):
        for valeur in throws:
            if throws.count(valeur) >= 3:
                return 28
        return 0
    
    def is_carre(throws):
        for valeur in throws:
            if throws.count(valeur) >= 4:
                return 35
        return 0
    
    def is_full(throws):
        for valeur in throws:
            if throws.count(valeur) in [2,3]:
                return 30
        return 0
        
            
            