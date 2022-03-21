# INPUT Output Programm Practise:
# Exercise 1: Accept numbers from a user
#Write a program to accept two numbers from the user and calculate multiplication

# a = int(input("Enter your 1st Number: "))
# b = int(input("Enter your 2st Number: "))
# c = a*b
# print("Multiplication is ",c)

#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
#Use the print() function to format the given words in the mentioned format. 
#Display the ** separator between each string.
# print('My', 'Name', 'Is', 'Murtuza', sep='**')

## Exercise 3: Convert Decimal number to octal using print() output formatting
# num = 8
# print("%o"% num)

# #Exercise 4: Display float number with 2 decimal places using
# num = 458.541315
# print("%.2f" % num)

# #Exercise 5: Accept a list of 5 float numbers as an input from the user
# numbers = []
# for i in range (0,5):
#     print("Enter number location",i,": ")
#     a = float(input())
#     numbers.append(a)
# print("User List",numbers)

#Exercise 6: Write all content of a given file into a new file by skipping line number 5:
# with open("test.txt", "r") as fp:
#     # read all lines from a file
#     lines = fp.readlines()

# # open new file in write mode
# with open("new_file.txt", "w") as fp:
#     count = 0
#     # iterate each lines from a test.txt
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
#             # write current line
#             fp.write(line)
#         # in each iteration reduce the count
#         count += 1

##Exercise 7: Accept any three string from one input() call::::
# str1, str2, str3 = input("Enter three string: ").split()
# print('Name1:', str1)
# print('Name2:', str2)
# print('Name3:', str3)

#OR

# ie = input('Enter more names by using space in between!')

# ie = ie.split()
# print('\n')

# for i in range(len(ie)):
#     print(f'Name {i}: {ie[i]}')


##Exercise 8: Format variables using a string.format() method.
##Write a program to use string.format() method to format the following three variables as per the expected output

# totalMoney = 1000
# quantity = 3
# price = 450

# print(f"I have {totalMoney} dollars so I can buy {quantity} for {price} dollars")


##Exercise 9: Check file is empty or not
# import os

# size = os.stat("test.txt").st_size
# if size == 0:
#     print('file is empty')

# ##Exercise 10: Read line number 4 from the following file
# # read file
# with open("test.txt", "r") as fp:
#     # read all lines from a file
#     lines = fp.readlines()
#     # get line number 3
#     print(lines[2])


##-------------------------------------LOOP--------------------------------------------------------------------##

##Exercise 1: Print First 10 natural numbers using while loop
# start = 0
# while start <= 10:
#     print(start)
#     start+=1

 ##Exercise 2 - Print the following pattern
 ##Write a program to print the following number pattern using a loop.

# print("Number Pattern ")

# # Decide the row count. (above pattern contains 5 rows)
# row = 5
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")

##Exercise 3: Calculate the sum of all numbers from 1 to a given number
# s: store sum of all numbers
# s = 0
# n = int(input("Enter number "))
# # run loop n times
# # stop: n+1 (because range never include stop number in result)
# for i in range(1, n + 1, 1):
#     # add current number to sum variable
#     s += i
# print("\n")
# print("Sum is: ", s)
# ########OR###############
# n = int(input("Enter number "))
# # pass range of numbers to sum() function
# x = sum(range(1, n + 1))
# print('Sum is:', x)

##Exercise 4: Write a program to print multiplication table of a given number

from math import factorial
from numpy import number


# n =2
# for i in range(1,11):
#     p = n*i
#     print(n,"X",i,"=",p)

##Exercise 5: Display numbers from a list using loop:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i>500:
#         break
#     if i>150:
#         continue
#     if i%5==0:
#         print(i)

##Exercise 6: Count the total number of digits in a number
# num = 75869
# count = 0
# while num != 0:
#     num = num//10
#     count+=1
# print(count)



##Exercise 7: Print the following pattern
# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()


##Exercise 8: Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for i in new_list:
#     print(i)


##Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10,-0):
#     print(i)

# ##Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# for i in range(1,6):
#     print(i)
# else:
#     print("Done!!")

##Exercise 11: Write a program to display all prime numbers within a range---IMP
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)

## Exercise 12: Display Fibonacci series up to 10 terms ---IMP
# num = 0
# num2 = 1
# for i in range(11):
#     print(num,end=" ")
#     res = num +num2
#     num=num2
#     num2=res

#Exercise 13: Find the factorial of a given number
# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)


# num = 5
# factorial = 1
# for i in range(1,num+1):
#     factorial= factorial*i
#     print("The factorial of", num, "is", factorial)

#Exercise 14: Reverse a given integer number----IMP---
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

##Exercise 15: Use a loop to display elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#     print(i,end=" ")

#Exercise 16: Calculate the cube of all numbers from 1 to a given number
# input_num = 6
# for i in range(1,input_num+1):
#     c= i*i*i
#     print(f'Current Number is :", {i}, " and the cube is {c}')


##Exercise 18: Print the following pattern
# row = 5
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("#",end=" ")
#     print('\r')
# for i in range(row,0,-1):
#     for j in range(0,i-1):
#         print("#",end=" ")
#     print("\r")

#############################STRING EXCERSICE############################################
















