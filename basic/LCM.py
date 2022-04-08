# Least common multiple

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

mul = num1 * num2
smallNum = None
hcf = None

if num1 <= num2:
    smallNum = num1
elif num2 <= num1:
    smallNum = num2

while smallNum >= 1:
    if num1 % smallNum == 0 and num2 % smallNum == 0:
        hcf = smallNum
        break
    smallNum -= 1

lcm = mul / hcf
print("Your LCM is: %.2f" % lcm)
