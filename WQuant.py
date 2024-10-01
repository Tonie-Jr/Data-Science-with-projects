#Python order of operations (PEMDAS)
import pandas as pd
a = (((6**3 + 7) * 4) / 16 + 9 - 2)
print(a)

#Create and print a list that shows the area of the houses, called `area_m2`. Include the items `187.0`, `82.0`, and `235.0`.
area_m2 = [187, 82, 235]
print(area_m2)

#accessig the second and last items in the list
print(area_m2[1])
print(area_m2[-1])

#appending an item in the list
area_m2.append(4555)
print(area_m2)

#summing the area_m2
total_sum = sum(area_m2)
print(total_sum)

#Print Ellipsis
area_m3 = ...
print(area_m3)

#Try it yourself! Create a list called area_m2 that includes the terms 235.0, 130.0, and 137.0, then create another list called price_cop that includes the terms 400000000.0, 850000000.0, and 475000000.0. Then zip them together to create a new list called area_price, and print the result.
area_m2 = [235.0, 130.0, 137.0]
price_cop = [400000000.0, 8500000000.0,475000000.0]
new_list = zip(area_m2, price_cop)
zipped_list = list(new_list)
print(zipped_list)

#for loop
for x in price_cop:
    print(x)

#Dictionaries
bogota = {
"price_usd":121555.09,
"area_m2":82.0,
"property_type":"house"
}
print(bogota)
#Accessing a value from a dictionary
print(bogota["price_usd"])
print(bogota.get("price_usd"))

# Accessing all the Keys and values in a dictionary
print(bogota.keys())
print(bogota.values())

#If you want the printed in a form of a list
print(list(bogota.keys()))
print(list(bogota.values()))

#You can also iterate the values or the keys in dictionary
for i in bogota.keys():
    print(i)
for x in bogota.values():
    print(x)

#Working with jason file(JSON stands for Java Script Object Notation, and it's a text format for storing and transporting data.) JSON works by creating key-value pairs, where the key is data that can be represented by letters (called a string). JSON values can be strings, numbers, objects, arrays, boolean data, or null.

#You can create a DataFrame from a Python dictionary using from_dict function.
data = {
    "col_1": [4, 3, 2, 1, 0],
    "col_2": ["a", "b", "c", "d", "e"]
}
x = pd.DataFrame.from_dict(data)
print(x)

#We can also let keys to be index instead of the columns
# the (orient = "index") tells Pandas to treat the keys of the dictionary as the row index in the resulting DataFrame.
y = pd.DataFrame.from_dict(data, orient = "index")
print(y)

#We can also specify column names
z = pd.DataFrame.from_dict(data, orient = "index", columns = ["A","B", "C", "D", "E"])
print(z)

#Create a DataFrame called using the dictionary clothes and make the keys as index, and put column names as ['color','size']
clothes = {"shirt": ["red", "M"], "sweater": ["yellow", "L"], "jacket": ["black", "L"]}
print(pd.DataFrame.from_dict(clothes, orient = "index", columns = ["color", "size"]))

#JSON is short for JavaScript Object Notation. It is another widely used data format to store and transfer the data. It is light-weight and very human readable. In Python, we can use the json library to read JSON files. Here is an example of a JSON string.
info = """{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobby": "running",
    "age": 35
}"""
print(info)

import json
data = json.loads(info)
print(data)
print(data["firstName"])

#A dictionary may not be as convenient as a `DataFrame` in terms of data manipulation and cleaning. But once we've turned our json string into a dictionary, we can transform it into a `DataFrame` using the `from_dict` method.
jsdata = pd.DataFrame.from_dict(data)
print(jsdata)


df = pd.DataFrame.from_dict(data, orient="index", columns=["subject 1"])
df