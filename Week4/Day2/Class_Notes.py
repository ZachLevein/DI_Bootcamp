#Variables
name = "zach" #string 
age = 22 #integer

#Lists 
my_list = [4,3,2, age, name]

# Range indexes return a list from one index to the other (sequence_name[start:end])
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list2[0:4])  # The result gives us the numbers 1-4

#LIST METHODS(After Variable - Variable.method())
#APPEND() - add element to list 
my_list2.append("Hello")

#INSERT() insert at selected index point
my_list2.insert(9, "Hello") 

#remove(value) remove the FIRST occurence of an element value (not INDEX)

#list + list (concatenate two lists into one in the order specified)
new_list3 = my_list2 + my_list

#SORT() - To sort letters and numbers in AL or Num order

#INDEX()- Return Index of specified value



#LIST FUNCTIONS (Before Variable - function(variable))
#len() retrieve the indexnumber of specified 
len(new_list3)

#SORTED()- To sort Numbers and Letters



#Tuple
#Tuples are like lists, but they are immutable - they CANT be changed.
my_tuple = (1+3, 2,3, age, name)

#Single object Tuple (Note the comma is needed at the end)
my_tuple2 = (name,)

#Negative indexes,starting from the end to the beginning (sequence_name[-index_num]) 
my_tuple3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple3[-2])  # The result gives us the number 8

#FOR Loops
fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits:
  print(fruit)

#Establshing the letter varible inside the for statement 
for letter in name:
    print(letter)


cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]
#This line tells Python to retrieve the first value from the list cities and store it in the variable city. The loop will run until each city in cities has been read
for city in cities:
    print("I once went to", city)

#Enumerate - (give the index of a string based value)
for index, city_name in enumerate(cities):
    print(index, city_name)


#Ranges: ( will loop through the spepcified RANGE)
numbers = range(4, 19)
for number in numbers:
  print(number)
print(list(numbers))


#While Loop: 
while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")