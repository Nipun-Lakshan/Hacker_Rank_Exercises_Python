def get_list_with_all_combinations(integer_list_for_x, integer_list_for_y,
                                   integer_list_for_z, n):
    final_list = []
    for i in range(0, len(integer_list_for_x)):
        for j in range(0, len(integer_list_for_y)):
            for k in range(0, len(integer_list_for_z)):
                temp = []
                sum = i + j + k
                if (sum != n):
                    temp.append(i)
                    temp.append(j)
                    temp.append(k)
                    final_list.append(temp)
    return final_list


def get_integer_list(number, limit):
    list = []
    for i in range(0, (number + 1)):
        list.append(i)
    return list


def get_validated_integer_input(symbol):
    while True:
        try:
            user_input = int(
                input("Enter an integer for " + symbol +
                      " greater than or equal to 0 : "))
            if (user_input >= 0):
                return user_input
            else:
                print(
                    "Invalid Input! Please enter an integer greater than or equal to 0.\n"
                )
        except ValueError:
            print(
                "Invalid Input! Please enter an integer greater than or equal to 0.\n"
            )
        except KeyboardInterrupt:
            print("\nError! Input aborted by user.\n")
        except EOFError:
            print("Error! End of input reached.\n")
        except Exception as e:
            print("Unexpected Error! : " + e + "\n")


def get_validated_integer_input_1(symbol):
    while True:
        try:
            user_input = int(
                input("Enter an integer for " + symbol +
                      "                            : "))
            return user_input
        except ValueError:
            print(
                "Invalid Input! Please enter an integer greater than or equal to 0.\n"
            )
        except KeyboardInterrupt:
            print("\nError! Input aborted by user.\n")
        except EOFError:
            print("Error! End of input reached.\n")
        except Exception as e:
            print("Unexpected Error! : " + e + "\n")


def main():
    print()
    x = get_validated_integer_input("x")
    print()
    y = get_validated_integer_input("y")
    print()
    z = get_validated_integer_input("z")
    print()
    n = get_validated_integer_input_1("n")
    print()

    integer_list_for_x = get_integer_list(x, n)
    integer_list_for_y = get_integer_list(y, n)
    integer_list_for_z = get_integer_list(z, n)

    print(
        get_list_with_all_combinations(integer_list_for_x, integer_list_for_y,
                                       integer_list_for_z, n))


if __name__ == "__main__":
    main()
