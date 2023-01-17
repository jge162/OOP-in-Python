#  questions
#  OOP practice program

class Parent:
    count = None  # initialize
    count2 = None  # initialize
    mom = None  # initialize
    dad = None  # initialize

    def __init__(self):
        print("Parent class initialized")

    def momndad(self, mom, dad):  # want to add input for mom and dads name now
        mom = input("Enter moms name: ")  # worked
        dad = input("Enter dads name: ")
        Parent.mom = mom
        Parent.dad = dad

    def setDadnMom(self, momage, dadage):
        momage = input("Enter dads age: ")
        dadage = input("Enter moms age: ")
        Parent.count = momage
        Parent.count2 = dadage

    def showDadnMom(self):
        print("Dads age is: ", Parent.count)
        print("Moms age is: ", Parent.count2)


class Child(Parent):  # child of Parent
    def __init__(self, childName):
        super().__init__()
        self.childName = childName
        print("Child class initialized")


c = Child("John")  # child inherits moms n dads stuff
# c.setCount(50)  # set counter value LOL
# c.showMeCount()
c.setDadnMom(10, 15)  # started as 10 and 15 but updated after user input
c.momndad('Jane', 'Jack')  # started as Jane and Jack but updated after user input

print("================================")
print("Mom's name is " + str(c.mom) + "\n" + "Dad's name is " + str(c.dad) + "\n" + "Their child's mame is " + str(
    c.childName))
print("================================")
print("Mom is " + c.count + " years old \n" + "& Dad is " + c.count2 + " years old")
print("================================")
