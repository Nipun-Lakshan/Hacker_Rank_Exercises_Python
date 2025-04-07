def is_leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False


def get_validated_integer_input():
    while True:
        try:
            user_input = int(input("\nEnter a year (1900 - 1000000) : "))
            if (user_input >= 1900 and user_input <= 1000000):
                return user_input
            else:
                print(
                    "Invalid Input! Please enter a year between [1900, 1000000]."
                )
        except ValueError:
            print(
                "Invalid Input! Please enter a year between 1900 to 1000000!")
        except KeyboardInterrupt:
            print("\nError! Input aborted by user.")
        except EOFError:
            print("Error! End of input reached.")
        except Exception as e:
            print("Unexpected Error! : " + e)


def main():
    year = get_validated_integer_input()
    print(str(year) + " is a leap year : " + str(is_leap_year(year)))


if __name__ == "__main__":
    main()
