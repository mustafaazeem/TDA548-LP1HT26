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

    def get_bomb_ids(self):
        return self.id

    def fire(self, velocity, theta):
        self.x_pos
        self.y_pos
        dt = 0.02

        x_vel = velocity * math.cos(theta)
        y_vel = velocity * math.sin(theta)

        while self.y_pos >= 0:
            self.x_pos += x_vel * dt 
            self.y_pos += y_vel * dt
            x_vel -= AIR_DRAG * dt
            y_vel -= G * dt 

            time.sleep(0.1)
            animate(self.x_pos, self.y_pos)

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


b1 = Projectile(201, 10, 3.65)
print(b1.get_projectile_data())
# b1.fire(20, math.radians(45)) velocity 20 was pushing projectile out of view in lecture 
b1.fire(2, math.radians(45))    # shift to velocity 2