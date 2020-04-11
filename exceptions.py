try:
  print(x)
except:
  print("An exception occurred")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")

