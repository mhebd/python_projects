# Geometry area claculator

from math import sqrt


def triangle():
    line1 = int(input('Enter first line length: '))
    line2 = int(input('Enter second line length: '))
    line3 = int(input('Enter thrid line length: '))
    s = (line1 + line2 + line3) / 2
    area = sqrt(s*(s-line1)*(s-line2)*(s-line3))
    return area


def rectangle():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length * width
    return area


def square():
    length = int(input('Enter length: '))
    area = length * length
    return area


def circle():
    radius = int(input('Enter radius: '))
    area = 3.1416 * (radius * radius)
    return area


switcher = {
    1: triangle,
    2: rectangle,
    3: square,
    4: circle,
}

while 1:
    print('1. Triangle \n2. Rectangle \n3. Square \n4. Circle \n0 to exit...')
    mtd = int(input('Choose your option: '))

    if(mtd == 0):
        break

    print("your area is: %.2f \n\n" % switcher.get(mtd)())
