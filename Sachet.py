
class Sachet:
    def __init__(self):
        self.poids = 0
        self.type = ""
        self.grains = []
        self.composition = []
        self.types = ["pure", "mixte"]
        
    def is_valid(self):
        return self.type in self.types and isinstance(self.poids, int) and self.poids % 500 == 0 and self.poids <= 2000 and all([grain.is_valid() for grain in self.grains]) and (self.type =="pure" or sum(self.composition) == 100)