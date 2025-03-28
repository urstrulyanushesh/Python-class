# Encapsulation -> The Process of hiding the attrutes in the class 
# access modifier -> public - a, protected - _a, private - __a
# a, _a, __a

class Encap:
    def __init__(self,a,b,c):
        self._a = a   # protected
        self.__b = b    # private
        self.c = c      # public
        
    def getInfo(self):
        # self.__b = 100
        print(f"a= {self._a} b = {self.__b} c ={self.c}")
        
    
    # Changes values of private data 
    def changeValue(self, b):
        self.__b = b
        
obj = Encap(10,20,30)
print(obj._a)
print(obj.c)
obj.getInfo()
obj.changeValue(100)
obj.getInfo()
# print(obj.__b)


# Wap to add 3 number using oop Encapsukation make 2 value private change the value in at first and then add

class AddNumber:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.z = z
        
    def changeValue(self,x,y):
        self.__x = x
        self.__y = y
        
    def showData(self):
        print(f"x= {self.__x} y = {self.__y} z ={self.z}")
        
    def addData(self):
        return self.__x + self.__y + self.z
        
data = AddNumber(10,20,30)
data.showData()
data.changeValue(50,70)
data.showData()
print(data.addData())




# Abstraction

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def details(self):
        pass

    
class Ford(Car):
    def details(self):
        return "Car is Ford"
        
        
obj3 = Ford()
print(obj3.details())


# Inheritance -> Parents properties access by child class

class Parent:
    def details(self):
        print("This is parent class")
        
class Child(Parent):
    def details(self):
        super().details()
        
    
obj4 = Child()
obj4.details()



# Practise
class Car:
    def start(self,name,age,model):
        print("The Car is started.")
        print(f"The {name} has {model} model manufactured in {age}")
        
class Tesla(Car):
    
    def __init__(self,name,age,model):
        self.name = name
        self.age = age
        self.model = model
    
    def start(self):
        super().start(self.name,self.age,self.model)
        print("Tesla car is being started")
    
obj5 = Tesla("Tesla",2025,"Tesla Model X")
obj5.start()



class Cars:
    def show(self):
        print("This is parent class Car")

class Bikes:
    def show(self):
        print("This is parent class Bike")

class Details(Bikes, Cars):
    def showDetails(self):
        Cars.show(self)
        Bikes.show(self)
        print("This is child class")
        
obj6 = Details()
obj6.showDetails()



class A:
    name1 = "Em Esh"
    def show1(self):
        print("Parent Level one")
        
class B(A):
    name2 = "Em Esh Thapa"
    def show2(self):
        print("Parent Level Two")
        
class C(B):
    name3 = "Em Esh Thapa Magar"
    def show3(self):
        print("Parent Level Third")
        

obj6 = B()
obj6.show1()
obj6.show2()
print(obj6.name1)
print(obj6.name2)
obj7 = C()
obj7.show1()
obj7.show2()
obj7.show3()
obj8 = A()
obj8.show1()



# hiearchy

class GP:
    last_name = "Magar"
    def show(self):
        print("Grand Parents")
        
class P(GP):
    def shows(self):
        print("GrandParents -> Parents")
        
class C(GP):
    def showss(self):
        print("GrandParents -> Parents -> Child")
  
obj9 = P()
print(obj9.last_name)
obj9.show()
obj9.shows()
obj10 = C()
print(obj10.last_name)      
obj10.show()
obj10.showss()

