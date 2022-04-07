# calculate avarage of some number

sum = 0
count = 0

while 1:
  num = int(input("Enter a number to continue or 0 to exit: "))
  if(num == 0):
    break
  else:
    sum += num
    count += 1

avg = sum / count

print("Total num is: " + str(count))
print("Sum is: " + str(sum))
print("Avg is: {0}".format(avg))
