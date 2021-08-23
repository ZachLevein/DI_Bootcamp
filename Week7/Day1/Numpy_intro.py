import numpy as np

#Turning a Python list into a Numpy Array
array_list = [2, 4, 6, 8, 10, 12]
numpy_arr = np.array(array_list)

numpy_arr.shape

np.arange(start=1, stop=10, step=3)


#Reshaping dimension with NumPY 

# (3row and 2 columns)
numpy_arr_reshape_multi_diemnsional = numpy_arr.reshape((3, 2))

# (2row and 3columns)
numpy_arr.reshape((2, 3))

#Indexing & Slicing:
# Selecting by Index is the same as with a reg Python list
numpy_arr[1]

# To select a specified colum from a multi diemsional list:
numpy_arr_reshape_multi_diemnsional[:, 1]

# Mathmatical Functions:
np.mean(array_list)
np.median(array_list)

numpy_arr.min()
numpy_arr.max()

# Mathmatical Operations: 
# Add a number to each element
numpy_arr + 5
# To raise each element to the power 
numpy_arr ** 2

