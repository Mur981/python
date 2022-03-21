year = int(input("Enter the year to check the Leap year: "))

if year % 400 == 0:
    print(f"{year} It is the Leap year")
elif year % 4 == 0:
    print(f"{year} It is the Leap year")
elif year % 100 == 0:
    print(f"{year} It is not a leap year")
else:
    print(f"{year} It is not a leap year")