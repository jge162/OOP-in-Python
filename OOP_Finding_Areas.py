# Jeremy 1/16/2023
from abc import ABC, abstractmethod


# goal is to inherit from ABC
class Shape(ABC):
    def __init__(self):
        super().__init__()
        # tying to find four areas, Triangle, Circle, square and rectangle

    @abstractmethod
    def area(self):  # You have to have correct spacing for self to work
        pass  # dummy use here, not significant value


class Triangle(ABC):
    def __init__(self, triangleBase, triangleHeight):
        triangleBase = int(input("Please enter Triangle Base: "))
        triangleHeight = int(input("Please enter Triangle Height: "))
        self.triangleHeight = triangleHeight
        self.triangleBase = triangleBase

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a Triangle is: \" {int((self.triangleBase * self.triangleHeight) / 2):.2f}}}"  # works


class Circle(ABC):
    def __init__(self, circleRadius):
        circleRadius = float(input("Enter the Radius of the Circle: "))
        self.circleRadius = circleRadius

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a Circle is: \" {int(3.14159265359 * self.circleRadius ** 2):.2f}}}"  # works


class Square(ABC):
    def __init__(self, squareSides):
        squareSides = int(input("Enter one side of a Square: "))
        self.squareSides = squareSides

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a Square is: \" {int(self.squareSides ** 2):.2f}}}"  # works


class Rectangle(ABC):
    def __init__(self, rectangleLength, rectangleWidth):
        rectangleLength = int(input("Enter length of rectangle: "))
        rectangleWidth = int(input("Enter width or rectangle: "))
        self.rectangleWidth = rectangleWidth
        self.rectangleLength = rectangleLength

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a rectangle is: \" {int(self.rectangleLength * self.rectangleWidth):.2f}}}"  # works


class Trapezoid(ABC):
    def __init__(self, Base1, Base2, Height):
        Base1 = int(input("Enter base A of Trapezoid: "))
        Base2 = int(input("Enter base B of Trapezoid: "))
        Height = int(input("Enter height of Trapezoid: "))
        self.Base1 = Base1
        self.Base2 = Base2  # issue below is it sum not *
        self.Height = Height  # formula is wrong below (1\2(a * b)*h checking formula online now

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a Trapezoid is: \" {int(((self.Base1 + self.Base2) * self.Height) * 0.5):.2f}}}"  # works


class Ellipse(ABC):
    def __init__(self, axisA, axisB):
        axisA = int(input("Enter first axis A: "))
        axisB = int(input("Enter first axis B: "))
        self.axisA = axisA  # formula of an ellipse is pi*a*b
        self.axisB = axisB  # need to add full value of pie for correct answer

    def area(self):  # You have to have correct spacing for self to work
        return f"{{\"Area of a Ellipse is: \" {((self.axisA * self.axisB) * 3.14159265359):.2f}}}"


class Kite(ABC):
    def __init__(self, diagonalA, diagonalB):
        diagonalA = int(input("Enter Kite diagonal A: "))
        diagonalB = int(input("Enter Kite diagonal B: "))
        self.diagonalA = diagonalA
        self.diagonalB = diagonalB

    def area(self):
        return f"{{\"Area of a Kite is: \" {((self.diagonalA * self.diagonalB) / 2):.2f}}}"


print("============================")
t = Triangle(15, 6)  # dummy declarations here for base and height
print(t.area())  # print the area after inputs to triangle
print("============================")
c = Circle(20)  # need to add user input now
print(c.area())  # print value of circles area. with is Pi*r ^2 Missing pi above 3.14
print("============================")
s = Square(10)  # print the area after inputs to Square
print(s.area())  # print the area after inputs to square
print("============================")
r = Rectangle(10, 15)  # dummy declarations here for Rectangle
print((r.area()))
print("============================")
p = Trapezoid(10, 15, 6)  # dummy declarations here for Trapezoid
print(p.area())  # print the area after inputs to Trapezoid
print("============================")
e = Ellipse(1, 2)  # dummy declarations here for axis's
print((e.area()))  # print the area after inputs to Ellipse
print("============================")
k = Kite(1, 2)  # dummy declarations here for axis's
print((k.area()))  # print the area after inputs to Kite
print("============================")

"""
============================
Please enter Triangle Base: 22
Please enter Triangle Height: 6
{"Area of a Triangle is: " 66.00}
============================
Enter the Radius of the Circle: 99
{"Area of a Circle is: " 30790.00}
============================
Enter one side of a Square: 19
{"Area of a Square is: " 361.00}
============================
Enter length of rectangle: 11
Enter width or rectangle: 915
{"Area of a rectangle is: " 10065.00}
============================
Enter base A of Trapezoid: 10
Enter base B of Trapezoid: 20
Enter height of Trapezoid: 30
{"Area of a Trapezoid is: " 450.00}
============================
Enter first axis A: 2
Enter first axis B: 3
{"Area of a Ellipse is: " 18.85}
============================
Enter Kite diagonal A: 15
Enter Kite diagonal B: 33
{"Area of a Kite is: " 247.50}
============================"""