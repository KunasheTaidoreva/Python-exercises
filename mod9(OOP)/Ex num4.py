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


object=1
CARS=[]
import random
for i in range(10):
    max=random.randint(100,200)
    regNum="ABC-"+str(object)
    instance = Car(regNum,max)
    CARS.append(instance)
    object +=1

race_finished = False

while race_finished == False:

    for i in range(len(CARS)):
        speed = random.randint(-10, 15)
        CARS[i].accelerate(speed)
        CARS[i].drive(1)

    for i in range(len(CARS)):
        if CARS[i].travelled_distance >= 10000:
            race_finished = True
            break

print(f"{'Registration':<15}{'Max Speed':<15}{'Current Speed':<15}{'Distance':<15}")
print("-" * 60)

for car in CARS:
    print(f"{car.registration_number:<15}{car.max_speed:<15}{car.current_speed:<15}{car.travelled_distance:<15}")