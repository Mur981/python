# 1.  Given the sample dic - How would you update the value of "Apple" from 10 to 100
# fruit = {"Apple":10,"Organge":20,"Banana":30,"Guava":40}
# fruit["Apple"] = 100
# print(fruit)
# --------------------------------------------------------------------------------------
# 2. How would you find common elements present in the given two sets?
# a= {1,2,4,5,6,}
# b= {5,6,7,8,9}
# print(a.intersection(b))
# ------------------------------------------------------------------------------------------
# 3. Palindrome program
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
#             OR
# def pal(num):
#     a = num[::-1]
#     if a == num:
#         print("Palidrome")
#     else:
#         print("Not Palidrom")

# print(pal('121'))

# 5. Program that Points the Following Pattern
# for int_num in range(6):
#     for i in range(int_num):
#         print(int_num,end=" ")
#     print("\n")
# -------------------------------------------------------------------------------------
# 6. Print program in below pattern:
# def pattern_print(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("#",end="")
#         print("\r")
# pattern_print(5)
#  OR
# for i in range(11):
#     for j in range(i):
#         print("*",end=" ")
#     print("\r")


# --------------------------------------------------------------------------------------
# 7. Print 20 Prime Numbers
# def is_Prime (n):
#     for i in range (2,n):
#         if not (n % i):
#             return False
#     return True

# for n in range(1,200):
#     if is_Prime(n):
#         print(n)
# -------------------------------------------------------------------------------
# 11. If you have dic like this d1={"k1:10,"k2:20,k3:30}. How would you increment values in 
# all the Keys?
d1 = {"k1":10,"k2":20,"k3":30}
for i in d1.keys():
    d1[i] = d1[i] + 10
d1.values()


    
