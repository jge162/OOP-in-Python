#  questions
#  OOP practice program

class Parent:

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
            else:
                if momAge >= 18:
                    print("Perfect age mom, lets go. ")
            dadAge = int(input("Enter dads age: "))
            if dadAge < 18:
                print("Too young to get married dad ")
            else:
                if dadAge >= 18:
                    print("Perfect age dad, lets go. ")

            if momAge == dadAge:
                print("Wow, your the same age?")
                break
            else:
                if momAge != dadAge:
                    print("Why cant we ever be the same age")
                    break


        Parent.count = momAge
        Parent.count2 = dadAge

    def showDadnMom(self):
        print("Dads age is: ", Parent.count)
        print("Moms age is: ", Parent.count2)


class Child(Parent):  # child of Parent
    def __init__(self, childName):
        super().__init__()
        childName = input(" Enter child's name: ")
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
 Enter child's name: Jacob
Child class initialized
Enter moms age: 21
Perfect age mom, lets go. 
Enter dads age: 20
Perfect age dad, lets go. 
Why cant we ever be the same age
Enter moms name: Jane
Enter dads name: Doe
================================
Mom's name is Jane
Dad's name is Doe
Their child's mame is Jacob
================================
Mom is 21 years old 
& Dad is 20 years old
================================
"""