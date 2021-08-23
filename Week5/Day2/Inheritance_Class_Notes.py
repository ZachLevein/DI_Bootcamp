# Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.

class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)






#Polymorphism
class Parrot():
    
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
# >> Parrot can fly

flying_test(peggy)
# >> Penguin can't fly


class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")
  
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()



from random import randint 
class Door():
    def __init__(self):
        self.__is_opened = bool(randint(0,1))
    def status(self):
        print(f'the door is { "open" if self.__is_opened else "closed"}')
    def open_door(self):
        self.__is_opened = True
    def close_door(self):
        self.__is_opened = False
class BlockedDoor(Door):
    block_message = 'This door is blocked and cannot be used'
    def open_door(self):
        print(self.block_message)
    def close_door(self):
        print(self.block_message)


        




#ABSTRACT - esitt only to be inherited never INISTALED
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass