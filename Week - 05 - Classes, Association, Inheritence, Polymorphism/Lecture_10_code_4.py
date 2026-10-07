'''
Inheritence: Classes in a child parent relationship 
Class Projectile is a parent (or super or base) class. Missile, Bomb and Rocket classes dervice from Projectile classes, that means Missile, Bomb and Rocket are childen of Projectile class. 
Also see how Projectile, Missile, Bomb and Rocket classes have a method with the same name 'get_projectile_data'. It is a basic example of polymorphism, that means, multiple functions with the same name. Which function is actually called is decided based on arguments, which is 'self' in this case
'''
import math 
import time

G = 9.82
AIR_DRAG = 0.4

class Projectile:
    def __init__(self, ID, size, energy):
        self.id = ID
        self.size = size 
        self.energy = energy 
        self.x_pos = 0
        self.y_pos = 0

    def get_projectile_data(self):
        # A getter function 
        return (f'id {self.id}, size {self.size}, energy {self.energy} and position ({self.x_pos}, {self.y_pos})')
    

class Missile(Projectile):
    def __init__(self, ID, size, energy, feul, guidance_system):
        super().__init__(ID, size, energy)
        self.feul = feul 
        self.guidance_system = guidance_system 

    def get_projectile_data(self):
        base_data = super().get_projectile_data()
        return base_data + self.guidance_system

    def guide(self):
        print("Missile is on a guided path")

class Bomb(Projectile):
    def __init__(self, ID, size, energy, explosion_method):
        super().__init__(ID, size, energy)
        self.explosion_method = explosion_method

    def get_projectile_data(self):
        base_data = super().get_projectile_data()
        return base_data + self.explosion_method

    def explode(self):
        print("Bomb will explode with a timer")

class Rocket(Projectile):
    def __init__(self, ID, size, energy, speed):
        super().__init__(ID, size, energy)
        self.speed = speed 

    def get_projectile_data(self):
        base_data = super().get_projectile_data()
        return base_data + str(self.speed )

    def show_speed(self):
        print("Current speed of rocket is", self.speed)

m1 = Missile('M101', 25, 23, 'GPS', 'solid')
r1 = Rocket('R101', 15, 13, 500)
b1 = Bomb('B101', 12, 8, 'Timer')

print('missile data: ', m1.get_projectile_data())
print('rocket data: ', r1.get_projectile_data())
print('bomb data: ', b1.get_projectile_data())

b1.explode()
m1.guide()
r1.show_speed()
