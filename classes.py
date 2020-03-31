class MyClass:
  x = 5

p1 = MyClass()
# print(p1.x)

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def myFunc (self):
        print (self.name + " " + str(self.age)  + " this is the name of the person who was called and the age of the person")

p2 = Person ("John", 36)
print (p2.name, p2.age) 
p2.myFunc()

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.age)

p1 = Person2("Ivan", 36)
p1.name = "Venelin"
del p1.age
p1.myfunc()