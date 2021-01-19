class Parent:        # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)

    def myMethod(self):
        print("Calling Parent method")


class Child(Parent):  # define child class
    name = None

    def __init__(self, name):
        print("Calling child constructor")
        Child.name = name

    def childMethod(self):
        print("Calling child method")

    def getName(self):
        return Child.name

    def myMethod(self):
        print("Calling Child method")


c = Child("Porsia")  # instance of child
c.childMethod()      # child calls its method
print(c.getName())
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.myMethod()         # override parent method if child's method available, if not call parents method
