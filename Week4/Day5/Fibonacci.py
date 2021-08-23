#Fibonacci Number Generator
def fib(number):
    a = 0
    b = 1
    for i in range(number):
    
        temp = a
        a = b
        b = temp + b
        yield a



for x in fib(10):
    print(x)

# Function returns a generator when it encounters 'yield'.
def simple_generator():
    z = 1
    yield z
    yield z + 2
    yield z + 3

generator_object = simple_generator()
generator_object  # only generator. no code runs. no value gets returned


for i in simple_generator():
    print(i)

def number_fuck(num):
    a = 0
    b = 2
    for i in range(num):
        yield a 
        c = a 
        print(c )
        a = b 
        print(a)
        c = a+b 
        print(c)
         
        
        
for j in number_fuck(1):
    print(j)