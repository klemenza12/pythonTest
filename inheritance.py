class Person:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname (self):
        print (self.firstname + " " + self.lastname)


class Student(Person):
    def __init__(self, large, long):
        Person.__init__(self, large, long)


class Pedal(Student):
    def __init__(self, first, second, year):
        super().__init__(first, second)
        self.graduationyear = year
    
    def welcome(self):
        print(str(self.graduationyear) + " " + str(self.firstname) + " " + str(self.lastname))


x = Student("John", "Doe")        
x.printname()


y = Pedal("Georgi", "Doe", 2020)        
y.printname()
y.welcome()
