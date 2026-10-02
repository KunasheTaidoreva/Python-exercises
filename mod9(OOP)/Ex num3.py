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
