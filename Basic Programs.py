# # 1. Python program to add two numbers
# a = int(input("Enter the first No: "))
# b = int(input("Enter the second No: "))
# c = a + b
# print(f'The sum of {a} and {b} is {c}')

#  2. Maximum of two numbers in Python
# a = 200
# b = 1000
# if a > b:
#     print(a)
# else:
#     print(b)

# 3. Python Program for factorial of a number
# def fact(num):
#     if num ==1:
#         return(num)
#     else:
#         return num * fact(num-1)
# print(fact(10))

# 4. Python Program for simple interest
# P = 3000
# R = 7
# T = 1
# si = P * R * T /100
# print(si)

# 5. Python Program for compound interest
# def ci(principle,rate,time):
#     a = principle * (pow((1 + rate/100),time))
#     CI = a - principle
#     print("Compount interest is: ", CI)
# print(ci(1200,2,5.4))

# 6. Python Program to check Armstrong Number
# n = int(input("Enter the number: "))
# a = list(map(int,str(n)))
# b = list(map(lambda x:x **3,a))
# if sum(b) == n:
#     print("Yes")
# else:
#     print("Not")

# 7. Python Program for Program to find area of a circle
# def circlearea(r):
#     pi = 3.122
#     return pi * (r*r)
# print(circlearea(10))

# 8 .Python program to print all Prime numbers in an Interval
# a = 1
# b = 100
# for i in range (a,b):
#     for j in range(2,i):
#         if (i % j==0):
#             break
#     else:
#         print(i)

# 9. Python program to check whether a number is Prime or not
# n = int(input("Enter the number to check the prime number: "))
# def prime(num):
#     if n%2 !=0:
#         print(num,"number is prime")
#     else:
#         print(num,"Not the prime number")
# print(prime(11))

# 10. Python Program for n-th Fibonacci number 

# def fabo(n):
#     if n<=0:
#         print("Incorrect Output")
#     elif n==1:
#         return 0
#     elif n ==2:
#         return 1
#     else:
#         return fabo (n-1) + fabo (n-2)

# print(fabo(10))

# Program no 11
# Task
# Given an integer, , perform the following conditional actions:
# If is odd, print Weird
# If is even and in the inclusive range of to , print Not Weird
# If is even and in the inclusive range of to , print Weird
# If is even and greater than , print Not Weird

# n = int(input())
# check = {True: "Not Weird", False: "Weird"}

# print(check[
#         n%2==0 and (
#             n in range(2,6) or 
#             n > 20)
#     ])


# Take two lists, say for example these two: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = set(a) & set(b)
# print(a)

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# n = int(input("Enter the interger: "))
# print("The divisiors of the integar are: ")
# for i in range(1,n+1):
#      if n%i==0:
#              print(i)

# Program to get the length of str without usein len function
# a ="Hello World I am at jungle"
# b = 0
# for i in a:
#         b=b+1
# print(b)


print








