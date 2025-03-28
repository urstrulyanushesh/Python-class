# Logical  -> and

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Logical  -> or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Logical  -> not
print(not True)
print(not False)


# bitwise operator


# Ternary Operator

a = 25
ab = "Greatest" if a>10 else "Lowest"
print(ab)

# WAP in ternary operator to find the number is even or odd
a = 10
print("Even" if a%2==0 else "odd")


# identifier is, not is 
a = 10
b = 20
c = "10"

print(a is c)
print(a is not c)
print(a is b)
print(a is a)


# List, Tuple, Set, Dictionary
array = [3,6,4,8,2] 

array.append(7)
array.sort()
print(array)
array.reverse()
print(array)

a = array.pop(5)
print(a)

array.insert(2,10)
print(array) 

array.remove(8)
print(array) 

b = array.copy()
array.clear() 

print(array)
print(b)
b[0] = 55
print(b)
# array


# Tuple Method
tuple1 = (1,4,2,3,4,5,6,4,)
print(tuple1)
print(tuple1.count(4))
print(tuple1.index(4))



print(tuple1)
b = list(tuple1)
print(b)

b.append(10)
print(b)
b.insert(0,10)
print(b)

tuple2 = tuple(b)
print(tuple2)


# set
set1 = {1,2,3,4,5,6}
set2 = {7,8,9,10,11,12}

list_set = list(set2)

print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
print(set1.intersection_update(set2))

# Empty Set 
set3 = set()



# Dictionary
dict1 = {
    "name" : "Dilip",
    "age" : 23
}

print(dict1.items())
print(dict1.values())
print(dict1.keys())

for keys, values in dict1.items():
    print(f"{keys} is {values}")


abc = None
print(abc)
    
for i in tuple1:
    print(i)
    
for i in array:
    print(i) 
    
for i in set2:
    print(i)

print(list_set)

