#Let user enter name, surname and age. Print if user is allowed to enter 
# an online casino or not. 21 is the age cap.


name= str(input("Enter your name:"))
surname= str(input("Enter your surname:"))
number= int(input("Enter your age:"))

if number>=21:
    print("You are allowed to enter")
elif number == 21:
    print("You are alowed!")
elif number < 21:
    print("You are not alowed!")
else: 
    print(f"you have entered {number}")
