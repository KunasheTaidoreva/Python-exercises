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

e1 = Elevator(1,8)
e1.go_to_floor(5)
print("-"*15)
e1.go_to_floor(1)