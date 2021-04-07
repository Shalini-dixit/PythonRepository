import animal

class Mammal(animal.Animal):
    def __init__(self,name):
        self.name = name

    def is_mammal(self):
        return True

    def is_reptile(self):
        return False