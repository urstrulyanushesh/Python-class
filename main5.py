# OOP in python

# It is a programming pradishim
# Real life example lai liyera class and object ma convert garinxa


# Properties
# class and object
# methods
# self -> this
# 4 pillars -> encap, inheritance, polymorphism, abs
# dunder methods
# class meta
# abstract class


# class -> it is a blueprint
# object -> instance of a class 

class Colony:
    # properties, Fields
    let = 0
    name = "Em Esh"
    

house1 = Colony()
print(house1.let)
print(house1.name)

house2 = Colony()
house2.let = 1
house2.name = "Dilip MD"
print(house2.let)
print(house2.name)




class Kist:
    faculty = "deprt"
    head = "Name"
    sem = 0
    
    def __init__(self,faculty,head,sem):
        self.faculty = faculty
        self.head = head
        self.sem = sem
        
        print(f"{faculty} {head} {sem}")
        
bit = Kist("BIT","Em Esh",5)


class Kist:
    faculty = "deprt"
    head = "Name"
    sem = 0
    
    def __init__(self):
        
        print(f"Call Itself")
    
bit = Kist()


class Add: 
    def __init__(self,a,b):
        self.a =a
        self.b =b
        
        print(a+b)
        
    def AddNumber(self,c):
        print(self.a+self.b+c)
    
add = Add(3,5)
add.AddNumber(2)



# WAP in oop about the class name students with the following options need to make a constructor 
# with the value of name, age, gender and batch need to make 3 methods which will add two number to add a,b
# 2nd methods which will print name and age
# last one print the gender and batch

class Student:
    def __init__(self, name, age, gender, batch):
        self.name = name
        self.age = age
        self.gender = gender
        self.batch = batch
        
    def AddNumber(self,a,b):
        print(a+b)
        
    def NameAge(self):
        print(f"Name = {self.name} and age is {self.age}")
        
    def GenderBatch(self):
        print(f"Name = {self.gender} and age is {self.batch}")
        
s = Student("Em Esh", 23, "Male", 2023)
s.AddNumber(7,10)
s.NameAge()
s.GenderBatch()


# Static Methods

class One:
    @staticmethod
    def abc(a,b):
        return a+b
    
print(One.abc(22,16))

    
class Two:
    @classmethod
    def cdf(cls,a,b):
        cls.a = a
        cls.b = b
        print(a+b)

Two.cdf(5,5)



class Age:
    @staticmethod
    def ages(age):
        if age>18:
            print("Can Drive")
        else:
            print("Can not Drive")
     
Age.ages(6)