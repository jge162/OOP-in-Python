# inheritance

print(" ")


class Kitchen:  # Parent class, children will all inherit from Parent later
    def __init__(self, utensils):
        self.utensils = utensils  # common object in a home.
        # print("Kitchen initialize! ")
        pass  # empty code...


class Stove(Kitchen):  # common to have a stove in a kitchen, so will add a pot
    def __init__(self, utensils, pot):  # child has an object(s) of its own here...
        super().__init__(utensils)  # child inherits object utensils from Parent here
        pot = input("Enter type of pot: ")
        self.pot = pot  # stove has an object pot sitting on it!


class Oven(Kitchen):  # common to have a Oven in a kitchen, so will add a food items (liver, turkey, meatLoaf):
    def __init__(self, utensils, liver, turkey, meatLoaf):  # child inherits object utensils from Parent here
        super().__init__(utensils)  # child inherits object utensils from Parent here
        self.liver = liver
        self.turkey = turkey
        self.meatLoaf = meatLoaf


class Microwave(Kitchen):   # common to have a Microwave in a kitchen, so will add plates, bowl and etc
    def __init__(self, utensils, plates, bowl, etc):  # a microwave can take objects like plates, bowl and etc
        super().__init__(utensils)
        self.plates = plates
        self.bowl = bowl
        self.etc = etc


class Refrigerator(Kitchen):  # common to have a stove in a kitchen, so will add milk
    def __init__(self, utensils, milk):
        super().__init__(utensils)
        milk = input("Enter type of milk (e.g. whole or skim): ")
        self.milk = milk


s = Stove("Bakers spoon ", "fry pan")
o = Oven("metal pan ", "liver ", "turkey ", "meat loaf")
m = Microwave("Microwave safe plate ", "tupperware ", "bowl ", "etc")
r = Refrigerator("Metal pan ", "milk")

print("===========================================================================")
print("The stove utensil is a: " + s.utensils + "| The type of pot is: " + s.pot)
print("===========================================================================")
print("The Oven utensil is a: " + o.utensils + "| The type of Meats are is: " + o.liver + o.turkey + o.meatLoaf)
print("===========================================================================")
print("The Microwave utensil is a: " + m.utensils + "| The type of Microwave items are: " + m.plates + m.bowl + m.etc)
print("===========================================================================")
print("The Refrigerator utensil is a: " + r.utensils + "| The type of milk is: " + r.milk)
print("===========================================================================")

""" Console output 
Enter type of pot: Plastic
Enter type of milk (e.g. whole or skim): Skim
===========================================================================
The stove utensil is a: Bakers spoon | The type of pot is: Plastic
===========================================================================
The Oven utensil is a: metal pan | The type of Meats are is: liver turkey meat loaf
===========================================================================
The Microwave utensil is a: Microwave safe plate | The type of Microwave items are: tupperware bowl etc
===========================================================================
The Refrigerator utensil is a: Metal pan | The type of milk is: Skim
===========================================================================
"""