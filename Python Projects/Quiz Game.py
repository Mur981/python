print("Welcome to my computer quiz game!!")
playing = input("Do you want to play this game? ")
if playing.lower() !="yes":
    quit()

print("Okay..Let's Play :)")

score = 0

answer = int(input("In which year of First World War Germany declared war on Russia and France? : "))
if answer == 1914:
    print("Congrats!!...Correct Answer")
    score+=1
else:
    print("Oopppss.....Incorrect")

answer = input("RAM stands for: ")

if answer.upper() == "random access memory":
    print("Congrats!!...Correct Answer")
    score+=1
else:
    print("Oopppss.....Incorrect")

answer = input("India has largest deposits of in the world: ")
if answer.upper() == "Mica":
    print("Congrats!!...Correct Answer") 
    score+=1
else:
    print("Oopppss.....Incorrect")

answer = int(input("How many Lok Sabha seats belong to Rajasthan?.: "))
if answer == 25:
    print("Congrats!!...Correct Answer")
    score+=1
else:
    print("Oopppss.....Incorrect")

print("Game End:" + " " +"Your score",str(score))
print("Game End:" + " " +"Total Percentage",str((score/4)*100)+"%")
