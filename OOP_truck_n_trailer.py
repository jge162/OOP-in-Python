#  tractor and trailer
#  two objects

class Truck:
    def __init__(self, tractor):
        tractor = input("Enter type of tractor: ")
        self.tractor = tractor


class Trailer:
    def __init__(self, load):
        load = input("Enter type of trailer: ")
        self.load = load


semi = Truck("Ken worth")  # placeholder
tail = Trailer("box trailer")  # placeholder
#  what type of variable are these objects?

print("The type of semi is a " + semi.tractor)
print("The type trailer is a " + tail.load)

print(isinstance(semi, Truck))
print(isinstance(tail, Trailer))

