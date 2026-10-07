'''
This code demonstrates associations between classes via 
Dependency injection mechanism. The fire method of class Canon depends upon Projectile object. 
'''
import math 
import time

G = 9.82
AIR_DRAG = 0.4

class Projectile:
    def __init__(self, ID, size, energy, x_pos=0, y_pos=0):
        self.id = ID
        self.size = size 
        self.energy = energy 
        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_projectile_data(self):
        # A getter function 
        return (f'id {self.id}, size {self.size}, energy {self.energy} and position ({self.x_pos}, {self.y_pos})')


class Canon:
    def __init__(self, cid, length, type):
        self.cid = cid 
        self.length = length 
        self.type = type 

    def fire(self, bomb, velocity, theta):
        x_vel = velocity * math.cos(theta)
        y_vel = velocity * math.sin(theta)
        dt = 0.02

        while bomb.y_pos >= 0:
            bomb.x_pos += x_vel * dt 
            bomb.y_pos += y_vel * dt 
            x_vel -= AIR_DRAG * dt 
            y_vel -= G * dt 
            time.sleep(0.2)

            animate(bomb.x_pos, bomb.y_pos)

# Helper function to display trajectory of our projectile 
def animate(x, y):
    width, height = 60, 30
    scale = 100
    screen = [[" " for _ in range(width)] for _ in range(height)]

    column = round(x * scale)
    row = height - 1 - round(y * scale)
    if 0 <= column < width and 0 <= row < height:
        screen[row][column] = "*"

    print("\033[2J\033[H", end="")
    print("\n".join("".join(line) for line in screen), flush=True)
    time.sleep(0.1)

bomb_1 = Projectile('B101', 20, 15)
gun_1 = Canon('Gun-13', 20, 'Ground-based muzzle')

# We pass Projectile object (bomb_1) to canon object (gun_1)
gun_1.fire(bomb_1, 2, math.radians(50))