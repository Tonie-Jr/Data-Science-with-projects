import json
import pandas as pd
info = """{"column1": [1, 2, 3, 4, 5], "column2": [66.3, 54.43, 543.4, 543.6, 54334], "column3": [6, 3, 7, 32, 7]}"""
print(type(info))

info1 = json.loads(info) #Load json string into python dictionary
print(type(info1))
info2 = json.dumps(info1) #Convert the python dictionary into jason string
print(type(info2))

dataframe1 = pd.DataFrame.from_dict(info1, orient= "index")
print(dataframe1)



