#Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for i in zip(keys, values):
  tuple = i
  print(tuple)

#Exercise 2 : Cinemax #2
price = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key, value in family.items():
    name = key 
    age = value
    if age < 3:
        price = 0 
    elif age < 12:
        price = 10
    elif age <= 50:
        price = 15
    print("For", (name), "the price is", (price))

#Exercise 3: Zara

brand = {"name": "zara", "creation_date": 1975, "creator_name": "Amancio", "number_stores": 7000, "type_of_clothes": ["men" , "women", "childeren", "home"], "competitors":["gap", "h&m", "benetton"], "major_color":{

    "france":"blue", 
    "spain": "red", 
    'usa': 'green'
}}
#Change the Number Of Stores 
brand["number_stores"] = 2
print(brand["number_stores"])

#Write a sentence re who their customers are
unpack_customers = tuple(brand["type_of_clothes"])
print('Zaras main clients are ', (unpack_customers))

#Add a  NEW key called country_creation:
brand['country_creation'] = 'spain'

#Add another comptetitor
brand['competitors'] + 'Deigual'


#Delete the information about the date of creation.
del brand["creation_date"]

#Print the last international competitor.
print(brand['competitors'][2])

#Print the major clothes colors in the US.
print(brand['major_color']['usa'])

#Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

#Print the keys of the dictionary.
print(brand.keys())

# Create another dictionary called more_on_zara with the following details:
more_on_zara ={
    "creation_date": 1975, 
    "number_stores": 10000
    }


#Excersise 4: 
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
