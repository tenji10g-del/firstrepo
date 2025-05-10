
# class car:
#     def __init__(self, color,model):
#         self.color=color#attribute 
#         self.model=model#attribute
#     def honk(self): #method 
#         print("Beep Beep!")

# #creating an object
# my_car = car("red","toyota")
# my_car.honk() #output:beep beep!

       #encapsulation 
# class Bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance
    
# account= Bankaccount(100)
# account.deposit(50)  
# print(account.get_balance()) #output: 150 


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # Private attribute

#     # Getter method
#     def get_age(self):
#         return self.__age

#     # Setter method
#     def set_age(self, age):
#         self.__age = age 

# stud = Student('DAWA', 12)

# # Retrieving age using getter
# print('NAME:', stud.name, stud.get_age())

# # Changing age using setter
# stud.set_age(16)

# # Retrieving age using getter
# print("NAME:", stud.name, stud.get_age())

#practise_OOPs 

# class coffeemachine:
#     def __init__(self,brand, model, type):
#         self.brand=brand
#         self.model=model
#         self.type=type 
#     def display_info(self):
#         return f"This is coffee machine with {self.brand} brand and model {self.model} and type {self.type}"

# machine1=coffeemachine("tesla","A12","electric")
# machine2=coffeemachine("ABC","B234","traditional")

# print(machine1.display_info())
# print(machine2.display_info())

# class Employee:
#     def __init__(self,name, age ,salary):
#         self.name=name 
#         self._age=age 
#         self._salary=salary 
#     def dispalyEmployee(self):
#         print("Name:",self.name,"age:", self._age, "salary:",self._salary)
# e1=Employee("RAM",24,10000)
# print(e1.name)
# print(e1._salary)
# print(e1._age)
# print(e1.dispalyEmployee)

#types_of_attributes

class Pen: 
    location= "india"  #class attribute
    def __init__(self, name , type , model):
        self.name=name #object attrubue 
        self.type=type #object attribute 
        self.model=model #object attribute
    def Quality(self):
        return f"This is A 1 quality pen in nepal as far we know."

p1=Pen("technotip","blue", "techno")
print(p1.location)
print(p1.Quality())






