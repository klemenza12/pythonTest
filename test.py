import random

# print(random.randrange(1,9))
x = "awsesome"
def myFunc():
    global t
    t=141
    print ("python is " + x)
    

# myFunc()    

# print(9 != 10)


def myTest ():
    if (1 < 5 & 3 > 4):
        return True
    else:
        return False

# print(myTest())            
thelist = ["banana",
           "apple",
           "mango"
           ]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 3020
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"].keys())

# for x,y in thisdict.items():
#   print(y)



# print(thisdict)
# print(len(thelist))
# thelist.append("orange")
# thelist.insert(1, "notapple")
# for x in thelist:
#     print (x)
