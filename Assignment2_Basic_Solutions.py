# Assignment-2: Python Basics
# 1. Write a python script to add comments and print “Learning Python” on screen

print('Learning Python')

''' 2 . Write a python script to add multi line comments and print values of four variables,
 each in a new line. Variable contains any values. '''

name= input("enter your name :") 
age=int(input (" Enter your age:"))
college=input("enter your college name :")
roll=int(input("enter your rollno. :"))
print(name , age , college , roll , sep='\n')

# Write a python script to print types of variables. Create 5 variables each of them
# containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
a=23
b= True
c="MySirG"
d=5.46
e=3+4j
f="45"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

 # 4  Write a python script to print the id of two variables containing the same integer
 # values.
num1 = 10
num2 = 10

print("Id of num1 is: ",id(num1))
print("Id of num2 is: ",id(num2))

# 5 Create four variables in a Python script and assign values of different data types to
# them. Write a Python script to print value, its type and id of each variable.
a=23
b= True
c="MySirG"
d=5.46
e=3+4j
f="45"
print(type(a) , id(a) , a)
print(type(b) , id(b) , b)
print(type(c) , id(c) , c)
print(type(d) , id(d) , d)
print(type(e) , id(e) , e)
print(type(f) , id(f) , f)

 # 6 Write a python script to print all the keywords
 # importing "keyword" for all keywords 
import keyword
  
# printing all keywords using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# 10. Write a python script to display the current date and time. First create variables to
 #store date and time, then display date and time in proper format (like: 13-8-2022 and
 # 9:00 PM
from datetime import datetime
dt=datetime.today()
print(dt.strftime("%d-%m-%Y and %I:%M:%p"))



