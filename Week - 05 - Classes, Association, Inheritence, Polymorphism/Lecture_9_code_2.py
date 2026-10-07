class Projectile:
    def __init__(self, ID, size, energy):
        self.id = ID
        self.size = size 
        self.energy = energy 

    def get_projectile_data(self):
        # A getter function 
        return (f'The bomb with id {self.id} has {self.size} and {self.energy}')

    def get_bomb_ids(self):
        return self.id

bomb_list = [Projectile(102, 20, 3.5), Projectile(103, 2.54, 0.5)]

for bomb in bomb_list:
    print('getter function: ', bomb.get_bomb_ids())
    print('direct access: ', bomb.id)