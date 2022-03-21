# Types of Inhertaince


# class phone:
#     def make_call(self):
#         print("I am making call")
#     def play_games(self):
#         print("I am playing games")

# p1 = phone()
# p1.make_call()
# p1.play_games()


# class Phone:
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost
#     def make_call(self):
#         print("Make a call")
#     def play_games(self):
#         print("Playing Games")

# p2 = Phone
# p2.set_color("White")
# p2.set_cost(10000)
# p2.show_color()
# p2.show_cost()
# p2.play_games()
# p2.make_call()

#  Creating class with Constructor
# __int__ method is the Constructor where you can define all the values at one time.
# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender

#     def show_employee_details(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         print("Salary: ",self.salary)
#         print("Gender: ",self.gender)

# e1 = Employee("Murtuza",30,4000,"Male")
# e1.show_employee_details()


# Inhritance in Python 
# With inheritance one class can derive the properties of another class
# Types of Inheritance 1. Single 2. Multiple 3. Multiple Level
# 2 types of class - Super and Sub or Child Class

# # Super Class

# class Vehicle:             
#     def __init__(self,milage,cost):
#         self.milage = milage
#         self.cost = cost
#     def show_vehicle_details(self):
#         print("My Cost and Milage are")
#         print("Milage:",self.milage)
#         print("Cost:",self.cost)

# v1 = Vehicle(100,500000)
# v1.show_vehicle_details()

# # Child Class
# class car(Vehicle):
#     def show_car_details(self):
#         print("I am a car")

# c1 = car(400,50000)
# c1.show_vehicle_details()
# c1.show_car_details()

# Over-riding init Method
# Super is used to call base class constructor and method
# Calling base class method and constructor it support reusability of code.

# class Car(Vehicle):
#     def __init__(self, milage, cost,tyre,hp):
#         super().__init__(milage, cost)
#         self.tyre = tyre
#         self.hp = hp
#     def show_car_details(self):
#         print(" I am car")
#         print("the tyre is ",self.tyre)
#         print("the hp is",self.hp)

# c1 = Car(100,2000000,700,32)
# c1.show_car_details()
# c1.show_vehicle_details()



# Types of Inheritance
# 1. Single 2. Multiple 3. Multilevel 4. Hybrid 

# Multiple Inheritance
# In this inheritance the Child inherits from more than 1 parent class

# class Parent1:
#     def assign_string_one(self, str1):
#         self.str1 = str1
#     def show_str1(self):
#         return self.str1
# class Parent2:
#     def assign_string_two(self,str2):
#         self.str2 = str2
#     def show_str2 (self):
#         return self.str2
# class Child (Parent1,Parent2):
#     def assign_string_three(self,str3):
#         self.str3 = str3
#     def show_str3 (self):
#         return self.str3

# my_child = Child()
# my_child.assign_string_one("This is my Yard")
# my_child.assign_string_two("This is my Ring")
# my_child.assign_string_three("This is my Show")
# my_child.show_str1()
# my_child.show_str2()
# my_child.show_str3()

# In Multilevel Inheritance,we have Parent,Child,grand - child relationship
# class Parent:
#     def assign_name(self,name):
#         self.name = name
#     def assign_age(self,age):
#         self.age = age
#     def show_name(self):
#         return self.name
#     def show_age (self):
#         return self.age

# class Child (Parent):
#     def assign_gender(self,gender):
#         self.gender = gender
#     def show_gender(self):
#         return self.gender

# class GC(Child):
#     def assign_birth_mark(self,birth_mark):
#         self.birth_mark = birth_mark
#     def show_birth_mark(self):
#         return self.birth_mark


# m1 = GC()
# m1.assign_gender ("Male")
# m1.assign_age(32)
# m1.assign_name("Miz")
# m1.assign_birth_mark("Til")
# m1.show_gender()
# m1.show_age()
# m1.show_name()
# m1.show_birth_mark()





# Encapsulation
# The feature of preventing data from direct access is called Encapsulation

# Polymorphism
# This polymorphism is the Feature of using the same function in multiple ways


# Method Resolution Order MRO
# Any attribute or method is searched first in the Current Class.If it is not found then the 
# the search will continue in the parent class from Left to Right
# Base Class
class AA:
    def m1(self):
        print ("Inside aa class")
# Base Class
class BB:
    def m1(self):
        print("Inside BB Clas")
# Dervied Class
class CC(AA,BB):
    def m1(self):
        print("Inside CC Class")

obj = CC
obj.m1







