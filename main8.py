print("Hello World")

# Read Mode (r)
# Write Mode (w)
# Append Mode (a)


let = open("details.txt","r")
const = let.read()
print(const)


file =  open("example.txt","w") 
file.write("Hello I am a python developer.")
file = open("example.txt","r")
details = file.readline()
print(details)



file =  open("example.txt","w") 
file.write("I am working hard as I can.")
file = open("example.txt","r")
details = file.readline()
print(details)



file = open("example.txt",mode = "a")
file.write(f"\n {const}")
file = open("example.txt",mode = "r")
details = file.read()
print(details)



# os 
# import os
# os.remove("requirement.txt")


# with operator in python 
with open("example.txt","r") as files:
    data = files.readlines()
    print(data)

with open("example.txt" , mode = "w+") as files:
    files.write("Hello World")
    details = files.read()
    print(details)
    
    
    
# python manage.py startapp blog 
# free blog templates in html
# python -m venv env 
# cd folderName 
# env\Scripts\activate
# pip install django 


# django-admin startproject core . 
# python manage.py runserver 
# CTRL+c 
# python manage.py startapp blog 


# MVC -> laravel 
# MVT -> model view templates 

# python manage.py migrate 
# python manage.py createsuperuser


# # python manage.py runserver 
# python manage.py makemigrations
# python manage.py migrate


# pip freeze > requirements.txt
# pip install Pillow