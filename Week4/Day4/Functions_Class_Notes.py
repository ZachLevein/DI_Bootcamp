#  --------------
#  | Functions: |
#  --------------
#Example 
def my_function():
  print("Hello from a function")

my_function()

#Example Of A Function That Accept More Than One Argument(order must match up)
def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "FR")


#Returning More Than One Value With A Tuple
def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

#Returns a tuple
format_name("zach", "levein") 
#Unpacking the tuple
first, last = format_name("RICk", "MORTY")
print(first)
print(last)

#Class Excersise 1: 
def calculation(num1, num2 ):
    addition = num1 + num2
    subtract = num2 -  num1
    return ("Added together:", addition, "Subtracted together:",  subtract)
calculation(5, 7)

#Another Way of writing ^^
def calculation2(a, b):
    return a-b, a+b, a*b
res = calculation2(40, 10)
print(res[0])
print(res[1])
print(res[2])

#Passing List As Function Arguments
def greet_users(users):             # users should be a list
    for user in users:              # Because it's a list, we can loop through it
        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

usernames = ["steve", "stan", "debbie"]
greet_users(usernames)

#If you want to prevent a function from modifying a list, pass my_list.copy() instead of my_list in the arguments.


#*Args - To pack and unpack mutiple values 
def check_multiple_arguments(*args):
    return sum(args)

print(check_multiple_arguments(10,20,100,30))

#**Kwargs - packs the return into a dictionary
def  check_keywordedarguments(**kwargs):
    print(kwargs)

check_keywordedarguments(name="Sarah", age=24)

#unpacking the KEY and VALUE 
def check_keywordedarguments(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

check_keywordedarguments(name="Sarah", age=24)

#The Map() Function - executes the function on everry object in a list and returns as a new list 

def upper_string(s):
    return s.upper()

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(upper_string, fruit)

print(list(map_object))
#>> ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']

#The Filter() Function (returns a new list that meets filter req)

def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(starts_with_A, fruit)

print(list(filtered_object))
#>> ['Apple', 'Apricot']

#Excersise 2: Say hello to everyone whos nam is less or equal to 4 letters 



