#Excersise 1:
list1 = [5, 10, 15, 20, 25, 50, 20]

list1.index(20) #= Index 3

list1.insert(3, 200) #= Replace index 3 with value 200

print(list1)

#Excersise 2:

a_tuple = (10, 20, 30, 40)

(ten, twenty, thirty, forty) = a_tuple # Unpacking the tuple by storing the values on new variables

#Excersize 3
user_numbers = int(input("Type a number:"))

for user_number in user_numbers:
  value = user_number * user_numbers

#Excersize 4: 
current_number =1
while current_number <=10:
    print(current_number)
    current_number +=1