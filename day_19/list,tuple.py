# for palindrome
# def check():
#     word=input("enter word here:")
#     l1=list(word)
#     if l1==l1[::-1]:
#         print(f"{word} is palindrome")
#     else:
#         print(f"{word} is not palindrome")

# check()
# a=1
# while a<=10:
#     print(a)
#     a+=1

l1=[1,3,2,4,3,2,13,2]
r=input("enter number searching for here:")
for a in l1:
    if a==r:
        print(f"number found in index",l1.index(r))
    else:
        print("number not found")

# list1 = [1, 3, 4, 5, 3, 5, 4, 3, 5, 4]
# p = int(input("Enter number you want to search: "))

# if p in list1:
#     print(f"{p} found at index {list1.index(p)}")  # First occurrence only
# else:
#     print(f"{p} not found in the list.")






