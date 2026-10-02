class Car:
    def __init__(self,registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

c1 = Car("ABC-123",142)
print(c1.registration_number)
print(c1.max_speed)
print(c1.current_speed)
print(c1.travelled_distance)