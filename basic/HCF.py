# Highest common factor

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

smallNum = None

if num1 <= num2:
    smallNum = num1
elif num2 <= num1:
    smallNum = num2

while smallNum >= 1:
    if num1 % smallNum == 0 and num2 % smallNum == 0:
        print("Your HCF is: " + str(smallNum))
        break
    smallNum -= 1
