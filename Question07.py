def print_as_a_string(number):
    for i in range(1, (number + 1)):
        print(i, end="")
    print()


def get_validated_integer_input():
    while True:
        try:
            user_input = int(input("\nEnter an integer between (1 - 150) : "))
            if (user_input >= 1 and user_input <= 150):
                return user_input
            else:
                print(
                    "Invalid Input! Please enter and integer in range of [1, 150]."
                )
        except ValueError:
            print("Invalid Input! Please enter and integer between 1 to 150!")
        except KeyboardInterrupt:
            print("\nError! Input aborted by user.")
        except EOFError:
            print("Error! End of input reached.")
        except Exception as e:
            print("Unexpected Error! : " + e)


def main():
    number = get_validated_integer_input()
    print("Consecutive Values as a String from 1 to " + str(number) + " : ",
          end="")
    print_as_a_string(number)


if __name__ == "__main__":
    main()
