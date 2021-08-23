user = input("Write a coma seperated sentence:")
print(user)

result = sorted(user.split(', '))
tuple_to_unpack = tuple(result)