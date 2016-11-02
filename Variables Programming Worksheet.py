#Task 1 : 100th Birthday
name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
currYear=int(input("What is the current year?"))
hundredYear=(100-age)+currYear
print("Nice to meet you "+name+"\nIn the year "+str(hundredYear)+" you will be 100 years old.")

#Task 2 : Cylinders
pi=3.1415926
radius=int(input("Enter radius of cylinder: "))
height=int(input("Enter height of cylinder: "))
vol=pi*radius*radius*height
sa=2*pi*radius*(radius+height)
print("The volume is "+str(vol)+"\nThe total surface area is: "+str(sa)+"")
