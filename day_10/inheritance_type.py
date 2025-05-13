#mutiple_inheritance
# class Person:
#     def __init__(self,name):
#         self.name=name 
#     def greet(self):
#         return f"hello, my name is {self.name}."

# class Employee:
#     def __init__(self,employee_id):
#         self.empolyee_id=employee_id 
#     def get_id(self):
#         return f"my employee id is {self.empolyee_id}."

# class Manager( Person, Employee):
#     def __init__(self,name,employee_id, department):
#         Person.__init__(self,name)
#         Employee.__init__(self, employee_id)
#         self.department= department
#     def show_detail(self):
#         return f"{self.greet()} {self.get_id()} i manage the{self.department} department"
    
# manager = Manager("Tenji ","AB1","Sales")

# print(manager.greet())
# print(manager.get_id())
# print(manager.show_detail())

# class Animal:
#     def __init__(self, species):
#         self.species=species
#     def eat(self):
#         return f"{self.species } is eating "
    
# class Mammal(Animal):
#     def __init__(self, species, fur_color):
#         super().__init__(species)
#         self.fur_color=fur_color
#     def breathe(self):
#         return f"{self.fur_color} breathe air."
# class Dog(Mammal):
#     def __init__(self, species, fur_color,name):
#         super().__init__(species, fur_color)
#         self.name=name 
#     def bark(self):
#         return f"{self.name} says woof!."

# my_dog=Dog("Dog","Brown","buddy")

# print(my_dog.eat())
# print(my_dog.breathe())
# print(my_dog.bark())


class Animal:
    def __init__(self, species):
        self.species =species
    def speak(self):
        return f" {self.species} makes a sound "
    
class Dog(Animal):
    def __init__(self,name):
        super().__init__("Dog")
        self.name=name 
    def bark(self):
        return f"{self.name} says woof!"
class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat")
        self.name=name
    def meow(self):
        return f"{self.name} says meow!"
dog=Dog("buddy")
cat=Cat("whiskers")

print(dog.speak())
print(dog.bark())
print(cat.speak())
print(cat.meow())
