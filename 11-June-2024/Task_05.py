# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400
# Ex : input 2024
# Output : Leap Year


year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
