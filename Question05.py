# Libraries
import math


# Request an user input function
def get_validated_integer_input():
    while True:
        try:
            user_input = int(input("\nEnter an integer between (1 - 20) : "))
            if (user_input >= 1 and user_input <= 20):
                return user_input
            else:
                print(
                    "Invalid Input! Please enter and integer in range of [1, 20]."
                )
        except ValueError:
            print("Invalid Input! Please enter and integer between 1 to 20!")
        except KeyboardInterrupt:
            print("\nError! Input aborted by user.")
        except EOFError:
            print("Error! End of input reached.")
        except Exception as e:
            print("Unexpected Error! : " + e)


# Main Function
def main():
    # Request an input From User
    user_input = get_validated_integer_input()
    # Running a Loop to Get Answer
    for number in range(0, user_input):
        print(int(math.pow(number, 2)))


# Command To Run Main Function
if __name__ == '__main__':
    # Calling Main Function
    main()
