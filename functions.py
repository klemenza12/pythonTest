def myFunc (param1, param2):
    print (param1, param2)

myFunc("Email", "abv")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function1(child3, child2, child1):
  print("The youngest child is " + child2)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function2(country = "Norway"):
  print("I am from " + country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")

def my_function4(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function4(fruits)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    # print (k)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)