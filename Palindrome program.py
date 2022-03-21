#  Palindrome phrase number or a sequence will be same even if it is written backwards
#  Eg = Madam it written backwards it will be same Madam

# def pal(num):
#     a == num[::-1]
#     if a = num:
#         print("Palidrome")
#     else:
#         print("Not Palidrom")

# print(pal('madam'))

n = input("Enter the strg to check: ")
a = n.casefold()   "Casefold  function will convert str into lowercase."
b = reversed(a)
if list(a) == list(b):
    print("It is palindrome")
else:
    ("it is not")


n = input("Enter the strg to check: ")
b = reversed(n)
if list(n) == list(b):
    print("It is palindrome")
else:
    ("it is not")


# Program to get the length of str without using len function
a ="Hello World I am at jungle"
b = 0
for i in a:
        b=b+1
print(b)

a = input("Enter the String: ")
b = reversed(a)
if list(a) == list(b):
    print("It is palindrome")
else:
    print("It is not")


                                    # OR

number=int(input("Enter any number :"))
#store a copy of this number
temp=number
reverse_num=0 #calculate reverse of this number
while(number>0): #extract last digit of this number
    digit=number%10 #append this digit in reveresed number
    reverse_num=reverse_num*10+digit #floor divide the number leave out the last digit from number
    number=number//10
#compare reverse to original number
if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")