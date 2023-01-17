# pseudo code idea using inheritance
# ============================================
from abc import ABC, abstractmethod  # testing this abstract feature


# Tahoe, Suburban, Silverado
# class Chevrolet - > main class
# def init (self, interiorType, price) and set declarations for both self. = self
# 3 attributes of the cars are ( interiorType, driveType, price)

class Chevrolet(ABC):
    def __init__(self):
        super().__init__()

    # price = None
    # interiorType = None
    # driveType = None

    @abstractmethod
    def vehicles(self):
        pass


# ============================================

# class Tahoe (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType
# then self declare them to use in Make
class Tahoe(Chevrolet):
    def __init__(self, interiorType):
        super().__init__()
        interiorType = input("Enter Tahoe interior type: ")
        self.interiorType = interiorType

    def vehicles(self):
        # return print("Interior type is: ", self.interiorType)
        return f"{{ \"Leather color is:\"  {self.interiorType}}}"
        # hm not sure issue here.


# ===========================================
# class Suburban (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType
class Suburban(Chevrolet):
    def __init__(self, price):
        super().__init__()
        price = input("Enter price of Suburban: ")
        self.price = price

    def vehicles(self):
        # return print("Price is: ", self.price)
        return f"{{ \"price of Suburban is:\"  {self.price}}}"


# ============================================

# class Silverado (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType
class Silverado(Chevrolet):
    def __init__(self, driveType):
        super().__init__()
        driveType = input("Enter drive type of Silverado: ")
        self.driveType = driveType

    def vehicles(self):
        # return print("Vehicle is: ", self.driveType)
        return f"{{ \"Drive type of Silverado:\"  {self.driveType}}}"


# ============================================

# declare a variable to call Make here
# Chevrolet = Tahoe ("...
# Chevrolet = Suburban ("...
# Chevrolet = Silverado ("...
# ============================================

tahoe = Tahoe("leather")  # testing not sure if this works.
suburban = Suburban(100000)
silverado = Silverado("Four wheel")
print(tahoe.vehicles())  # unexpected output of none. need to see why
print(suburban.vehicles())  # unexpected output of none. need to see why
print(silverado.vehicles())  # unexpected output of none. need to see why

# print (Chevrolet.Tahoe
# print (Chevrolet.Silverado
# ============================================

# should run now..
# print("test")

""" Output correct now
Enter Tahoe interior type: Leather
Enter price of Suburban: 80000
Enter drive type of Silverado: Four wheel
{ "Leather color is:"  Leather}
{ "price of Suburban is:"  80000}
{ "Drive type of Silverado:"  Four wheel}
"""
