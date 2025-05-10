
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
