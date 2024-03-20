import random


class Grain:
    def __init__(self):
        self.origine = ""
        self.arome = ""
        self.annee = 0
        self.corps = random.randint(1, 9)

        self.origines = ["Vietnam", "Kenya", "Colombie", "Guatemala"]
        self.aromes = ["Floral", "Fruite", "Chocolate", "Epice"]
        

    def is_valid(self):
        if self.origine not in self.origines:
            print(f"Invalid origine: {self.origine}")
            return False
        if self.arome not in self.aromes:
            print(f"Invalid arome: {self.arome}")
            return False
        if not isinstance(self.annee, int) or self.annee % 5 == 0:
            print(f"Invalid annee: {self.annee}")
            return False
        if not isinstance(self.corps, int) or not (1 <= self.corps <= 9):
            print(f"Invalid corps: {self.corps}")
            return False
        return True