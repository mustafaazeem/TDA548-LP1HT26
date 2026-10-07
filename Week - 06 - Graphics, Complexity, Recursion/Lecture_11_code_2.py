'''
We learn how to move our bomb object on screen with graphics library.
In this design, we calculate bomb position on screen by ourself. 
The coordinate system of our window is different than the real world
In graphics library, the x =0, y = 0 is on top-left corner, while is 
on bottom-left in real world. So we need a translation formula which 
we develop here
'''

from graphics import * 
import math 

from Animate import animate 
from Projectile import * 

class Canon:
    # Now a composition design 
    def __init__(self, cid, length, type):
        self.cid = cid 
        self.length = length 
        self.type = type 
        self.bomb = Projectile(201, 25, 12)
        self.win = GraphWin("Projectile Simulation", 800, 800)
        
# def method_name (self, another_object)
    def fire(self, velocity, theta):
        x_vel = velocity * math.cos(theta)
        y_vel = velocity * math.sin(theta)
        dt = 0.02

        bomb = Circle(Point(10, 390), 5)
        bomb.setFill('red')
        bomb.draw(self.win)

        # SCALE represents how many pixels we put in one unit of real-world, for example in a feet or meter 
        SCALE = 100
        while self.bomb.y_pos >= 0:
            dx = x_vel*dt 
            dy = y_vel*dt 

            self.bomb.x_pos += x_vel * dt 
            self.bomb.y_pos += y_vel * dt 
            x_vel -= AIR_DRAG * dt 
            y_vel -= G * dt 

            print(dx, dy)

            # putting a - sign with y inverts it to represent a real-world like change 
            bomb.move(dx*SCALE, -dy*SCALE)

            time.sleep(0.2)
           
        self.win.getKey()

    def load_projectile(self):
        self.bomb.x_pos = 0 

canon = Canon('C101', 45, 'Vehicle-Mounted')
canon.fire(10, math.radians(60))