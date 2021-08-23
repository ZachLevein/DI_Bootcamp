#Excersise 1:
from os import error
import random 

file = open('Day4\Word_download.txt', 'r')

def get_words_from_file(index=0):
    rand = random.randint(1, 100000) *3
    rand_list = file.readlines()[rand:random.randint(rand, rand*2)]
    list = rand_list[0:index]
    final_list = []
    for element in list:
        final_list.append(element.strip())
    sentence = " ".join(final_list)
    return sentence



def main(value=1):
    value = int(input("Input a number 1:21"))
    if value >= 21:
        raise ValueError("Your numbers are not in range")
    else:
        return value
get_words_from_file(main())


#Excersise 2:
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
parse = json.loads(sampleJson)
# print(parse['company']['employee']['name']['payable'])
name = parse['company']
name['employee']['birthday'] = '1991'
print(name)