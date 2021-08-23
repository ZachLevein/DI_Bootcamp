class Farm():
    def __init__(self, name):
        self.name = name 
        self.animals = []
        self.amounts = []
      
    
    def add_animal(self, new_animal, amount=1):
        self.animal = new_animal 
        self.animals.append(new_animal)
        self.amount = amount
        self.amounts.append(amount)

    
    
    def get_info(self):
       print(f"{self.name}'s Farm")
       for i, y in zip(self.animals, self.amounts):
           print(i, y)
       print(" E-I-E-I-0!")
        


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()

