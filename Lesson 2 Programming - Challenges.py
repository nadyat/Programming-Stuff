#easy
print("Computing \n \nis \n \namazing") #this line prints the phrase "Computing is amazing", using the \n to split the string into different lines
#hardish
a, b, c = map(int, input("Input your numbers, splitting them with a space").split()) #this saves the inputs, using the "map" function to split a single input into 3 seperate values
print (a + b + c) #This prints the sum of the 3 user input values
print ((a+b+c)/3) #This prints the average of the values (sum of the values/number of values)
#harder
x, y = map(int, input("Input your numbers, splitting them with a space").split()) #This saves the inputs to variables x and y, using the map function to split the single line input into 2 values
print (x//y) #This prints the modulo of the two values
print(x%y) #This prints the remainder
#hardest
money=int(input())
twenties= money//20
money=money - twenties*20
tens=money//10
money=money-tens*10
fives=money//5
money=money-fives*5
twos=money//2
money=money-twos*2
ones=money//1
money=money-ones
print(money)
print("RM20:" + str(twenties) + "; RM10:" + str(tens) + "; RM5:" + str(fives) + "; RM2:" + str(twos) + "; RM1:" + str(ones))


