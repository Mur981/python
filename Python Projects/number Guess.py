import random
from winreg import REG_NO_LAZY_FLUSH
Range_Number = input("Enter the number: ")
if Range_Number.isdigit():
    Range_Number = int(Range_Number)
    if Range_Number <=0:
        print("Please enter the number which is greater than 0.")
        quit()
else:
    print("Please enter the number which is greater than 0.")
    quit()

random_number = random.randint(0,Range_Number)
print(random_number)
no_guesses = 0
while True:
    no_guesses+=1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter the number.")
        quit()
        continue

    if user_guess == random_number:
        print("Congrats...You got that Right!!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print("You got the correct answer :", no_guesses , "guesses")