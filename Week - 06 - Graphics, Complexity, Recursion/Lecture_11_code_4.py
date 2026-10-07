'''
This simulation uses the coordinate system provided by the graphics library. 
We now divide the screen based on our own unit definition. For example, 
the following window is 800 x 800 pixels, when we set its coordinates 
as 0,0,200,200, we get 4-pixels per unit. 
Also, we can now set x=0, y=0 to be the bottom-left corner which represents 
a real-world like situation.
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
        self.win.setCoords(0, 0, 200, 200)
        
# def method_name (self, another_object)
    def fire(self, velocity, theta):
        x_vel = velocity * math.cos(theta)
        y_vel = velocity * math.sin(theta)
        dt = 0.02

        bomb = Circle(Point(10, 10), 1)
        bomb.setFill('red')
        bomb.draw(self.win)

        # Now we do not need a SCALE because we have already scaled our window with setCoords
        # SCALE = 100
        while self.bomb.y_pos >= 0:
            dx = x_vel*dt #* SCALE
            dy = y_vel*dt #* SCALE

            self.bomb.x_pos += x_vel * dt 
            self.bomb.y_pos += y_vel * dt 
            x_vel -= AIR_DRAG * dt 
            y_vel -= G * dt 

            print(dx, dy)
            bomb.move(dx, dy)

            time.sleep(0.02)
           
        self.win.getKey()

    def load_projectile(self):
        self.bomb.x_pos = 0 

canon = Canon('C101', 45, 'Vehicle-Mounted')

# the velocity is now more realistic 
canon.fire(40, math.radians(60))