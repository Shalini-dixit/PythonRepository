class Car:
    def __init__(self, name, model,engine):
        self.name = name
        self.model = model
        self.engine = engine
    
    def get_info(self):return "This is {} {} with engine {} ".format(self.name, self.model, self.engine)


car = Car("Mercedez", "Benz","2500cc")
print(car.get_info())
        
