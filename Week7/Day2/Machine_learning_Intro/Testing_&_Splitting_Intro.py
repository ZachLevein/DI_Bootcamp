from os import replace
import pandas as pd 
import numpy as np
from pandas.core.algorithms import rank
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import random
from sklearn.model_selection import train_test_split





#Excersize 1: 
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.head()
df.shape

train, test = train_test_split(df, test_size = 0.15, random_state=42)
len(test)

train.shape
test.shape

test.head()
train.head()
train.describe()

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import csv
music_data = pd.read_csv(r"C:\Users\User\Desktop\DI_Bootcamp\Week7\Day2\Machine_learning_Intro\music.csv")

#Split that Data into input and output 
# Output Set
X = music_data.drop(columns=['genre'])
# Input Set 
y = music_data['genre']
#X_train, X_test = Input sets for test & train 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creating the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
score