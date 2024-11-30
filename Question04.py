print()
a = int(input("Enter the First  Number : "))
b = int(input("Enter the Second Number : "))
result1 = a // b
result2 = a / b
result3 = round(result2, 2)
result4 = float(result1)
print("")
print("The Integer Division Result : " + "%.2f" % (result4))
print("The Floor   Division Result : " + str(result3))
