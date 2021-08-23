import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#Plotting a graph 

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('first graph')
plt.show()


sheet = pd.read_csv('C:/Users/User/Downloads/deals.csv')
sheet.head()
# "r--" argument. This is a format string, which gives the options to style and color the plots.
plt.plot(sheet['Term'], sheet['Funded'], "r--")
plt.show()

plt.scatter(sheet['Term'], sheet['Funded'])
plt.xlabel('Term Length (months)' )
plt.ylabel('Funded Amount')
plt.grid()