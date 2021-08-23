import json
#Write A Python Dictionary Into A JSON File

sopranos = {
    'management':['Tony', 'Sylvio'],
    "capos": ['jimmy', 'paulie']
}

json_file = 'sopranos.json'

with open(json_file, 'w') as file_obj:
    json.dump(sopranos, file_obj)


# The python function to save an object into a file is :
# json.dump(object_to_save, destination_file)

# Convert A Python Dictionary To JSON String
sopranos2 = {
    'management':['Tony', 'Sylvio'],
    "capos": ['jimmy', 'paulie']
}
json_sopranos2 = json.dumps(sopranos2)
print(json_sopranos2)


# Convert A Python Dictionary To JSON String : Pretty Print

sopranos = {
    'management':['Tony', 'Sylvio'],
    "capos": ['jimmy', 'paulie']
}



json_file = "index.json"

with open(json_file, 'w') as file_obj:
    json.dump(sopranos, file_obj, indent = 2, sort_keys=True)


json_file = 'my_file.json'
with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family)
#>> {'children': ['Summer', 'Morty'], 'parents': ['Beth', 'Jerry']} 


