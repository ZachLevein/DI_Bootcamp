
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
cat1 = Cat('linda', 12)

cat2 = Cat('john', 3)

cat3 = Cat('paul', 1)

#Excersise 2: 
class Dog():
    def __init__(self, name, height):
        self.name = name 
        self.height = height
    def bark(self):
        print(f"{self.name} goes WOOF")
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height}cm")
davids_dog = Dog('Rex', 50) 
print(davids_dog.name) 
print(davids_dog.height)
davids_dog.jump()
davids_dog.bark()

sarahs_dog = Dog('Teacup', 20) 
print(sarahs_dog.name) 
print(sarahs_dog.height)
sarahs_dog.jump()
sarahs_dog.bark()

if sarahs_dog.height > davids_dog.height:
    print("Sarahs dog is bigger")
else:
    print("Davids dog is bigger")

#Exercise 3 : Who’s The Song Producer?
class Song():
    def __init__(self, words):
        self.words = words
    def singmeasong(self):
       print(tuple(self.words))

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.singmeasong()


# Exercise 4 : Afternoon At The Zoo

class Zoo():
    def __init__(self, zooName):
        self.zoo = zooName
        self.animals = [ ]
    def add_animal(self, new_animal):
        for i in new_animal:
            self.animals.append(i)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        sold_list = []
        sold_list.append(animal_sold)
        print(f"You have sold the following: {sold_list}")
        print(self.animals)
    def sort_animals(self):
        print(sorted(self.animals))
        first = []
        for i in self.animals: 
            print(i)
            if i[0] == i[0]:
                first.append(i)
                    
        print(first)
            
            
        
animal_list = ['lion', 'cougar', 'cat', 'eel', 'emu', 'bear', 'babbon', 'cougar' 'python', 'anaconda', 'aqua', 'trex' 'tarantula', 'zebra', 'zealot']
Saf = Zoo("SafariPark")
Saf.add_animal(animal_list)
Saf.get_animals()
Saf.sell_animal('lion')
Saf.sort_animals()
