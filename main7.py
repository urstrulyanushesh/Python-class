# polymorphism

class Cat:
    def speak(self):
        print("Meow")
        
class Dog:
    def speak(self):
        print("Bark")
        
animal = [Dog(),Cat()]
for i in animal:
    i.speak()
    


# Exceptional Handling

# try, throw, else, and finally
try:
    a

    if True:
        print("Hello World")
        
except NameError:
    print("Name Error")

except IndentationError:
    print("Indentation Error Occured")
    
else:
    print("Not Error")
    
finally:
    print("Finally Block")
    
    
    
# pip install requests

import requests
def GetWeather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=9c9940e9e1bf4e4ca6013952243112&q={city}&aqi=yes"
    data = requests.get(url)
    toJson = data.json()
    location = toJson['location']['name']
    temp = toJson['current']['temp_c']
    print(f"location : {location}")
    print(f"Temperature : {temp}")
    
    
city = input("Enter your city name : ")
GetWeather(city)


