import re

pattern = "[a-zA-Z0-9 +@[a-zA-Z]+\.(com|edy|net)"
user_input = input("Write Here: ")

if(re.search(pattern, user_input)):
    print('Valid Email')
else:
    print("Invalid EMail")
    

    
    