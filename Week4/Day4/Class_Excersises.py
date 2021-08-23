
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
magicians = ['Gandalf', 'Saroman', 'Harry Potter']
def show_magicians(magic):
    for magician in magicians: 
        print(magician)
        return
magicians = ['Gandalf', 'Saroman', 'Harry Potter']
show_magicians(magician)


