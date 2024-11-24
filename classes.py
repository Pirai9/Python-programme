# Class
class vehile:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def moves(self):
        print("Moves along..")

    def get_move(self):
        print(f"I'm a {self.model} {self.make}.")

my_car=vehile('Tesla','model Y')


my_car.moves()
print(my_car.model)
print(my_car.make)
print(my_car.get_move())

your_car=vehile('Tata','Nexan')
your_car.get_move()

print('\n\n')
# Inheritance
class Airplane(vehile):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id=faa_id

    def moves(self):
        print('Flies along..')

class Truck(vehile):
    def moves(self):
        print('Rumbles along..')

class GolfCart(vehile):
    pass

# Objects
cessna=Airplane('Cessna','Skyhawk','N-12345')
mack=Truck('Mack','Pinnacle')
golfwagon=GolfCart('Yamaha','GC100')

# **************
cessna.get_move()
cessna.moves()
mack.get_move()
mack.moves()
golfwagon.get_move()
golfwagon.moves()

print('\n\n')
# *****Polymarpisim***
for v in (my_car,your_car,cessna,mack,golfwagon):
    v.get_move()
    v.moves()

    