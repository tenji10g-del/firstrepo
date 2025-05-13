#inheritance

class car:
   name="F1"
   brand="Nepali"

class Tesla(car):
    def __init__(self,type):
        self.type=type                                 #single inheritance

    def info(self):
       car_detail=[f"car:{self.name}",f"brand:{self.brand}",f"type:{self.type}"]
       for x in car_detail:
           print(x)

#polymorphis:
# class Complex: 
#     def __init__(self, real , img ):
#         self.real= real 
#         self.img=img 
#     def Shownumber(self):
#         print(self.real,"i+", self.img,"j")
    
#     def __add__(self,num2):
#         newReal = self.real + num2.real 
#         newimg= self.img + num2.img 
#         return Complex(newReal,newimg)
    
# num1= Complex(1,2)
# num2=Complex(3,4)

# num1.Shownumber()
# num2.Shownumber()
# num3= num1+num2
# num3.Shownumber()


#project_polymorphism 
# class Circle: 
#     def __init__(self,radius):
#         self.radius= radius 

#     def Area(self):
#         return 3.14*self.radius**2
    
#     def perimeter(self):
#         return 2*3.14* self.radius
    
# c1=Circle(7)
# print(c1.Area())
# print(c1.perimeter())

class Employee: 
    def __init__(self,role, dept , salary):
        self.role=role 
        self.dept=dept
        self.salary=salary 
    def show_detail(self ):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)
    
class Engeneer(Employee): 
    def __init__(self, name , age):
        self.name=name 
        self.age= age 
        super().__init__("engeeneer","it","30000")
eng = Engeneer("Tenji Sherpa","18")
eng.show_detail()