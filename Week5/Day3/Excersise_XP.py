# # Excersise 1:
# class Example:
#     """The DOC method is what the PRINT() function uses to return it value"""
#     def do_nothing(self):
#         pass

# print(Example.__doc__)

# #Exercise 2: Currencies

# class Currency():
#     def __init__(self, forex, amount):
#         self.forex = forex
#         self.amount = amount
#     def __repr__(self):
#         return f'{self.amount} {self.forex}s'
#     def __str__(self):
#         return f' {self.forex}'
#     def __int__(self):
#         return self.amount
#     def __add__(self, other):
#         if other >= 1:
#             return self.amount +  other
#         elif other.amount >=1:
#             return self.amount, other.amount
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# str(c1)
# int(c1)
# repr(c1)
# c4= c1 + 5
# c5 =c1 + c2
# c5
# c4
# c1.amount, c1.forex

# XP  Part 2:

# Excersise 1 & 2 & 4:
#Create a function that shows todays date
from datetime import timedelta, datetime, holidays 

jan = datetime(2021,1, 1, 0, 0)
diff = datetime.today() - jan
print(diff)

#Excersise 3:

def birthday_calc(year, month, day, hour=0, min =0):
    birthday = datetime(year, month, day, 0, 0)
    dif = datetime.today() - birthday
    mins = (dif.seconds) *60
    print(f'You have been alice for {mins} minutes')
birthday_calc(1999, 6, 20, 0, 0)

#Excersise  4:
def holiday_calc():
    today = datetime.today()
    holiday = datetime(2021, 9, 6, 0, 0)
    dif = holiday - today 
    print(f'Today is {today} the next holiday is Rosh Hashana on {holiday} which takes place in aprox {dif}')
holiday_calc()

# Excersise5:
dict = {
    'mars' : 1.88, 
    'jupiter' : 11.8,
    'saturn'  :29.44,
    'uranus':84.016,
    'neptune' : 1.64.
    }

# class Planet():
#         def __init__(self, user_age):
#             self.user_age = user_age
#         @classmethod
#         def mutiple(cls):
#             planets = []
#             for i in dict:
#                 planets.append(key)
#             for value in dict:
#                 if i < 1: 

         