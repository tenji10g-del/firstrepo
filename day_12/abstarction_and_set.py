# from abc import ABC, abstractmethod 
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass 
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# class Cat(Animal):
#     def make_sound(self):
#         return "meow!"
# dog=Dog()
# print(dog.make_sound())

#waw_of_creating_abstractionmethod 
# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def engine_strat(self):
#         pass 
# class Car(ABC):
#     def engine_start(self):
#         pass 

#example
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def gettotalsalary(self):
#         pass 
# #creating concreate subclass of Employee, Engineer
# # class Engineer(Employee):
# #     def __init__ (self,name, base_salary, bonus ):
# #         self.name= name 
# #         self.base_salary=base_salary
# #         self.bonus=bonus 

# #         #overriding the abstract method
# #     def gettotalsalary(self):
# #             return self.base_salary + self.bonus
        
# # e1= Engineer("Tenji",20000,100)

# # print(e1.name+"'s total salary:$"+
# # str(e1.gettotalsalary()))
    
# from abc import ABC, abstractmethod
# class Calculation(ABC):
#     @abstractmethod
#     def calculate(self,x , y):
#         pass 
# class Addition(Calculation):
#     def calculate(self, x ,y ):
#         return x+y
# class subraction(Calculation):
#     def calculate(self, x,y):
#         return x-y 
# class mulplicaiton(Calculation):
#     def calculate(self, x, y ):
#         return x*y
# class Division(Calculation):
#     def calculate(self, x , y): 
#         return x/y

# a=Addition()
# s=subraction()
# m=mulplicaiton()
# d=Division()

# result1=a.calculate(20,30)
# result2=s.calculate(20,30)
# result3=m.calculate(20,30)
# result4=d.calculate(20,30)

# outcome=[result1, result2, result3, result4]
# for a in outcome:
#     print(a)

#example2
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self ):
        pass 

    @abstractmethod
    def display_info(self):
        pass 
class NMB(Bank):
    def __init__(self, name , intrest_rate):
        self.name=name 
        self.intrest_rate=intrest_rate

    def git_interest_rate(self):
        return self.intrest_rate
    def display_info(self):
        print("Bank:", self.name)
        print("Intrest rate:",sbi.get_interest_rate(),"%")

class Prabu(Bank):
    def __init__(self, name , intrest_rate):
        self.name=name 
        self.intrest_rate=intrest_rate

    def git_interest_rate(self):
        return self.intrest_rate
    def display_info(self):
        print("Bank:", self.name)
        print("Intrest rate:",prabu.get_interest_rate(),"%")
class Rastra(Bank):
    def __init__(self, name , intrest_rate):
        self.name=name 
        self.intrest_rate=intrest_rate

    def git_interest_rate(self):
        return self.intrest_rate
    def display_info(self):
        print("Bank:", self.name)
        print("Intrest rate:",rastra.get_interest_rate(),"%")

class Hamro(Bank):
    def __init__(self, name , intrest_rate):
        self.name=name 
        self.intrest_rate=intrest_rate

    def git_interest_rate(self):
        return self.intrest_rate
    def display_info(self):
        print("Bank:", self.name)
        print("Intrest rate:",harmro.get_interest_rate(),"%")

prabu=Prabu("Prabu bank",2)
rastra=Rastra("rastra bank",4)
hamro=Hamro("hamro",5)

prabu.display_info()
rastra.display_info()
hamro.display_info()