a=(1,2,3,4,5)

element=int(input("enter number here:"))
p=0
while p<=4:
    if (a[p] ==element):
     print(element,"is here in","index",p)
    else:
        print(element,"is not here")
    p+=1

#fibonacci_series
# def fibonacci(n):
#     if n <= 0:
#         return "invalid input please return again!"
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         sequence = fibonacci(n - 1) 
#         sequence.append(sequence[-1] + sequence[-2]) 
#         return sequence


# num_terms = int(input("Enter the number of Fibonacci terms: "))

# print(f"Fibonacci Series: {fibonacci(num_terms)}")