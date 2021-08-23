import numpy as np 
from numpy import random
import pandas as pd
from dateutil.parser import parse
from pandas.core.frame import DataFrame

# #Excersise 1: Write a function to create a numpy array using only the input: start, length, and stop.
# Use the function to create an numpy array of length 100, starting from 6 and has a step of 4 between consecutive numbers

def ex_1():
    a = np.arange(6, 100, 4)
    return a
ex_1()



# Excersise 3: Write a function to create a numpy array using only the input: start, length, and stop.
list = np.random.randint(100, size=30).reshape((5, 6))
print(list)
list.max()

# Excersie 5: use a pandas Series function to find the unique values and their frequencies of the following Series:
series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

series = series.map(lambda x: parse(x))
print("Day of Month:")
print(series.dt.day.tolist())
print("Day of Week:")
print(series.dt.dayofweek.tolist())
print("Week Number: ")
print(series.dt.weekofyear.tolist())


#Excersise 6: 
data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
data.shape
data.Length.unique()
# THERE ARE 27 COLUMS AND 92 ROWS
pd.DataFrame.rename(data, columns={'Type' : 'Car Type'})

# Excersise 7: 
data = pd.DataFrame.drop(data, columns={'Length'})
data.Length.unique()


# Excersise 8: 
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

df3 =pd.merge(df1, df2, on=['price', 'price'])

df3 = pd.DataFrame.drop(df3, columns={'pazham', 'kilo'})
df3.head()

# Excersie 9: 
df = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])

df.row.str.split(',|\t', expand=True)