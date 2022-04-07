while 1:
  num = int(input("Enter a number to continue or 0 to exit: "));
  if num == 0:
    break;
  elif num % 2 == 0:
    print("{0} is a even number".format(num));
  elif num % 2 != 0:
    print(str(num) + " is a odd number.");
  else:
    print('Something went wrong!');