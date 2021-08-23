import pandas as pd 
import numpy as np
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
pd.DataFrame({"Rank":ordinal, "Encoded Rank":encoded_items})

# This value is continuous so I am going to scale it for ML 
df['Ticket'].describe()
list= []
continuous = np.array(df['Ticket'])
for i in continuous: 
    list.append(i)
    s_scaler = StandardScaler()
s_scaler.fit_transform(list._get_numeric_data())[0:2]

