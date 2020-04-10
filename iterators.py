mytuple = ("banana", "cherry", "lemon")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


z = "banana"
x = iter(z)

for y in z:
    print(y)


class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = myNumbers()
myiter = iter(myclass)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)