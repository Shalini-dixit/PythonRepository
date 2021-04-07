import mammal

class Bear(mammal.Mammal):
    def __init__(self,name):
        self.name = name

    def is_bear(self):
        return True