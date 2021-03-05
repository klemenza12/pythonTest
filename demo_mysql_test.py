import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mecho",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")

# mycursor.execute("DROP TABLE customers")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# print(mycursor.rowcount, "record inserted.")

# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)

# mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT name, address FROM customers")
# myresult1 = mycursor.fetchone()
# myresult = mycursor.fetchall()

# print(myresult1)

# for x in myresult:
#   print(x)


# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# sql = "SELECT * FROM customers WHERE address LIKE '%way%' ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# # mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")


# sql = "DROP TABLE IF EXISTS customers23"

# mycursor.execute(sql)


# 

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

