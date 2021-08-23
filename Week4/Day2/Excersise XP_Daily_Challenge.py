#Exercise 1 : Favorite Numbers
my_fav_number =  {2, 4, 6, 8, 10}
my_fav_number.add(7)
my_fav_number.add(11)
my_fav_number.remove(10)
print(my_fav_number)
friend_fav_numbers = {1, 3, 5, 7, 9}
our_fav_numbers = my_fav_number.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
#Answer = NO

#Exercise 3: Print A Range Of Numbers
numbers = range(0,21)
for number in numbers:
    print(number)

#Exercise 4: Floats
#Float is a precise number with a Decimal 
list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

#Exercise 5: Shopping List
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.index("Blueberries")
basket.pop(2)
basket.insert(2, "Kiwi")
length = len(basket)
basket.insert(0, "Apples")
appleCount = basket.count("Apples")
print(appleCount)
print(length)
print(basket)

#Exercise 6 : Loop
name = "zach"
while True:
    userInput = input("Enter Your Name:")
    if userInput== name:
        break   
else: 
    print(userInput)

#Excercise 7:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers: 
 if number % 2 == 0: 
     print(number)

#Exercise 8:
digits = range(1500, 2500)
for digit in digits:
    if (digit % 5 ==0) and (digit % 7==0):
        print(digit)


#Exercise 9: Favorite Fruits
userFruit = input("Name Somefruits: (seperate with a single space) ")
userFruitList = userFruit.split(" ")
bool = False

secondFruit= input("Your favortie fruit :" )

if secondFruit in userFruitList:
    print("You chose your favortie")
else: 
    print("You chose a new fruit!")

#Exercise 10: Who Ordered A Pizza ?
saved_toppings = []
while True: 
    toppings = input("What topping do you want: ('quit' to end)")
    print(toppings)
    saved_toppings.insert(1,toppings)
    if toppings == "quit":
        break
    else: 
        print("We will add " + (toppings) + " to your pie")

print("We will pt the following toppings to your pie: ")
print(saved_toppings)
total_price = len(saved_toppings) * 2.5 + 7.5
print("Total price is:") 
print(total_price)

#Exercise 11: Cinemax

amnt_atendees = 0
atendees = 0
age = 0
price = []
cancel = 666
run = True 

while run ==True :
    age= int(input(" Enter Age: "))
    atendees += 1
    if age < 3:
        price.insert(1, 0)
    elif age < 12:
        price.insert(1, 10)
    elif age == 12:
        price.insert(1, 15) 
    elif age == 666:
        break

total_price = sum(price)
print("The total price for " + (str(atendees)) + " people attending this movie is $" + (str(total_price)))


#Exercise 13 & 14 :
sandwich_orders = ["tuna", "salami", "turkey", "avocado", "pastrami","pastrami","pastrami",]
finished_sandwiches = []
final_sandwich_orders = set(sandwich_orders)
print(final_sandwich_orders)
print("Run Out Of Pastrami:")
final_sandwich_orders.remove("pastrami")
     
     
     
for final_sandwich_order in final_sandwich_orders:
    finished_sandwiches.insert(0, final_sandwich_order)
    print("i made you a "+finished_sandwiches[0]+ " sandwich")




