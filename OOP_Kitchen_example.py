# practicing inheritance with classes
# (object in a kitchen for example)

class Kitchen:
    def __init__(self, Utensils):
        self.Utensils = Utensils


class Stove(Kitchen):
    def __init__(self, Utensils, plates):
        super().__init__(Utensils)
        self.plates = plates


class Oven(Kitchen):
    def __init__(self, Utensils, meat, turkey, meatLoaf):
        super().__init__(Utensils)
        self.meat = meat
        self.turkey = turkey
        self.meatLoaf = meatLoaf


class Microwave(Kitchen):
    def __init__(self, Utensils, topRamen):
        super().__init__(Utensils)
        self.topRamen = topRamen


class Refrigerator(Kitchen):
    def __init__(self, Utensils, milk):
        super().__init__(Utensils)
        self.milk = milk


s = Stove("fork ", "porcelain")
o = Oven("steak knives", " steak ", " white meat ", "three pounds")
m = Microwave("microwave safe only ", "chicken flavor")
r = Refrigerator("plastic only ", "Must not be rotten")


print(s.Utensils + s.plates)
print(o.Utensils + o.meat + o.meatLoaf + o.turkey)
print(m.Utensils + m.topRamen)
print(r.Utensils + r.milk)

""" expected output
fork porcelain
steak knives steak three pounds white meat 
microwave safe only chicken flavor
plastic only Must not be rotten
"""
