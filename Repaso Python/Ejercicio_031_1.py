import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

dado_6_caras = Die(6)

print("Tiradas de un dado de 6 caras:")
for _ in range(10):
    print(dado_6_caras.roll_die())

dado_10_caras = Die(10)

print("\nTiradas de un dado de 10 caras:")
for _ in range(10):
    print(dado_10_caras.roll_die())

dado_20_caras = Die(20)

print("\nTiradas de un dado de 20 caras:")
for _ in range(10):
    print(dado_20_caras.roll_die())
