x=float(input()) #
if x==0:
    print("Number is equal to 0")
else:
    print("Number is not equal to 0")
if x<=0:
    print("Number is less than or equal to zero")
else:
    print("Number is larger than 0")
if 1<x<20:
    print("Number is between 1 an 20 exclusive")
else:
    print("Number is not between 1 an 20 exclusive")
if 1<=x<=20:
    print("Number is between 1 and 20 inclusive")
else:
    print("Number is not between 1 and 20 inclusive")
if 1<x<10 or 100<x<120:
    print("Number is either between 1 and 10 or between 100 and 120 exclusive")
else:
    print("Number is not either between 1 and 10 or between 100 and 120 exclusive")
