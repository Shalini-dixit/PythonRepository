import animal

class Reptile(animal.Animal):
    def __init__(self, name):
        self.name = name
    
    def is_reptile(self):
        return True

    def is_mammal(self):
        return False