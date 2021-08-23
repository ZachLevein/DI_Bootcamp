
#Class & Static Method
class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')



# use of class method and static method.
from datetime import date
   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
       
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
   
person1 = Person('zach', 22)
person2 = Person.fromBirthYear('Zach', 1999)
   
print (person1.age)
print (person2.age)
   
# print the result
print (Person.isAdult(22))


#MY.EG @CLASS METHOD
data = [
    {
        'name': 'Tony',
        'film': 'Sopranos',
        'roll' : 'Boss'
    },
    {
        'name': 'Vito',
        'film': 'Godfather',
        'roll' : 'Boss'
    }
]
        
 
class Gangster():
    def __init__(self, name, film, roll):
        self.name = name 
        self.film = film 
        self.roll = roll
    
    @classmethod
    def from_dict(cls, data):
        gangster_list = []
        for row in data:
            gangster = cls(row['name'], row['film'], row['roll'])
            gangster_list.append(gangster)
        return gangster_list

gangsters = Gangster.from_dict(data)
print(gangsters[0].name)
print(gangsters[0].film)

print(gangsters[1].name)
print(gangsters[1].film)

#@STATICMETHOD

#Regular 
class GansterTwo():
    def __init__(self, name):
        self.name = name
    def about(self):
        print(f'I am {self.name}')
    def speak(self, msg):
        print(msg)

g = GansterTwo("Sylvio")
g.about()
g.speak("just when I thought I was out they pulled me back In again")

class GansterThree():
    def __init__(self, name):
        self.name = name
    def about(self):
        print(f'I am {self.name}')
    # I am not using self in the
    def speak(self, msg):
        print(msg)

g = GansterTwo("Sylvio")
g.about()
g.speak("just when I thought I was out they pulled me back In again")