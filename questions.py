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

    def setDadnMom(self, momAge, dadAge):

        while 1:
            momAge = int(input("Enter moms age: "))
            if momAge < 18:
                print("Too young to get married mom ")
            elif momAge >= 18:
                print("Perfect age mom, lets go. ")
            dadAge = int(input("Enter dads age: "))
            if dadAge < 18:
                print("Too young to get married dad ")
                break
            elif dadAge >= 18:
                print("Perfect age dad, lets go. ")
                break

        Parent.count = momAge
        Parent.count2 = dadAge

    def showDadnMom(self):
        print("Dads age is: ", Parent.count)
        print("Moms age is: ", Parent.count2)


class Child(Parent):  # child of Parent
    def __init__(self, childName):
        super().__init__()
        # childName = input(" Enter child's name: ")
        self.childName = childName
        print("Child class initialized")


c = Child("John")  # child inherits moms n dads stuff
# c.setCount(50)  # set counter value LOL
# c.showMeCount()
c.setDadnMom(30, 30)  # started as 10 and 15 but updated after user input
c.momndad('Jane', 'Jack')  # started as Jane and Jack but updated after user input

print("================================")
print("Mom's name is " + str(c.mom) + "\n" + "Dad's name is " + str(c.dad) + "\n" + "Their child's mame is " + str(
    c.childName))
print("================================")
print("Mom is " + str(c.count) + " years old \n" + "& Dad is " + str(c.count2) + " years old")
print("================================")

"""
Parent class initialized
Child class initialized
Enter moms age: 15
Too young to get married mom 
Enter dads age: 19
Perfect age dad, lets go. 
Enter moms name: Jane
Enter dads name: Joe
================================
Mom's name is Jane
Dad's name is Joe
Their child's mame is John
================================
Mom is 15 years old 
& Dad is 19 years old -
================================
"""