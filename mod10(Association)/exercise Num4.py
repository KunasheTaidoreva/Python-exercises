import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, acceleration):
        self.acceleration = acceleration
        self.current_speed = self.current_speed + self.acceleration

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.hours = hours
        self.travelled_distance += self.hours * self.current_speed


class Race:
    def __init__(self, name, kilometres, car_List):
        self.name = name
        self.kilometres = kilometres
        self.car_List = car_List
    def hour_passes(self):
        for car in self.car_List:
            speed = random.randint(-10, 15)
            car.accelerate(speed)
            car.drive(1)
    def print_status(self):
        print(f"\n{self.name}")
        print(f"{'Registration':<15}{'Max Speed':<15}{'Current Speed':<15}{'Distance':<15}")
        print("-" * 60)

        for car in self.car_List:
            print(
                f"{car.registration_number:<15}{car.max_speed:<15}{car.current_speed:<15}{car.travelled_distance:<15.1f}")

    def race_finished(self):
        for car in self.car_List:
            if car.travelled_distance >= self.kilometres:
                return True

        return False

cars = []

for i in range(10):
    max_speed = random.randint(100, 200)
    registration_number = "ABC-" + str(i + 1)

    car = Car(registration_number, max_speed)
    cars.append(car)

r1= Race("F1 racing", 8000, cars)
hours = 0
while not r1.race_finished():
    r1.hour_passes()
    hours= hours+ 1
    if hours % 10 == 0:
        r1.print_status()


print("\nRACE FINISHED!")
r1.print_status()