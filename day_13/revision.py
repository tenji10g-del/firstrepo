a=(1,2,3,4,5)

element=int(input("enter number here:"))
p=0
while p<=4:
    if (a[p] ==element):
     print(element,"is here in",p)
    else:
        print(element,"is not here")
    p+=1

    