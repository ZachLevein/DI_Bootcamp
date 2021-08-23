# Exercise 3 : Dogs Domesticated

import random
from Excersise_XP import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super(). __init__(name, age, weight)
        self.train = False
        self.other = ' '
    def training(self):
        print(self.bark())
        if self.train == False:
            self.train = True
    def play(self, *other):   
        self.other = other
        print(f"{self.other} all play together ")
    def do_trick(self):
        tricks = [f' {self.name} does a roll',  f' {self.name} stands', f'{self.name}  does a back flip', f'{self.name} jumps up super high']
        if self.train == False:
            print(f'{self.name} is not trained')
        else:
         print(tricks[random.randint(0, 3)])
dog4 = PetDog('john', 22, 28)
dog4.training()
print(dog4.train)
dog4.play("max", 'ruby', 'sacha')
dog4.do_trick()

