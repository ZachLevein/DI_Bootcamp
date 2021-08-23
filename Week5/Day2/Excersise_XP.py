# Exercise 1 : Pets
from random import random


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat(Pets):
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Symese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
cat1 = Bengal('john', 12)
cat2 = Symese('peter', 10)
cat3 = Symese('kate', 8)
cat4 = Chartreux('alex', 6)
my_cats = [cat1, cat2, cat3, cat4]
my_pets = Pets()
print(my_pets.animals)

for i in my_cats:
    print(i.walk())

# Exercise 2 : Dogs
import random 
class Dog():
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight
        self.speed = 1
    def bark(self):
        return(f"{self.name} is barrking WOOF!")
    def run_speed(self,):
        self.speed = int((self.weight/self.age) * 10)
        return(f"{self.name} is running at {self.speed} KMPH")
    def fight(self, other_dog):
       self.other_dog = other_dog
       winner_calc = self.speed * self.weight
       if self.speed * self.weight  > other_dog.speed * other_dog.weight:
           print(f"{self.name} won!")
       else:
            print(f'{self.other_dog.name} won!')
          

dog1 = Dog("max", 12, 29)
dog2 = Dog("will", 11, 55)
dog3 = Dog("harry", 18, 32)       
my_dogs = [dog1, dog2, dog3]

for i in my_dogs:
     battle = i.fight(dog1)
     print(i.run_speed())





