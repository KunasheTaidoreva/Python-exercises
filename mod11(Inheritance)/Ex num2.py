class Car:
    def __init__(self,registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self,acceleration):
        self.acceleration=acceleration
        self.current_speed= self.current_speed+self.acceleration
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            if self.current_speed<0:
                self.current_speed = 0
    def drive(self,hours):
        self.hours = hours
        self.travelled_distance = self.travelled_distance+(self.hours*self.current_speed)
        
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

electricCar = ElectricCar("ABC-15", 180, 52.5)
gasolineCar = GasolineCar("ACD-123", 165, 32.3)

electricCar.accelerate(100)
gasolineCar.accelerate(120)

electricCar.drive(3)
gasolineCar.drive(3)

print(f"Electric car distance: {electricCar.travelled_distance} km")
print(f"Gasoline car distance: {gasolineCar.travelled_distance} km")