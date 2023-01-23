#  goal today create a OOP to display details of a car

class Lexus:  # car is a lexus with leather interior and navigation with a costs of $80,000.00
    leather = None
    navigation = None
    costs = None

    def __init__(self):  # function handles the 3 parameters here
        self.discountAmt = None
        self._discountAmt = None
        self.__secret = "This should not be reachable"  # testing __

    def lexusDiscount(self, discountAmt, leather, navigation, costs):
        costs = float(input("Enter vehicle price: "))
        self.leather = leather  # declarations
        self.navigation = navigation
        self.costs = costs
        self.discountAmt = discountAmt
        return discountAmt

    def lexusCost(self):
        _discountAmt = float(input("Enter discount %: "))
        var = self.costs - (self.costs * self.discountAmt)
        return self.costs


blackLexus = Lexus()
blackLexus.lexusDiscount(0.5, "Black Leather", "Touch screen Navigation", 8000)  # car is 50% off
print(blackLexus.leather)
print(blackLexus.navigation)
print(blackLexus.costs * (blackLexus.lexusDiscount(0.25, "Black Leather", "Touch screen Navigation", blackLexus.costs)))
