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

c1 = Car("ABC-123",142)
c1.accelerate(30)
c1.accelerate(70)
c1.accelerate(50)
print(c1.current_speed)
c1.accelerate(-200)
print(c1.current_speed)