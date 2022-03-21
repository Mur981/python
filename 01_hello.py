# import os
# print (os.listdir())

# import os
# print(os.listdir())

# Name = 'Murtuza' -Str
# Age = 23 Int
# Male = True #Bolain Value
# Height = 5.8 #Flotting value
# print (type (Male)) - None

# Varible type
# a = 'Murtuza' str
# a = 398 Int
# a = 3.9 Floating value
# a = True or False Boolain value
# a = None  None Value 

# Assignment Operators
# a = 3
# b = 9
# b += 9
# b -=2
# print (b)

# a = 12
# b = 2
# b *= 2
# print(a + b)

# Arithmetic Operators
# print ('The value of 3+6 is',3+6)
# print ('The value of 3-6 is',3-6)
# print ('The value of 3*6 is',3*6)
# print ('The value of 3/6 is',3/6)

# Comparison Operators
# b = (14<=7)
# b = (14==7)
# b = (14>7)
# b = (14<7)
# print (b)

# Logical Operators
# Bool1 = True
# Bool2 = False
# print ('The value of Bool1 and Bool2', Bool1 and Bool2) And Function both value should be true or it will give false
# print ('The value of Bool1 or Bool2', Bool1 or Bool2) Or Function One value should be true
# print ('THe value of not Bool2',not Bool2)  Not Function Print Opposite value 

# Bool1 = 12 < 9
# Bool2 = 12 > 9
# # print("The value of Bool 1", Bool1 and Bool2)
# # print("The value of Bool and Bool2", Bool1 or Bool2)
# print('The value of Bool1 and Bool2', not Bool2)

# Typecasting - It is way to convert one data type (variable) to another eg int to Str or vica-versa
# a ='243'
# a = int (a)
# print (type(a))
# b = 23
# print (a + b)

# a = "True"
# print(type(a))
# a = bool(a)
# print(type(a))

# Input Fuction
# a = input ("Enter your name :  ")  Input Function
# b = input ("Age : ")
# b = int(b)
# print (type(b))

# mm = input("Ennter Your Account No Please : ")
# mm=int(mm)
# print(type(mm))
# print(mm)

# Chapter 2 Practice
# Question 1
# a = 89
# b = 4512
# print ("The sum of a and b is = ", a + b)

# a = 34
# b = 32
# print('The Minus value of a and b : ' , a - b)

# Question 2
# a = 15
# b = 3
# print ("The remainder when a is divided by b " ,a%b)

# Question3
# a = input('Enter your password ')
# a = int(a)
# type(a)

# Question4
# a = 34
# b = 80
# print (a>b)

# # Question5 - Avg Function not working
# a = input("Enter your first Number " )
# b = input("Enter your Second Number " )
# a = int(a)
# b = int(b)
# avg = (a + b)/2
# print ("The average of a and b is  ")

# Question6
# a = input ("Enter the number of square ")
# a = int(a)
# print (a * a)

# # Chapter 3 - String Functions
# a = '''all of these lines acros's my face'''
# print (a)
# print (len(a))
# print (a.endswith ('Faceee'))
# print (a.count ('s'))
# print (a.capitalize ())
# print (a.find ('lines'))
# print (a.replace ('face','faces'))
# b= 'These all python are easy to remember \nThey are also easy' - Insert New Line by using \n
# b= 'These all python are easy to remember \tThey are also easy' - Insert tab by using \t
# b = 'These all python are easy to remember The\'y are also easy'  - Insert Appostrofe by using \'
# b = 'These all python are easy to remember \\ They are also easy'  - Insert Slash between by using \\

# str1 = "Finally the Undertaker retires from the WWE"
# str = str1.endswith("WWE") Endswith Function
# # print(str)
# str1 = "Finally the Undertaker retires from the WWE"
# # str = str1.count("the") - Count Function repatation of the word in the str
# print(str)
# # str = str1.capitalize() - capitalize Fuction
# print(str)
# str = str1.find("WWE") - Find Function 
# print(str)
# str = str1.replace("retires", "ends") Replace Function.
# print(str)
# Count,Find,Replace,capitalize - Str Functions
# Escape Sequesce - \n - new line , \t - Tab in sentence or word , \' = Single Quote , \\ - Backslash

# Chapter3 Practice Set
# Question1
# a = input("Enter your Name : ")
# b = " Good Afternoon!!\nHope you are doing well"
# print (a + b)

# Question2
# Letter = ('''Dear <|Name|>,
# You are selected!!
# Date  <|DATE|> ''')
# name = input("Enter your name ")
# date = input("Today's date ")
# Letter = Letter.replace("<|Name|>", name)
# Letter = Letter.replace("<|DATE|>",date)
# print (Letter)

# Weddingcard = '''Dear <|Name|>,
#               Welcome to the Grant Stage of Wedding!!
#               You are invited <|Invitees No|>
#               Date <|Date|>
#               Thank You!! '''
# name = input("Enter you name ")
# InviteesNo =input ("Count of Invites ")
# date = input("Enter date ")
# Weddingcard = Weddingcard.replace("<|Name|>",name) 
# Weddingcard = Weddingcard.replace("<|Invitees No|>",InviteesNo)
# Weddingcard = Weddingcard.replace("<|Date|>",date)
# print (Weddingcard)

# Form = '''<|Name>| Welcome to the ATOS.
#         Date <|Date>| of Joining.
#         Age <|Age>| of Candidate
#         Position <|Position>| Hired.
#         Thanks & Regards <|HR Name>|'''
# name = input("Enter your name : ")
# date = input ("Today's Date : ")
# age  = input("Age : ")
# position = input("Position name : ")
# hrname = input("Sign by HR Name : ")
# Form = Form.replace("<|Name>|", name)
# Form = Form.replace("<|Date>|", date)
# Form = Form.replace("<|Age>|", age)
# Form = Form.replace("<|Position>|", position)
# Form = Form.replace("<|HR Name>|", hrname)
# print(Form)

# Eg = ''' Hello First_Name Second_Name ! You just delved into python.'''

# fn = input("First Name : ")
# sn = input("Second Name : ")
# Eg = Eg.replace("First_Name",fn)
# Eg = Eg.replace("Second_Name",sn)
# print(Eg)

# Question4
# a = "This is my ring and I am the king of this   ring "
# doublespace =a.find('  ')
# print (doublespace)

# # Question5
# a = "This is my ring and I am the king of this  ring "
# sp = a.replace('  '," "  )
# print(sp)

# # Question6
# letter = '''Dear Murtaza,\nThis Python course is nice.\nThanks!! '''
# print (letter)

# # Chapter4- List and Tuples
# List - Mutable and start with []
# a = ['Apple','Mango','Guvava','Grapes']
# print(a)

# Change the value of list of List
# a = ['Apple','Mango','Guvava','Grapes']
# a[0]= 'Banana'
# print(a)

# We can create list of different type
# a = ['Apple','12','9.8','False']
# print(a)

# a= "this is a string"
# a = a.split(" ")
# a = "-".join(a)
# print(a)

# b = "quick brown fox jumps over a lazy dog"
# b = b.split(" ")
# b = "-".join(b)
# print(b)


# # List Slicing
# a = ['Apple','Mango','Guvava','Grapes']
# print(a[0:3])
# print(a[:3])

# List Methods
# a = ['Apple','Mango','Guvava','Grapes']
# a.sort()
# print(a)
# b = [1,3,6,34,63,54]
# # b.sort() - Sort the list
# print(b)

# list = ('Mumbra','Thane','Ambernath','Mulund','Mumbra')
# print(type(list))
# list.count.list(3)

# list.append("Mumbai")
# print(list)
# list.pop()
# print(list)
# list.reverse()
# print(list)
# list.sort()
# print(list)
# print()
# list.remove('Mulund')
# print(list)

# a = ['Apple','Mango','Guvava','Grapes']
# a.reverse() - Reverse the list
# print(a)

# a = ['Apple','Mango','Guvava','Grapes']
# a.append('Lichi') - Adds the value in the list at the end
# print(a) 

# a = ['Apple','Mango','Guvava','Grapes']
# a.insert(3,'dates')  - Insert value in the mentioned index.
# print(a)

# a = ['Apple','Mango','Guvava','Grapes']
# # a.pop(1) - Delelte the element at given index and return the value.
# # print(a)

# a = ['Apple','Mango','Guvava','Grapes']
# a.remove('Apple') - Remove the element from the mentioned index
# print(a)

# Tuples - Start with () and they cannot be edited(immutable). In a single element insert , to define tuple.
# t = (1,2,4,3,5,6)
# print(t)
# Tuple with single element
# t = (1) - Wrong way to declare a tuple with Single element
# t = (1,) Tuple with single emlement
# print(t)

# Tuples Method
# t = (1,2,4,3,5,6,5,3,2,1,)
# # print(t.count(3)) - Counts the elements given in Index.
# t = (1,2,4,3,5,6)
# print(t.index(3))  - Index Function the index value given in index.

# Practice Set for Chap3
# Question1 Please ALT for curser double and click where you want to edit.
# F1 = input("Enter your 1 fruit name")
# F2 = input("Enter your 2 fruit name ")
# F3 = input("Enter your 3 fruit name ")
# F4 = input("Enter your 4 fruit name ")
# F4 = input("Enter your 4 fruit name ")
# F5 = input("Enter your 5 fruit name ")
# F6 = input("Enter your 6 fruit name ")
# F7 = input("Enter your 7 fruit name ")
# myfruitlist = [F1,F2,F3,F4,F5,F6,F6,F7]
# print(myfruitlist)

# Question2
# m1 = int(input("Student Marks 1:  "))
# m2 = int(input("Student Marks 2:  "))
# m3 = int(input("Student Marks 3:  "))
# m4 = int(input("Student Marks 4:  "))
# m5 = int(input("Student Marks 5:  "))
# m6 = int(input("Student Marks 6:  "))
# mylist=[m1,m2,m3,m4,m5,m6]
# mylist.sort()
# print(mylist)

# Question3
# t1 = (1,4,5,3,5,)
# t1[0] = 56

# Question4
# t1 = (1,4,5,3,5,)
# t1 = sum(t1)
# print(t1)

# Question5
# t1 = (7,0,8,0,0,9)
# print(t1.count(0))

a= ()
b= []
c = {}
print(type(a))