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
