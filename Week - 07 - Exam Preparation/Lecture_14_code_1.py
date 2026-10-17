class Station :
    def __init__(self, loc, capacity):
        self.loc = loc 
        self.capacity = capacity # 20 
        self.drones = []        # 10 

    def available(self):
        # available_capacity = self.capacity - len(self.drone) 
        # return available_capacity 
        return self.capacity - len(self.drones)

    # station.dock(self)

    def dock(self, drone):
        # if there is a space available? 
        if self.available():
            self.drones.append(drone) 
            return True 

        else:
            return False 

    def recharge(self):
        for drone in self.drones:
            drone = 15
        # TODO check how drone is recharged, and complete this part later 

from math import sqrt 

class Drone:
    def __init__(self, loc):
        self.loc = loc  
        self.range = 15 
        self.station = None 

    def distance_to(self, loc):
        x1, y1 = self.loc 
        x2, y2 = loc 

        distance = sqrt( (x2-x1)**2 + (y2-y1)**2 )

        return distance

    def reaches(self, station):
        # dist = self.distance_to(station.loc)
        # if dist <= self.range:
        #     return True 
        # return False 

        return self.distance_to(station.loc) <= self.range 

    def move(self, loc):
        d = self.distance_to(loc)

        if d <= self.range:
            if self.station is not None:
                self.station = None  

            self.range -= d
            self.loc = loc 
            return d 
        else: 
            print("cannot reach location")
            return 0
    
    def dock(self, station):
        if self.station:
            print("already docked")
        
        elif not self.reaches(station):
            print("cannot reach station")

        elif station.available() <= 0:
            print("Station full")

        else: 
            self.move(station.loc)
            self.station = station 
            station.dock(self)
            print("Successfully docked")
        

s1 = Station((3,2), 1)
s2 = Station((8,6), 2)

d1 = Drone((0,0))
print(d1.move((3,7)))
# 7.615773105863909

print(d1.move((4,4)))
# 3.1622776601683795

print(d1.dock(s2))
# cannot reach station

print(d1.dock(s1))
# successfully docked

d2 = Drone((10,0))
print(d2.move((6,3)))
# 5.0

print(d2.dock(s1))
# station full



# Time to say goodby to this wonderful class 
# Please stay happy, and become happier 