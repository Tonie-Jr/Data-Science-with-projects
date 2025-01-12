#Python order of operations (PEMDAS)
import pandas as pd

a = (((6**3 + 7) * 4) / 16 + 9 - 2)
print(a)

#Create and print a list that shows the area of the houses, called `area_m2`. Include the items `187.0`, `82.0`, and `235.0`.
area_m2 = [187, 82, 235]
print(area_m2)

#accessig the second and last items in the list.
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

#Working with jason file(JSON stands for JavaScript Object Notation, and it's a text format for storing and transporting data.) JSON works by creating key-value pairs, where the key is data that can be represented by letters (called a string). JSON values can be strings, numbers, objects, arrays, boolean data, or null.

#You can create a DataFrame from a Python dictionary using from_dict function.
data = {
    "col_1": [4, 3, 2, 1, 0],
    "col_2": ["a", "b", "c", "d", "e"]
}
x = pd.DataFrame.from_dict(data)
print(x)

#We can also let keys to be indexed instead of the columns
# the (orient = "index") tells Pandas to treat the keys of the dictionary as the row index in the resulting DataFrame.
y = pd.DataFrame.from_dict(data, orient = "index")
print(y)

#We can also specify column names
z = pd.DataFrame.from_dict(data, orient = "index", columns = ["A","B", "C", "D", "E"])
print(z)

#Create a DataFrame called using the dictionary clothes and make the keys as index, and put column names as ['color','size']
clothes = {"shirt": ["red", "M"], "sweater": ["yellow", "L"], "jacket": ["black", "L"]}
print(pd.DataFrame.from_dict(clothes, orient = "index", columns = ["color", "size"]))

#JSON is short for JavaScript Object Notation. It is another widely used data format to store and transfer the data. It is light-weight and very human-readable. In Python, we can use the json library to read JSON files. Here is an example of a JSON string.
info = """{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobby": "running",
    "age": 35
}"""
print(info)

import json
data2 = json.loads(info)
print(data2)
print(data2["firstName"])

#A dictionary may not be as convenient as a `DataFrame` in terms of data manipulation and cleaning. But once we've turned our json string into a dictionary, we can transform it into a `DataFrame` using the `from_dict` method.

df = pd.DataFrame.from_dict(data, orient="index", columns=["subject 1", "subject 1", "subject 1", "subject 1", "subject 1"])
print(df)

#This will create a DataFrame where "Name" and "Age" are the columns.
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df4 = pd.DataFrame().from_dict(data, orient='columns')
print(df4)

#This will treat "row1" and "row2" as the row labels (index) and populate the DataFrame accordingly with "Name" and "Age" as columns.
data = {'row1': {'Name': 'Alice', 'Age': 25},
        'row2': {'Name': 'Bob', 'Age': 30}}
df5 = pd.DataFrame.from_dict(data, orient='index')
print(df5)

# Floor Division
print(67//8)

# Bitwise Operators.
m = 5
n = 3
READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1

#Bitwise AND
UserPermission = 6
if (UserPermission & READ_PERMISSION)  == WRITE_PERMISSION:
    print("Can Read")
else:
    print("Cannot Read")
print(UserPermission & READ_PERMISSION)

#Bitwise OR
print(m|n) # Output: 7 (Binary: 0111)
READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1
userPermission = READ_PERMISSION | WRITE_PERMISSION
userPermission |= EXECUTE_PERMISSION
print(userPermission)
print(bin(userPermission))

#Bitwise XOR (Exclusive OR)
print(m^n) #Output: -6 (Invert bits)
userPermission = READ_PERMISSION | WRITE_PERMISSION
userPermission ^= WRITE_PERMISSION
print(f" The new userPermission is: {userPermission} and its binary value is: {bin(userPermission)}")

print(~5) # The not operator gives th opposite value of each of the bit of a number.

#  The Right and Left shift operators shifts the bits either to the left or right of the number depending on the number of the shift you want to shift it.
print(5<<2)
print(20>>2)


#the gzip function is used to import compressed files in python
import gzip

import numpy as np

# Create a 1D numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)

# Perform element-wise operations
b = a * 2

print("Original array:", a)
print("After multiplication:", b)

# Calculate the mean of the array
mean_a = np.mean(a)
print("Mean of the array:", mean_a)


#Importing files in pycharm
import pandas as pd

# Load the CSV file
df = pd.read_csv("D:\\Study\\Rapic Tech Skills\\Data Science\\worldometer_data.csv")

# Check the first few rows of the data
print(df.head())
df.info()
#Working with pickle files
clothes = {
    "shirt" : ["Red", "M"],
    "sweater" : ["Green", "L"],
    "jacket" : ["White", "S"]
}
print(clothes)

# Importing Data from SQL Databases
import pandas as pd



#Sorting Even though the DataFrame in many ways behaves similarly to a dict, it also is ordered. Therefore, we can sort the data in it. Pandas provides two sorting methods, sort_values and sort_index.

data1 = pd.read_csv("D:\\Study\\Rapic Tech Skills\\Data Science\\worldometer_data.csv")
data2 = pd.read_csv(r"D:\\Study\\Rapic Tech Skills\\Data Science\\worldometer_data.csv")
data3 = pd.read_csv(r"D:/Study/Rapic Tech Skills/Data Science/worldometer_data.csv")
data4 = pd.read_csv("D:/Study/Rapic Tech Skills/Data Science/worldometer_data.csv")
print(data1.head())
print(data2.tail())
print(data3.head())
print(data4.tail())
data1.head()

#How to load data into python using the custom functon.
import pandas as pd

with open("D:\\Study\\WorldQuat Data Science\\Data\\tt.csv", "r") as f:
    colum_names = f.readline().strip().split(",")
    data = []
    for j in f:
        tt = j.strip().split(",")

        if len(tt) == len(colum_names):  # Append the row only if it matches the expected number of columns
            data.append(tt)
df = {colum_names[i]:[row[i] for row in data] for i in range(len(colum_names))}
df = pd.DataFrame(df)
print(df)


#Dictionary comprehension
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]


my_dict = {k:v for (k,v) in zip(keys, values)} # Using the help of the zip() function
print(my_dict)

my_dict1 = {keys[i] : values[i] for i in range(len(keys)) }
print(my_dict1)
my_dict2 = {keys[i] : values[i] for i in values for i in range(len(keys)) }
print(my_dict2)

#Dictionary comprehension using a condition using if statement
new_dict = {x:x**2 for x in range(20) if x**2 % 4 != 0}
print(new_dict)

new_dict1 = {x:x**2 for x in range(20+1) if x**2 % 4 == 0}
print(new_dict1)

m = "TON"
newdict = {x : {y : x for y in m} for x in m}
print(newdict)

info = """{"column1": [1, 2, 3, 4, 5], "column2": [66.3, 54.43, 543.4, 543.6, 54334], "column3": [6, 3, 7, 32, 7]}"""
print(type(info))

info1 = json.loads(info) #Load json string into python dictionary
print(type(info1))
info2 = json.dumps(info1) #Convert the python dictionary into jason string
print(type(info2))

dataframe1 = pd.DataFrame.from_dict(info1, orient= "index")
print(dataframe1)


import pandas as pd
data = pd.read_csv("D:\\Study\\WorldQuat Data Science\\Data\\brasil-real-estate-2.csv", encoding = "latin")
#print(data.head()) #print the first five rows of the data.
print(data.index[:5]) #This retrieves the index of the DataFrame, which is essentially the row labels. By default, the index is an integer-based range starting from 0. [:5] Slices notation selects the first five elements of the index.
print(data.shape) #To tell the data shape of the dataframe(the number of rows and columns).
print(data.head()) #Print the first five rows of the data.
print(data.loc[2]) #print the third row of the data
print(data["state"])

dictionary = {"names": ["Anto", "Toni", "Tonito"],
"Ages" : [44, 24, 53],
"State" : ["New york", "LA", "Chicago"]
}
dictionary1 = pd.DataFrame(dictionary)
print(dictionary1.loc[2, "Ages"])
print(dictionary1.iloc[:, [1,1]])




import pandas as pd
data = pd.read_csv("D:\\Study\\WorldQuat Data Science\\Data\\brasil-real-estate-2.csv", encoding = 'latin1')
#print(data.head()) #print the first five rows of the data.
print(data.index[:5]) #This retrieves the index of the DataFrame, which is essentially the row labels. By default, the index is an integer-based range starting from 0. [:5] Slices notation selects the first five elements of the index.
print(data.shape) #To tell the data shape of the dataframe(the number of rows and columns).
print(data.head()) #Print the first five rows of the data.
print(data.loc[2]) #print the third row of the data
print(data["state"]) #Access the column name using the column name as the key.
print(data.state) #Access the column by the use of the column name.
print(data[["state", "region", "lat"]]) #Accessing the multiple column from the data.
print(data.loc[:, "state"]) #Access the column using loc function
print(data.iloc[:, 1]) #Access the column using the function .iloc
print(data.loc[3:10]) #Access the rows for the third to tenth
print(data.columns) #checking for the dataframe columns
print(data.size)
print(data.tail()) #print the last five rows in a data
print(data.info()) # The info() function tells all sorts of things about the data.
print(data.sort_values("lat")) #Sort the data by the value latitude of the column
print(data.set_index("state").sort_index().tail()) #Sort the data by its index.
print(data.sort_values(by = "lat", ascending=False)) #Sort the column name lat by descending order.
print(data.sort_values(by = ["lat", "lon", "area_m2", "price_brl"]).head()) #Sort multiple columns
print(data.sort_values(by = ["lat", "lon", "area_m2"], ascending = [True, False, True], na_position= "first"))#Sort multiple columns with their specification and also NaNs at the beginning.
print(data.sort_values(by = "state", key = lambda x:x.str.len(), ascending=True)) #Custom sorting where sorting is done based on the length of the column name.
data["log_lat"] = data["lon"]/data['lat'] #Adding another column to the DataFrame
print(data.head())
print(data.drop("state", axis = "columns")) #drop the column for state
print(data.drop(2, axis = "index")) #Drop the third row in the dataframe
print(data.dropna(inplace = True)) #
print(data.dropna(inplace = False)) #



