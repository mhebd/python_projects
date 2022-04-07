# Linear interest calculator

base_mony = int(input("Enter your base money: "))
rate = int(input("Enter interest rate: "))
year = int(input("Enter total year: "));

interest = base_mony * (rate / 100) * year

print("Your interest is: " + str(interest))