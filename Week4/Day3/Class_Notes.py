# ||||||||||||||||||||
# |Nested Dictionary:|
# ||||||||||||||||||||

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
#To Access the KEY for "history"
sampleDict['class']['student']['marks']['history']

#To Change the KEY value of 'history
sampleDict['class']['student']['marks']['history'] = 'fail'

#To delete the KEY for history 
del sampleDict['class']['student']['marks']['history'] 
print(sampleDict)

#Removing Mutiple Keys 
sampleDict2 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keysToRemove = ["name", "salary"]
for key in keysToRemove:
    del sampleDict2[key]
print(sampleDict2)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Enumerate(Iterable): Enumerate Each Item in the loop and return VALUES in TUPLE
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

for item in enumerate('abcd'):
    print(item)

for (index_count, letter) in enumerate('abcd'):
    print('At index {} the letter is {}'.format(index_count, letter))

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |  ZIP - Connect mutiple lists/iterables into one TUPLE |
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

# |||||||||||||||||||||||||||||||||||||||||||||||||
# | List Comprehension: Quick of Creating A List  |
# |||||||||||||||||||||||||||||||||||||||||||||||||

#The standard basic way 
my_number = '1234'
my_list = []

for num in my_number:
    my_list.append(num)
print(my_list)

#List Comprehesion:
my_number = '1234'
my_list = []

my_list = [num for num in my_number]
print(my_list)

#Example with RANGE method
my_list = [x for x in range(0,6)]
print(my_list)


#The Basic Way Of Appending An Element Into A List With Nested Loop
my_list = []

for i in [2, 3, 4]:
    for j in [100, 200, 300]:
        my_list.append(i*j)

print(my_list)

#List Comprehension:
my_list = []
my_list = [(i*j) for i in [2, 3, 4] for j in [100, 200, 300]]
print(my_list)

#  ||| |||||||||||||||||||||||
#  | Dictionary Comprehension|
#  |||||||||||||||||||||||||||

#Syntax:
# dictionary = {key: value for var in iterable}

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
print(family_age.items())

new_year = 1

new_family_age = {name: age+new_year for (name, age) in family_age.items()}

print(new_family_age)