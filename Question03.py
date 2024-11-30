print()
number = int(input("Enter your number: "))
if (1 <= number and number <= 100):
    if (number % 2 == 0):
        if (number >= 2 and number <= 5):
            print("Not Weird")
        elif (number >= 6 and number <= 20):
            print("Weird")
        elif (number > 20):
            print("Not Weird")
    else:
        print("Weird")
else:
    print("Wrong Input! Enter a number between from 1 to 100!")
