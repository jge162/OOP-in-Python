#  tractor and trailer
#  two objects

class Truck:
    def __init__(self, tractor):
        self.tractor = tractor


class Trailer:
    def __init__(self, load):
        self.load = load


semi = Truck("Ken worth")
tail = Trailer("box trailer")
#  what type of variable are these objects?

print(semi.tractor)
print(tail.load)

print(isinstance(semi, Truck))
print(isinstance(tail, Trailer))

