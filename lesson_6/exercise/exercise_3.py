#allow user to enter two numbers, print out which one is 
# higher than the other, or are they equal?

a = int(input("Enter your  number a"))
b = int(input("Enter your  number b"))

if b > a:
     print("B is the higher!")
if b==a:
    print("=")
else:
    print("A is the higher!")