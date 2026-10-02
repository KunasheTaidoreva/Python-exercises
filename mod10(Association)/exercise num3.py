class Elevator:
    def __init__(self,bottom_floors,top_floors):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.current_floor = bottom_floors
    def floor_up(self):
        self.current_floor = self.current_floor+1
    def floor_down(self):
        self.current_floor = self.current_floor-1
    def go_to_floor(self,floorNum):
        self.floorNum = floorNum
        while self.current_floor != floorNum:
            if self.current_floor > floorNum:
                self.floor_down()
                print(f"Now on floor {self.current_floor}")
            if self.current_floor < floorNum:
                self.floor_up()
                print(f"Now on floor {self.current_floor}")

class Building:
    def __init__(self,bottomFloors,topFloors,ElevatorNum):
        self.bottomFloors = bottomFloors
        self.topFloors = topFloors
        self.ElevatorNum = ElevatorNum
        self.Elevators =[]
        for e in range(ElevatorNum):
            Evt = Elevator(bottomFloors,topFloors)
            self.Elevators.append(Evt)
    def run_elevator(self,elevator,floorDestination):
        self.floorDestination = floorDestination
        self.elevator = elevator-1
        self.x = self.Elevators[self.elevator]
        self.x.go_to_floor(floorDestination)
    def fire_alarm(self):
        for i in self.Elevators:
            i.go_to_floor(self.bottomFloors)
        print("Fire alert all elevators are on the bottom floors")

b1 = Building(1,8,4)
b1.run_elevator(4,8)
print("-"*15)
b1.run_elevator(3,6)
print("-"*15)
b1.fire_alarm()