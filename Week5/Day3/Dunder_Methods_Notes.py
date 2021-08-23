
#2. The __str__ Method
mylist = [1, 3, 5]
print(str(mylist))

mylist = [1, 3, 5]
print(mylist.__str__())


# 4. The __call__ Method

class Gangster:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __call__(self):
        print (f'Gangster: {self.name}, Movie: {self.movie}')

member1 = Gangster("Sylvio", "Sopranos")
member1()
# Gangster: Sylvio, Movie: Sopranos


# # 4. How To Use The Dunder Methods?
# Example With __repr__()

class GangsterOne:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie

    def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.movie}"
    
    def __add__(self,other):
       return GangsterOne(self.name, other.name)

capo = GangsterOne('Sylvio', "Sopranos")
boss = GangsterOne('Tony', "Sopranos")
#Using the __add__() method
underBoss = boss + capo

print(capo, boss, underBoss)

#Overloading a method 
class GangsterTwo:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie
    
    def __repr__(self):
  
      return f"{self.__class__.__name__} : {self.name} {self.movie}"
    def __add__(self,other):
        name = self.name[0] + other.name[1:]
        movie = other.movie
        return GangsterTwo(name, movie)

boss = GangsterTwo('Vito', 'The Godfather')
otherBoss = GangsterTwo('Tommy', 'GoodFellas')
underBoss = boss + otherBoss
print(underBoss)
print(dir(underBoss))