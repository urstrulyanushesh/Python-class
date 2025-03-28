# functions


def function():
    return "Hello World"
    
print(function())


# using pass keyword
def passName():
    pass

print("Dilip Bhai")


# Parameter in function

def abc(a,b):
    return a+b

print(abc(4,5))



def abcd(a):
    print(a)
    
print(abcd(1))


def even_odd(a,b):
    for i in range(a,b):
        if i%2==0:
            print(f"Even {i}")


a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

print("Type ",type(a))
even_odd(a,b)


# Function Types
# no parameter no return
def function1():
    print("Dilip Bhai")
    
# with parameter no return
def function2(a,b):
    print("Lalu bhai")
    
# with parameter with return
def function3(a,b):
    return a+b

    
# no parameter with return
def function4(a,b):
    return a*b

function1()
function2(3,4)
print(function3(a,b))
print(function4(a,b))


# parameter type in python
# 1. Default
# 2. named
# 3. *args
# 4. **kwargs
# 5. positional argument  --> give value to the arg as you write in parameter


def abc(name,age):
    print(f"Name = {name} and age = {age}")
    
abc("Em Esh",34)


def abc1(name,age):
    print(f"Name = {name} and age = {age}")
    
abc1(age = 20,name = "Em Esh")


def abcd2(*data):
    for i in data:
        print(i)
abcd2("Em Esh",1,2,3)  # --> is send as a tuples


def abc(**details):
    for keys, values in details.items():
        print(keys, values)
        
abc(name = "Em Esh" , age = "23", gender = "isMale")


def abcd():
    print("Hello")
    return "ok"
    print("Data")
    
print(abcd())


# Prime or Composite in function
def prime(number):
    count = 0
    for i in range(1,number+1):
        if number % i==0:
            count+=1
        else:
            continue

    if count == 2:
        # print(count)
        print("It is a prime")
    else:
        # print(count)
        print("It is composite")
    
number = int(input("Enter a number : "))
prime(number)



# lambda function
function = lambda x,y:x+y

print(function(6,4))



