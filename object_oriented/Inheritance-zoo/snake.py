import reptile

class Snake(reptile.Reptile):
    def __init__(self,name):
        self.name = name

    def is_snake(self):
        return True