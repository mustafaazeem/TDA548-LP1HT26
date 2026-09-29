class Projectile:
    '''
    This class models a Prjectile. 
    It creates a new projectile with the following information:
    1 - projectile ID 
    2 - projectile size
    3 - projectile energy released on explosion 
    '''

    def __init__(self, ID, size, energy):
        '''
        This function is a constructor of our projectile class
        When this function is called, it creates a new Projectile object 
        '''
        self.id = ID
        self.size = size 
        self.energy = energy 

    def get_projectile_data(self):
        return (f'The bomb with id {self.id} has {self.size} and {self.energy}')

bomb_1 = Projectile(101, 2.5, 13)
print(bomb_1.id)
print(bomb_1.energy)
print(bomb_1.size)

print(bomb_1.get_projectile_data())

bomb_list = [Projectile(102, 20, 3.5), Projectile(103, 2.54, 0.5)]
for bomb in bomb_list:
    print(bomb.get_projectile_data())