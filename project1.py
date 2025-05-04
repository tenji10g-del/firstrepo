#for condition

# mark=int(input("enter your mark"))

# if(mark>=90):
#     print("A+")
# elif(mark<90 and mark>=80):
#     print("A")
# else:
#     print("need to work ")

#project2
# number=int(input("enter number here:"))
# result=number % 2
#  #condition
# if(result==0):
#     print(" This number even")
# else:
#     print("this is odd number")

#project3
# a=input("enter first number:")
# b=input("enter second number:")
# c=input("enter third number:")
# #condition
# print("your greatest number ")
# if(a>=b and a>=c):
#     print(a)
# elif(b>=a):
#     print(b)
# else:
#     print(c)

# #project4
# num=int(input("enter number here:"))
# reminder=  num % 7 
# #condition 
# if(reminder==0):
#     print(num,"is multiple of 7")
# else:
#     print(num,"is not multiple of 7")

#project4
# movies=[]
# movies.append(input("first movie:"))
# movies.append(input("second movie:"))
# movies.append(input("third movie:"))
# print(movies)

#testing palindrome of element
# list1=[]
# list1.append(input("enter first element:"))
# list1.append(input("enter second element:"))
# list1.append(input("enter third element:"))
# copy1=list1.copy()
# reverse1=copy1
# if(list1==reverse1 ):
#     print("elements are palindrome")
# else:
#     print("elements are not in palindrome")

#project(while loop)
# i=1
# while i<=100:
#     print(i)
#     i+=1

#multiple table of x
# x=int(input("enter number over here:"))
# i=1
# while i<=10:
#     print(i*x)
#     i+=1

#finding element in list
# roll=[1,2,3,4,5,2,5,2,6,7,4,54,32,56,32,56,32,]
# b=int(input("enter number:"))
# y=0
# while y<len(roll):
#     if(roll[y]==b):
#         print("found at index",y)
#     y+=1

# number=[1,2,3,4,7,3,2,2,9,7,6,4]
# idx=11
# x=int(input("enter number:"))
# for loop in number:
#     if(loop==x):
#         print("number available",idx)
#     idx+=1

## multipleusing(range)
a=int(input("enter number:"))
for num in range(1,10):
    print(num,"*",a,"=",num*a)