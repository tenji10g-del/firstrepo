
class Person:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        return f"Hello, my name is {self.name}."

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id 

    def get_id(self):
        return f"My employee ID is {self.employee_id}."

class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name)  
        super().__init__(employee_id)
         
        self.department = department

    def show_detail(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department."

manager = Manager("Tenji", "AB1", "Sales")

print(manager.show_detail())