# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# puesudo code idea for a Rivian electric car using inheritence
# Tahoe, Suburban, Silverado
# class Chevrolet - > main class
# def init (self, interiorType, price) and set declarations for both self. = self
# 3 attributes of the cars are ( interiorType, driveType, price)

class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)


#        self.period = period
#        self.publisher = publisher

# class Tahoe (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType
# then self delclare them to use in Make

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


# class Suburban (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


# class Silverado (Chevrolet): inherit the make here...
# super class to pull in interiorType and price, driveType

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


# declare a variable to call Make here
# truck = Tahoe ("...
# truck = Suburban ("...
# truck = Silverado ("...

# print (truck.Suburban
# print (truck.Tahoe
# print (truck.Silverado

# should run now..


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)