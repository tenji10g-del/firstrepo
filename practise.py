
# #function demo
# def calc_avg(a,b,c): #function defination + parameter
#     sum=a+b+c        #work
#     avg=sum/3         
#     return avg
#     #some code 
# # calc_avg(2,3,3)      #function call

# #for loop 
# x=int(input("enter number here:"))
# list1=[2,3,4,2,2,4,5,2,3]
# if  x in list1:

#     print("number found:")
# else:
#     print("number not found")

#loop practise 
# i=0
# while i<3:
#     i+=1
#     print("hello world")
# else:
#     print("you are in limit")
#for loop 
# n=int(input("enter number:"))
# for i in range(0,n):
#     print(i)
    
#practise_2
# fruit=('apple','banana','mango')
# for x in range(len(fruit)):
#     print(fruit[x])

# for l in "green":
#     if (l=="r"):
#         print("this is second word of letter",l[0])
#     print(l)

# a=1
# while a<=10:
#     if(a%2==0):
#         print("even",a)
#     else:
#         print("odd",a)
#     a+=1

#oops practise from begining. 
# class Student:
#     name="Rahul" 

# s1=Student()
# print(s1.name)

# class Tesla:
#     brand="coffee"
#     type="electric"
#     design="nepali"

# class car:
#     def __init__(self,name,type,brand):
#         print("This is all about car we are manifucturing.")
#         self.name= name
#         self.type=type 
#         self.brand=brand
# car1= car("tesla","electric","nepali")
# print(car1.name)

#project_based_on_oops 
# class student:
#     def __init__(self,name,mark1,mark2,mark3): 
#         self.name=name 
#         self.mark1=mark1
#         self.mark2=mark2
#         self.mark3=mark3
#     def average(self):
#         sum= self.mark1 + self.mark2 + self.mark3
#         average=sum/3
#         return average 
    
# std=student("Ram",12,23,43)
# print ("hello",std.name,"you average mark for three subject is ",std.average())

#same project using list 
# class Student:
#     def __init__(self,name, marks):
#         self.name=name 
#         self.marks=marks 
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"you average marks is",sum/3)

# std1=Student("Mingmar Sherpa",[98,95,99])
# std1.get_avg()
# std1.name="Tenji Sherpa"
# std1.get_avg()

# class Student: 
#     school="Sagarmatha Secondary School"
#     def __init__(self,name, rollnumber , grade,age):
#         self.name=name 
#         self.rollnumber=rollnumber
#         self.grade=grade
#         self.age=age
#         print("welcome:",self.name) 
        
#     def welcome(self):
#         print("Your information:")
#         std1=[f"name:{self.name}",f"roll number:{self.rollnumber}",f"grade:{self.grade}",f"age:{self.age}"]
#         for  info in std1:
#             print(info)
    
# std= Student("Nima Rai",16,"eight",13)
# print(std.school)
# std.welcome()

# std2=Student("Anish BK",1,"six",14)
# std2.welcome()

# std3=Student("Roshan", 10,"Ten",15)
# std3.welcome()

#static_method
# class student:
#     @staticmethod
#     def school(): 
#         print ("sagarmatha secondary school")
   
#     def __init__(self,name,address):
#         self.name=name 
#         self.address=address 
#     def welcome(self):
#         print(f"wel-come!{self.name}", f"your location is {self.address}" )

# std=student("Tenji Sherpa","phaplu")
# std.school()
# std.welcome()

#project_based_on_oops 
# class Account:
#     def __init__(self,balance,amt):
#         self.balance=balance 
#         self.amt=amt 
    
#     def debit(self,amount):
#         self.balance -= amount
#         print(f"amount{amount} is debited")
#         print("your current amount is",self.get_balance())

#     def credit(self,amount):
#         self.balance += amount
#         print(f"anount {amount} is credited to you account")
#         print("your current amount is",self.get_balance())
#     def get_balance(self):
#         return self.balance
# account1=Account(1000,1012)
# print(account1.balance)
# account1.debit(1000)
# account1.credit(100)
# print(account1.balance)

#project_for_oops 
# class Account: 
#     def __init__(self,acc_num,bal):
#         self.account=acc_num
#         self.bal=bal
    
#     def debit(self,amount):
#         self.bal-=amount
#         print (amount,"is debited from  you account")
#         print ("Now your total balance is",self.get_bal())
    
#     def credit(self,amount):
#         self.bal+=amount
#         print(amount,"is credited to you account ")
#         print ("Now your total balance is",self.get_bal())
#     def get_bal(self):
#         return self.bal

# account1=Account(1012,12000)
# account1.debit(1000)
# account1.credit(2000)

# class Subject:
#     def __init__(self,type,name): 
#         self.type=type 
#         self.name=name 
#     def __info(self):
#          x = [f"type: {self.type}", f"name: {self.name}"]
#          for about in x:
#             print(about)
#     def  detail(self):
#         print("hi! your information....")
#         print(self.__info())

#     def display(self):
#         self.detail()

# sub1=Subject("Maths","compulsary")
# sub1.display()

# class Subject:
#     def __init__(self, type, name): 
#         self.type = type 
#         self.name = name 

#     def _info(self):  # Changed from __info to _info
#         return [f"type: {self.type}", f"name: {self.name}"]

#     def detail(self): 
#         print("Hi! Your information....") 
#         print("\n".join(self._info()))  # Calling the method correctly

#     def display(self): 
#          print(self.detail())  # Avoiding recursion error

# # Creating an instance
# sub1 = Subject("Maths", "Compulsory")
# sub1.display()  


# from abc import ABC , abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass 
#     @abstractmethod 
#     def stop_engine (self):
#         pass
# class Car(vehicle):
#     def start_engine(self):
#         print("car engine started")
#     def stop_engine(self):
#         print("car engine stop")
# from abc import ABC, abstractmethod 
# class Animal(ABC):
#     @property
#     @abstractmethod
#     def sound(self):
#         pass 
# class Bird(Animal):
#     @property
#     def sound(self):
#         return "chirp"
# bird=Bird()
# print(bird.sound)
# def my_function(x):
#     print("line2")
#     print("The number is=",x)
# def my_decorator(some_function,num):
#     print("line6")
#     def wrapper(num):
#         print("line8")
#         print("Inside wraper to check odd/even")
#         if num%2==0:
#             ret="even"
#         else:
#             ret="odd"
#         print("line14")
#         some_function(num)
#         print("line16")
#         return ret 
#     print("wrapper function is called")
#     return wrapper
# no=10
# my_function =my_decorator(my_function, no )
# print ("it is", my_function(no))

#project_cafe

#define the menu of resturant.
# name=input("please enter your name:")

# items={"pizza":550, "salt tea":30, "cold drink":100, "coffee":50}
# print(items)

# #greet 
# print("welcome to our cafe Mr.",name)
# print("pizza:550\nsalt tea:30\ncold drink:100\ncoffee:50",)

# order_total=0

# item_1= input("Enter you first order:")
# if item_1 in items:
#     order_total+=items[item_1]
#     print(f"you item {item_1} has been added")
# else:
#     print(f"{item_1} is not available is our hotel")

# another_order= input("do you want to add another item? (yes/no)")
# if another_order=="yes":
#     item_2= input("enter the name of your second item:")
#     if item_2 in items:
#         order_total+= items[item_2]
#         print(f"item has been added to your order")
#     else:
#         print(f"sorry {item_2}, is not available here")

# print(f"Total amount to pay for your order {order_total}")



# set1={1:{"name":"Tenji", "age":18, "cls":10},
#       2:{"name":"Tenji", "age":18, "cls":10},
#       3:{"name":"Tenji", "age":18, "cls":10}}
# for c in set1[2]: 
#     print(c)

#project_calculator

#this is project to divide total expense to the number of people 
# def house_rent():
#       rent=int(input("enter total rent here:"))
#       electricity=int(input("enter electricity consumption:"))
#       electricity_rate=int(input("enter electricity rate per unit:"))
#       electricity_charge=electricity*electricity_rate
#       food=int(input("enter total food expences:"))
#       people=int(input("number of people:"))


#       total_expenses= rent+electricity_charge+food
#       division=total_expenses/people

#       print(f"each will pay {division} ")
#       print("thank you!")

# house_rent()

#scissor_papper_game

set1={"scissor","papper", "rock"}
my_list=list(set1)
computer=(my_list[0])
man=input("enter your move:")

if man==computer:
    print("with draw")
else:
    print("you win")

