class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')
your_car = Vehicle('Cadillac', 'Escalade')


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies through the sky..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles on the road..')


class GolfCart(Vehicle):
    def moves(self):
        print("Glides slowly on the course..")


class Boat(Vehicle):
    def moves(self):
        print("Sails smoothly on water..")


# Create instances
cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')
yacht = Boat("Yamaha", "WaveRunner")

# Call methods
for v in (my_car, your_car, cessna, mack, golfwagon, yacht):
    v.get_make_model()
    v.moves()
