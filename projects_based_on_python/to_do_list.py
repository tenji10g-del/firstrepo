# def main():
#     tasks=[]

#     while True:
#         print("\n====to_do list=====")
#         print("1. Add task")
#         print("2. show task")
#         print("3. mark task as done")
#         print("4. exist")

#         choice= input("Enter your choice: ")

#         if choice== "1":
#             print ()
#             n_task=int(input("how many task you want to add:"))
#             for i in range(n_task):
#                 task= input("enter the task: ")
#                 tasks.append("task":tasks, "done":False)
#                 print("task added")
#         elif choice=="2":
#             print("\ntasks:")
#             for index, task in enumerate(tasks):
#                 status="done" if task["done"] else "not done"
#                 print(f"{index + 1 }.{task['task']} -{status}")
        
#         elif choice=="3":
#             task_index=int(input("Enter the task number to mark as done:")) -1
#             if 0<-task_index< len(tasks):
#                 tasks[task_index]["done"]=True
#                 print("task added as done")
#             else:
#                 print("invalid task number.")

#         elif choice=="4":
#             print("exiting the to do list")
#             break
#         else:
#             print("invalid choice: please try again")


# simple calculator

# num1=int(input("Enter first number:"))
# num2=int(input("enter second number:"))

# opr=input("enter the operator:")

# # if opr=='+':
# #     print(num1+num2)
# # elif opr=='-':
# #     print(num1-num2)
# # elif opr=='/':
# #     print(num1/num2)
# # elif opr=='*':
# #     print(num1* num2)
# # else:
# #     print("invalid! please try again....")


# if opr=='+':
#     print(num1+num2)
# if opr=='-':
#     print(num1-num2)
# if opr=='/':
#     print(num1/num2)
# if opr=='*':
#     print(num1* num2)
# if opr!='+' and opr!='-' and opr!='/' and opr!='*':
#     print("invalid opr..")

#email validation project
email=input("Enter your email:-")#g@g.in
k=0
j=0
d=0

if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if(email[-4]=='.') ^ (email[-3]=="."):
                for i in email:
                    if i ==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1 
                if k==1 or j==1 or d==1:
                        print("spacing or case or digit error")
                else:
                    print("congrates your email varified")
            else:
                print(". error")    
        else:
            print("@ missing or double @")
    else:
        print(" starting letter should be alphabet character.")
else:
    print("invalid email address... ")

