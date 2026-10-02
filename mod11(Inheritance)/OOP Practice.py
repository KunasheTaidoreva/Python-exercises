class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
    def start_car(self):
        self.engine.start()

class ElectricCar(Car):
    def __init__(self,brand,engine,battery):
        super().__init__(brand,engine)
        self.battery = battery
    def start_car(self):
        print("Electric car starting")
        self.engine.start()
e1 = Engine()
c1 = ElectricCar("Tesla",e1,"12V")
c1.start_car()