# Excersize 1:
# Using a for loop to print the statement 5 times 

for i in range(5):
    print("hello world")

#Excersise 3:
# print(99^3)* 8

# Excersize 4:
computer_brand = "Asus"
print("I have a "  + (computer_brand)  + " computer")

#Excersize 5:
name = "Zach"
age = "21"
shoe_size = 42
info = "My name is " + (name) + "I am " + (age) + " years of age. My feet are size " + (str(shoe_size))
print(info)

#Excersize 6:
a = 20
b = 30 
string = ("helloworld")

if a < 30: 
    print(string)


#Excersize 7"
userNum = int(input("Input a number"))

if userNum % 2 == 0:
    print("{0} is Even".format(userNum))
else:
    print("{0} is odd".format(userNum))


#Excersize 8:
userHeight = int(input("Inset height in Inches: " ))
userHeightCM = userHeight * 2.54

if userHeightCM < 145:
    print("You are not tall enough to ride")
else:
    print("Enjoy the ride you are tall enough")