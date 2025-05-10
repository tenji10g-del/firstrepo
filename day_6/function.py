#function_with_parameter
#lambdafunction 
# square= lambda x:x*x
# print(square(5))

#check if number is positive, negative and zero 
# n= lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
# print(n(5))
# print(n(-3))
# print(n(0))

#simplefunction 
# def greet(name):
#     return f"hello,{name}!"
# print(greet("Tenji Sherpa"))

# calc= lambda x,y: (x+y,x*y)
# res=calc (3,4)
# print(res)

#filter_even_number_from a list
# n=[1,2,3,4,5,6]
# even= filter(lambda x:x%2==0,n)
# print(list(even))

#double_each_number_in_list 
# a=[1,2,3,4]
# b= map(lambda x:x*2,a)      #maping
# print(list(b))

#factorial
# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return(fact)

# a=int(input("enter numbe here:"))
# x=calc_fact(a)
# print(x)

#recursion_function 
# def calc_fabo(n):
#     if(n==10):
#         return
#     print(n)
#     return
