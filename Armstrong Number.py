# Armstrong number: A number is called Armstrong number if it is equal to the sum of the cubes of its own digits. 
# For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.


# n = int(input("Enter your Number : "))
# a = list(map(int,str(n)))
# b= list(map(lambda x:x **3,a))
# if (sum(b)==n):
#    print("True")
# else:
#    print("False")



                                        # OR
# num = 167
# # Changed num variable to string,
# # and calculated the length (number of digits)
# order = len(str(num))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** order
#    temp //= 10

#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")