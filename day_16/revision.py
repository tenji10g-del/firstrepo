# class person:
#     def __init__(self, name, id):
#         self.name=name 
#         self.id=id 
#     def get_detail(self):
#         return f"name: {self.name} , id: {self.id}"
# class Student(person):
#     def __init__(self, name, id , grade, course):
#         super().__init__(name, id)
#         self.grade = grade 
#         self.course= course
#     def get_detail(self):
#         return f"name: {self.name}, id: {self.id}, grade: {self.grade}, course: {self.course}"

# student = Student("Tenji ", 3245, "A",["maths", "science", "computer science"])
# detail=student.get_detail()
# print(detail)
# print(student)

#practising MRO 
# class CEO:
#     def repon(self):
#         print("final decision making")
# class Director(CEO):
#     def repon(self):
#         print("stragity making")
# class Manager(CEO):
#     def repon(slef):
#         print("team management")
# class Team_leader(Manager, Director):
#     pass

# t1= Team_leader()
# t1.repon()
# class Person:
#     def __init__(self, name, id):
#         self.name=name 
#         self.id = id 
#     def get_detail(self):
#         return f"name: {self.name}, id: {self.id}"
# class student(Person):
#     def __init__(self, name , id , grade):
#         super().__init__(name, id)
#         self.grade= grade
#     def get_detail(self):
#         return f"name: {self.name} id:{self.id} grade:{self.grade}"
# class Teacher(Person):
#     def __init__(self, name, id, subject):
#         super().__init__(name , id)
#         self.subject=subject
#     def ger_detail(self):
#         return f"name: {self.name} id: {self.id} subject:{self.subject}"
    
# std= student("Tenji", 221, 10)
# teacher= Teacher("ram", 3324, "science")
# print(std.get_detail())
# print(teacher.get_detail())

# class A: 
#     def say_hello(self):
#         print("hello from A")
# class B(A):
#     pass 
# obj= B()
# obj.say_hello()

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("c")
# class D(B,C):
#     pass
# obj=D()
# obj.show()
# print(D.mro())

class A:
    def greet(self):
        print("hello from A ")
class B(A):
    def greet(self):
        print("hello form B")
class C(A):
    def greet(self):
        print("hello form c ")
class D(B,C):
    pass
d=D()
d.greet()
print(D.mro)