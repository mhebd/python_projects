# Check a number is prime or not

num = int(input("Enter your number: "))

isPrime = True

if num % 2 == 0:
    isPrime = False
else:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print(str(num) + " is a prime number.")
else:
    print(str(num) + " is not a prime number")
