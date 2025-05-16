# from abc import ABC , abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass 
#     @abstractmethod 
#     def stop_engine (self):
#         pass
# class Car(vehicle):
#     def start_engine(self):
#         print("car engine started")
#     def stop_engine(self):
#         print("car engine stop")
# from abc import ABC, abstractmethod 
# class Animal(ABC):
#     @property
#     @abstractmethod
#     def sound(self):
#         pass 
# class Bird(Animal):
#     @property
#     def sound(self):
#         return "chirp"
# bird=Bird()
# print(bird.sound)
# def my_function(x):
#     print("The number is=",x)
# def my_decorator(some_function,num):
#     print("line6")
#     def wrapper(num):
#         print("Inside wraper to check odd/even")
#         if num%2==0:
#             ret="even"
#         else:
#             ret="odd"
#         some_function(num)
#         return ret 
#     print("wrapper function is called")
#     return wrapper

# no=10
# my_function =my_decorator(my_function, no )
# print ("it is", my_function(no))

# def my_decorator(some_function,num):
#     def wrapper(num):
#         print("Inside wraper to check odd/even")
#         if num%2==0:
#             ret="even"
#         else:
#             ret="odd"
#         some_function(num)
#         return ret 
#     print("wrapper function is called")
#     return wrapper

# @my_decorator
# def my_function(x):
#     print("the number is:",x)

# no=10
# print ("it is",my_function(no))


# class counter:
#     count=0
#     def __init__(self):
#         print("init called by",self)
#         counter.count=counter.count+1
#         print("count=", counter.count)
#     @classmethod
#     def showcount(cls):
#         print("called by",cls)
#         print("count=", cls.count)
# c1=counter()
# c2=counter()
# print("class method called by object")
# c1.showcount()
# print("class method called by class ")
# counter.showcount()

#property_method 
class Car: 
    def __init__(self, speed=40):
        self._speed=speed
        return 
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        if speed<0 or speed>100:
            print("speed limit 0 to 100")
            return 
        self._speed=speed
        return 
c1=Car()
print(c1.speed) #calls getter 
c1.speed=60    #calls shetter
