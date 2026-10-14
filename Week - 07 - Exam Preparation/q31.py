from math import sqrt

type Location = tuple[float,float]

class Station:
  def __init__(self, loc: Location, capacity: int):
    self.capacity = capacity
    self.loc = loc
    self.drones = set()
  
  def available(self):
    return self.capacity - len(self.drones)

  def dock(self, drone: "Drone") -> bool:
    if self.available() > 0:
      self.drones.add(drone)
      return True
    else:
      return False

  # Not a required part of solution
  def undock(self, drone: "Drone"):
    self.drones.remove(drone)

  def recharge(self):
    for drone in self.drones:
      drone.range = 15

  # Not a required part of solution
  def __repr__(self):
    (x,y) = self.loc
    return f"Station ({x},{y}) <{self.available()}/{self.capacity}>"

class Drone:
  def __init__(self, loc: Location):
    self.loc = loc
    self.range = 15
    self.station = None
  
  def distance_to(self, loc: Location) -> float:
    (x1,y1) = self.loc
    (x2,y2) = loc
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
  
  def reaches(self, station: Station) -> bool:
    return self.range >= self.distance_to(station.loc)

  def move(self, loc: Location) -> float:
    distance = self.distance_to(loc)
    if self.range < distance:
      print("cannot reach location")
      return 0
    if self.station:
      self.station.undock(self)
      self.station = None
    self.loc = loc
    self.range -= distance
    return distance

  def dock(self, station: Station):
    if self.station:
      print("already docked")
    elif not self.reaches(station):
      print("cannot reach station")
    elif station.dock(self):
      self.move(station.loc)
      self.station = station
      print("successfully docked")
    else:
      print("station full")

  # Not a required part of solution
  def __repr__(self):
    (x,y) = self.loc
    return f"Drone ({x},{y}) <{self.range}>"

# --- 

if __name__ == "__main__":

  s1 = Station((3,2), 1)
  s2 = Station((8,6), 2)

  d1 = Drone((0,0))
  d1.move((3,7))
  d1.move((4,4))
  d1.dock(s2) # cannot reach station
  d1.dock(s1) # successfully docked

  d2 = Drone((10,0))
  d2.move((6,3))
  d2.dock(s1) # station full
