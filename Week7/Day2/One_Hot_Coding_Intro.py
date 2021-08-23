import pandas as pd 
import numpy as np
import random





# Ordinal Features  - Creating Encoded Ranks
rank_list = ['Great', 'Okay', 'Bad', 'Poor'] 
items = pd.Series([random.choice(rank_list) for i in range(100)])

size_dict = {'Poor': 0, 'Bad':1, 'Okay':2, 'Good':3, 'Great':4}
encoded_items = items.map(lambda x: size_dict[x])
pd.DataFrame({"Rank":items, "Encoded Rank":encoded_items})

# Nominal Features:
# One-Shot-Encoding
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
pd.get_dummies(df, columns=['species'])

# Target Encoding: 
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
cars_df = pd.read_csv(url).dropna(subset=['Manufacturer', 'Price'])
# There’s a lot of features here, but our focus will be on two. Let’s say we want to predict the price, so Price will be the target variable. Manufacturer is a nominal feature and we can use target encoding to transform it to a numerical value.
cars_df.head()
means = cars_df[['Manufacturer', 'Price']].groupby('Manufacturer').mean()
cars_df['Manufacturer_transformed'] = cars_df['Manufacturer'].dropna().apply(lambda x: means.loc[x, "Price"])
cars_df[['Manufacturer', 'Manufacturer_transformed', 'Price']].head()

# Continuus Features: 
from sklearn.preprocessing import MinMaxScaler, StandardScaler
s_scaler = StandardScaler()
s_scaler.fit_transform(cars_df._get_numeric_data())[0:2]

mm_scaler = MinMaxScaler()
mm_scaler.fit_transform(df._get_numeric_data())[0:2]
# You can see in both cases that the data is now in a very close range and this will lead to much better ML predictions.



# def load_data():
#     return pd.read_csv('C:/Users/User/Downloads/deals.csv')

# df = load_data()
# df.head()

# # Turning the categorical data in the names column into a binry vector
# pd.get_dummies(df.Name)
# df.shape

# df2 = pd.DataFrame({'country': ['russia', 'germany', 'australia','korea','germany']})
# pd.get_dummies(df2['country'], prefix='country')