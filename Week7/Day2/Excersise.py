from os import replace
import pandas as pd 
import numpy as np
from pandas.core.algorithms import rank
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import random



#Excersize 1: 
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.head()
df.shape
df['Name'].describe()
# Name is a nominal catergorical feature so I have given it a binary vector
pd.get_dummies(df, columns=['Name'])

# Im reviewing this column to see how many unique values there and how many tims they appear
df['Sex'].describe()
df['Sex'].value_counts()
# Sex is a ordinal feauture so I created an encoded rank 
ordinal = df['Sex']
dictionary = {'male': 1, 'female': 2}
encoded_items = ordinal.map(lambda x: dictionary[x])
med =pd.DataFrame({'Sex': ordinal,'Encoded_Rank':encoded_items})
df['Sex'].replace(to_replace='Sex', value= med)
print(med)
df.head()
# Survived & PCLASS is already set up with ordinal encoding
df
# This value is continuous so I am going to scale it for ML 
df['Ticket'].describe()
continuous = np.array(df['Ticket'])

list1 = continuous.tolist()
s_scaler = StandardScaler()
s_scaler.fit_transform(df[['Ticket', 'Age']]._get_numeric_data())[0:2]
# I have made a loop so that I can pull all the continuous values on every row in a scaled MINMAX format
mm_scaler = MinMaxScaler()
for i in range(10):
    mm_scaler.fit_transform(df._get_numeric_data())[0:i]

# The max age is 80 so I will binne the age into ranges
df['Age'].max()
df['Age'].min()
bins = [0, 15, 30, 45, 80]
bin_name = ['infant', 'young-adult', 'midage', 'senior']

df['Binned'] = pd.cut(df['Age'], bins=bins, labels=bin_name, include_lowest=True)
df
df.head()

#I am deleting the Passenger ID column as it is simple to make my own passengerID  when needed 

df = pd.DataFrame.drop(df, columns='PassengerId')
df['Parch'].describe()
df['Parch'].value_counts()
