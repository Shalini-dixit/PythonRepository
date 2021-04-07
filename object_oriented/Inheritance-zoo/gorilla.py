import mammal

class Gorilla(mammal.Mammal):
    def __init__(self,name):
        self.name = name

    def is_gorilla(self):
        return True