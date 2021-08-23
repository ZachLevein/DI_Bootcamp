import numpy as np 
import pandas as pd 
 
# Reading a file with Panda
sheet = pd.read_csv('C:/Users/User/Downloads/deals.csv')

# HEAD() first 5 rows of the file to get a feel for the structure of the file
sheet.head()

# Using Numpy SHAPE to tell us how many rows and columns the file has
sheet.shape

# Using INFO to see datatype of each colum 
sheet.info()
sheet.describe()

# Data Selction & Indexing: 

# To see all the unique values in a specified colum
sheet.amount.unique()

# Filtering in Pandas uses Boolean masking.
# The statement in the brackets is a boolean mask
sheet[sheet.Stage == 'funded']

# Sorting: 
sheet.sort_values('amount', ascending=False)

# Grouping:
sheet.groupby('amount').apply(np.min)

#Renaming a Column: 
pd.DataFrame.rename(data, columns={'Type' : 'Car Type'})
# Delete: 
data = pd.DataFrame.drop(data, columns={'Length'})
