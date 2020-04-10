import mymodule as mx
import json

js1 = mx.js




# parse x:
y = json.loads(js1)

# the result is a Python dictionary:
print(y["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

ted = mx.xjs
# print(json.dumps(ted))
print(json.dumps(ted, indent=4, sort_keys=True))
# print(json.dumps(ted, indent=4, separators=(". ", " = ")))

# json.dumps(ted, indent=9
# json.dumps(ted, indent=4, separators=(". ", " = ")))