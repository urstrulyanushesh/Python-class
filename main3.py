# Conditions and Loop

# Conditions

if False:
    print("This is true")
    
else:
    print("This is False")
    
condition = True  
if condition:
    print("This is true")
    
else:
    print("This is False")
    
    
age = 20
age1 = 18

if age > 18:
    print("He or she is above 18")
    
elif age == 18:
    print("He or she is equal 18")
    
elif age < 10:
    print("Doesn't Count")
    
else:
    print("He or she is below 18")
    

    
if age1 > 18:
    print("He or she is above 18")
    
elif age1 == 18:
    print("He or she is equal 18")
    
elif age1 < 10:
    print("Doesn't Count")
    
else:
    print("He or she is below 18")
    
    
    
# # Match Statement
# def function(a):
#     match(a):
#         case 1:
#             print("Input is 1")
#         case 3:
#             print("Input is 3")
#         case 2:
#             print("Input is 2")
#         case _:
#             print("Other")
        
        

# a = int(input("Enter a number : "))
# function(a)


number = int(input("Enter a number : "))



# Between Odd number
a = int(input("Start Number : "))
b = int(input("Last Number : "))
print("Odd number : ")
for i in range(a,b):
    if i % 2 != 0:
        print(i)

# Between even number
a = int(input("Start Number : "))
b = int(input("Last Number : "))
print("Even number : ")
for i in range(a,b):
    if i % 2 == 0:
        print(i)

# WAP to find a given character is vowel or not:

a = input("Enter a character: ")
vowel = {'a','e','i','o','u'}
if a in vowel:
    print("It is vowel character")
else:
    print("It is not vowel")
    
# To odd or even 
num = int(input("Enter a number: "))
if num%2==0:
    print("It is Even")
else:
    print("It is odd")
    


def Day_Function(day):
    
    match(day):
        case 1:
            print("It is Sunday")
        case 2:
            print("It is Monday")
        case 3:
            print("It is Tuesday")
        case 4:
            print("It is Wednesday")
        case 5:
            print("It is Thursday")
        case 6:
            print("It is Friday")
        case 7:
            print("It is Saturday")
        case _:
            print("Enter a valid number")
    
day = int(input("Enter a Day number: "))
Day_Function(day)


# Month Today
def Month_Function(num):
   
    match(num):
        case 1:
            print("It is Jan")
        case 2:
            print("It is Feb")
        case 3:
            print("It is Mar")
        case 4:
            print("It is April")
        case 5:
            print("It is May")
        case 6:
            print("It is June")
        case 7:
            print("It is July")
        case 8:
            print("It is Aug")
        case 9:
            print("It is Sep")
        case 10:
            print("It is Oct")
        case 11:
            print("It is Nov")
        case 12:
            print("It is Dec")
        case _:
            print("Invalid Month number")
    
month = int(input("Enter a Month number: "))
Month_Function(month)


# Leap year

year = int(input("Enter a year"))
if year %4 == 0 and year%100 != 0:
    print("It is a leap year")

elif year%400 == 0:
    print("It is Leap year")

else:
    print("It is not a leap year")
    
    

# Positive or negative
num1 = int(input("Enter a number : "))
if num1 > 0:
    print("It is positive")
elif num1 < 0:
    print("It is negative")
else:
    print("It is zero")
    
    
# Prime and Composite
number = int(input("Enter a number : "))
count = 0
for i in range(1,number+1):
    if number%i==0:
        
        count+=1
    else:
        continue

if count == 2:
    print("It is a prime")
else:
    print("It is composite")
    
    
