# Find X and Y

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

devider = (a1*b2) - (a2*b1)

if devider == 0:
    print("X and Y is undefined!")
else:
    x = (b2 * c1 - b1 * c2) / devider
    y = (a1 * c2 - a2 * c1) / devider
    print("Your X is: %.2f" % x)
    print("Your Y is: %.2f" % y)
