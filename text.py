# num = 153
# sum = 0
# temp = num
# order = len(str(num))
#
# while temp>0:
#     digit = temp%10
#     sum+= digit ** order
#     temp//=10
#
# if sum == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
#
# n = int(input("Enter the number : "))
# a = list(map(int,str(n)))
# b = list(map(lambda x:x**3,a))
# if(sum(b)==n):
#     print(f"{n} value is armstrong number")
# else:
#     print(f"{n} value is not armstrong number")

# n = int(input("Enter your Number : "))
# a = list(map(int,str(n)))
# b= list(map(lambda x:x **3,a))
# if (sum(b)==n):
#    print("True")
# else:
#    print("False")


# def fact(num):
#     if num == 1:
#         return num
#     else:
#         return num * fact (num -1)

# print(fact(4))


# a = input("Enter the str: ")
# print("Orginal String is",a)
# size = len(a)
# print("Printing only even index chars")
# for i in range(0,size-1,2):
#    print("index[", i, "]", a[i])

# a = input("Enter the str: ")
# print("The Orginal String is",a)
# size = len(a)
# for i in range(0,size-1,2):
#   print("index[",i,"]",a[i])


# a = int(input("Enter the number1: "))
# b = int(input("Enter the number2: "))
# product = a*b
# if product <=1000:
#     print(product)
# else:
#     print(a+b)


# previous_num = 0
# for i in range(0,11):
#     print("CurrentNumber",i,"PreviousNumber",previous_num,"Sum",i+previous_num)
#     previous_num=i

# a = input("Enter the str: ")
# print("Original Str is",a)
# size = len(a)
# print("Printing only even index chars")
# for i in range(0, size - 1, 3):
#     print("index[", i, "]", a[i])

# def remove_char(word,n):
#     print("The orginal word is",word)
#     x = word[n:]
#     return(x)
# print(remove_char("pynative",4))

# def check_numbers(number_list):
#     print("The Given List:",number_list)
#     first_number = number_list[0]
#     last_number = number_list[-1]
#     if first_number == last_number:
#         print("True")
#     else:
#         print("False")
# print(check_numbers([[10, 20, 30, 40, 10]]))


# l = [[1,2,3],[11,12,'b','b','b'],[21,'t',223],[4,5,6],[7,8,9],'demo',12.5]

# for i in l:
#   if type(i)==list:
#     j=0
#     while j < len(i):
#         if type(i[j]) == str:
#             print("Index of str {} is:".format(i[j]),i)
#         j=j+1
#     j=0
#     while j<len(i):
#         if type(i[j]) == str:
#             print("The Str in the nested list is '{}'".format(i[j]))
#         i.remove(i[j])
#         continue
#         j = j+1

# print("list after removal of str from nested list is \r",l,'\n')


# a = input("Enter the Paragragh: ")
# #Q1 - Convert all the input into list
# b = a.split(" ")
# #Q2 - No Duplicates
# c = set(b)
# #Q3 - Assign your name 
# dic1= dict.fromkeys(c,'murtuza')
# #Q4 - Try to print tuple of all values
# t1=tuple(dic1.keys())
# #Q5 Try to print list of all keys
# print(t1)
# l2 = list(dic1.values()) 









#Python Script to add two numbers
# a = int(input("Enter your first Number: "))
# b = int(input("Enter your second Number: "))
# c = a + b
# print(f'The sum of {a} and {b} is {c}')

#
# p = int(input("Enter Principle amount: "))
# r = float(input("Enter rate of interest: "))
# t = int(input("Enter time in years: "))
# a = p * r * t / 100
# print("Your Simple Interest is : ", a)

# l = int(input("Enter the Length of Cuboid: "))
# b = int(input("Enter the breath of Cuboid: "))
# h = int(input("Enter the height of Cuboid: "))
# v = l * b * h
# print("Volume of Cuboid is:",v)

# a = int(input("Enter the number: "))
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")
# print("Program Excuted")


# a= int(input("Enter the year : ")) #Leap year is the year which are divisible by 400
# result = "leap year" if a%400==0 else "leap year" if a%4==0 and a%100!=0 else "Not Leap year"
# print(result)

# a= int(input("Enter 1 no: "))
# b= int(input("Enter 2 no: "))
# c= int(input("Enter 3 no: "))
# if a>b and b<a:
#     print(a)
# elif b>c and c<a:
#     print(b)
# else:
#     print(c)

# import calendar
import datetime
from typing import List, MutableMapping


# import math
# def factorial(num):
#     return (math.factorial(num))
# num = 5
# print("The Factorial of",num,"is",factorial(num))


# print(bool("abc"))

# n = int(input("Enter the Number : "))
# sum = 0
# order = len(str(n))
# copy_n = 0
# while(n>0):
#     digit = n%10
#     sum += digit**order
#     n = n//10
# if  (sum==copy_n):
#     print(f"{copy_n} is the armstrong number")
# else:
#     print(f"{copy_n} is the armstrong number")

# Python program to check if the number is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))
# sum = 0
# temp =num
# while temp>0:
#     digit = temp%10
#     sum+= digit**num
#     temp//=10
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")


# def isArmstrong(val: int) -> bool:
#     """val will be tested to see if its an Armstrong number.
#     Arguments:
#         val {int} -- positive integer only.
#     Returns:
#         bool -- true is /false isn't
#     """
#
#     # break the int into its respective digits
#     parts = [int(_) for _ in str(val)]

    # # begin test.
    # counter = 0
    # for _ in parts:
    #     counter += _ ** 3
    # return (counter == val)


# Check Armstrong number
# print(isArmstrong(2))
#
# print(isArmstrong(100))
#
# # Get all the Armstrong number in range(1000)
# print([_ for _ in range(1000) if isArmstrong(_)])





# n()
# def greeting(first_Name,last_Name):
#     print(f"Hello {first_Name} {last_Name}")
#     print("Welcome")
# greeting("Murtuza" ,"Madarwala")
# def is_prnum(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print('number is not prime')
#             break
#     else:
#         print('the num is prime')
# print(is_prnum(12))






# Nested Loops
# i = 1
# while i<=10:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1

# l = []
# t = ()
# s = set()
# d = {}
# print(type(d))

# i = 0
# while i < 6:
#     i+=1
#     if i ==3:
#         continue
#     print(i)


# lst = ["Book","Pen","Rubber","Pencil"]
# n = input("Enter the value to check: ")
# if n in lst:
#     print(n,"is present in lst")
# else:
#     print(n,"does not exist")


# lst1 = ["Book","Pen","Rubber","Pencil"]
# lst2 = ["Slate","Board","Student","Teacher"]
# lst3 = lst1 + lst2
# print(lst3)

# import math
# n = int(input("Enter the number to check cube: "))
# a = math.sqrt(n)
# print(a)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <=5:
#         print(i)
#     else:
#         print(i,"No is greater than 5")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [n for n in a if n%2==0]
# print(b)

# a = input("Enter the word: ")
# b = reversed(a)
# if list(a)==list(b):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = [i for i in set(a) if i in b]
# print(result)
# import calendar
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
# print(calendar.month(yy, mm))

# a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89} 
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# c = set(a) & set(b)
# print(c)


# n = input("Enter the word: ")
# a = list(n)
# print(a)

# n = int(input("Enter the interger: "))
# print("The divisors of the number are: ")
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# a= int(input("Enter the number: "))
# b= int(input("Enter the number: "))
# c= int(input("Enter the number: "))

# if a > b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# num = int(input("Enter a number: "))
# if num >= 0:
# 		print(num)
# else:
# 		print(-num)


# a = input("Enter the Str: ")
# b= len(a)
# print(b)

# a = int(input("Enter the number: "))
# for i in range(a):
#     print("Hello World")

# a = int(input("enter 1 no: "))
# b = int(input("enter 2 no: "))
# def multiply_number():
#     c = a*b
#     return c 
# d = multiply_number()
# print(d)

    
# list1 = [4, 5, 6, 7]
# list2 = [4, 5]
# print((set(list1) - set(list2)))

# import numpy as np
# n1=np.zeros((5,5))
# n1



# n = int(input("Enter the num: "))
# temp = n
# rev = 0
# while n>0:
#     dig = n%10
#     rev = rev*10+dig
#     n=n//10
# if temp == rev:
#     print(True)
# else:
#     print(False)

# for num in range(7):
#     for x in range(num):
#         print(num,end=" ")
#     print("\n")


# n = int(input("Enter the Number: "))
# temp = n
# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n=n//10
# if temp==rev:
#     print("Palindrom")
# else:
#     print("Not Palindrom")



# def get_sum(n):
#     sum = 0
#     for digit in str(n):
#         sum+= int(digit)
#     return sum
# n = 12345
# print(get_sum(n))

# a = "Hello"
# b = "World"
# a,b = b,a
# print(a,b)

# list = [1, "aalu", 56, 6, 32, "tamaatar", "sabji"  ]
# for items in list:
#     if type(items) == int and items>=6:
#         print(items)

# import pandas as pd
# df = pd.read_csv("heart.csv")
# print(df)
# from pandas_profiling import ProfileReport
# # # Gererate a Report
# profile = ProfileReport(df)
# profile.to_file(output_file= "heart.html")

# try:
#     a = "Murtuza"
#     a[1] = "m"
#     print(a)
#     print(id(a))
# # except:
# #     print("str will not support this as string is not mutable")
# finally:
#     print("Prograam end")


# # Join in Python:
# a = "John","Cena","Big","Show"
# b = " and ".join(a)
# print(b)

# while True:
#     # line = ('>')
#     # if line[0] =='#':
#     #     continue
#     # if line == 'done':
#     #     break
#     # print(line)
# print("Done")
