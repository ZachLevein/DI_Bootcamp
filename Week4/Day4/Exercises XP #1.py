
# Exercise 1 : What Are You Learning ?
def display_message():
    print("I am learning compute programming")
    return

display_message()

#Exercise 2: What’s Your Favorite Book ?

def favorite_book(title):
    print("My fave book is ", title)
    return
favorite_book("param")

#Exercise 3 : Some Geography
 
def describe_city(city, country= "Israel"):
    print(city, "is in", country)
    return 
describe_city("London")

#Exercise 4 : Random
import random
def number_acceptor(num1):
    random_num = random.randint(1, 100)
    if num1 == random_num:
        print("SUCCESS - You guessed Right!")
    else: 
        print("FAIL!! The Correct Number was:", random_num, "and you gussed:", num1)
        return 
number_acceptor(25)

#Excersise 5: Lets Create SOme Personalized Shirts! 
def make_shirt(message, size ="Large"):
    print('Your shirt message will be:', message, 'Size:', size)
    return 
make_shirt("I like food", "Medium")

#Exercise 6 : Magicians
def show_magicians(magicians):
    for magician in magicians: 
        print(magician)
magicians_list = ['Gandalf', 'Saroman', 'Harry Potter']
show_magicians(magicians_list)

def make_great(magicians):
    for magician in magicians: 
        print(magician, 'the great')
make_great(magicians_list)

print(magicians_list)

#Exercise 7: When Will I Retire ?
male = "male"
female = "female"

def get_age(year, month, day):
    return 2021 - year
age = get_age(1947, 6, 20)

def retire(gender, ages):
    if gender == male  and age >= 67:
        can_retire = True
    elif gender == "female" and age <= 74:
        can_retire = True
    else: 
        can_retire = False
    if can_retire == True:
        print("You CAN retire")
    else: 
        print("You can NOTT retire")
    
retire("female", age)
print(age)

#Excersise 8:
# def calculator(num):
#     for i in range(num):
#         for j in range(i+1):
#             print(num, "+",  end=" " )
#         print(" ")

    
# calculator(3)


def digits(n):
    sum = 0
    # this is the multiplier.
    # throughout the iterations it will be 1, 11, 111, 1111 ...
    repeater = 1
    for i in range(n):
        print(repeater *n, "+ ", end= "" )
        sum += n*repeater
        repeater = repeater*10+1
    return print( "=", sum)
digits(5)

#Daily Challenge
import re
matrix = [
    [7,'I',3],
    ['t','h','i'],
    ['s', '%', 'x'],
    ['i', '#'],
    ['s', 'm'],
    ['$', 'a'],
    ['#', 't', '%'],
    ['^', 'r', '!']
]
#Loopinbg through the 2d list to get everything in one colum
def deGrid():
    list = []
    for row in matrix:
        for col in row:
           list.append(col)
    return list          
deGrid()

import string
alpha = list(string.ascii_lowercase)

def removeShit(letter):
   if(letter in alpha ):
       return True 
   else:
       return False

removeShit= filter(removeShit, deGrid())
print(list(removeShit))


a = 0
b = 5
c = 2 

a += b+c
print(a)