import reptile

class Lizard(reptile.Reptile):
    def __init__(self,name):
        self.name = name
    
    def is_snake(self):
        return True