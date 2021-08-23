import random 

class First():
    def __init__(self, chromo=1, dna=1):
        self.chormo = chromo 
        self.dna = dna 
        self.genes = random.randint(0,1)
    def mutate(self):
        self.chromo = self.genes *10
        self.dna = self.chromo *10 
        if random.randint(1,2) == 1:
            self.chromo = self.chromo * 10
            self.dna = self.dna * self.chromo
        return self.chromo, self.dna


test = First()


# chromo, dna = test.mutate()
# print(chromo)
# print(dna)

class Organs(First):
    def __init__(self):
        super().__init__(chromo=1, dna=1)
        self.enviroment = []
    def envir(self):
         a = 1
         while a < 15:
            self.enviroment.append(test.mutate())
    def leng(self):
      print(len(self.enviroment))
                    
test2 = Organs()
test2.envir()
test2.leng()
