#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
#You can use input to receive the number. Example:
#n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dicta_one = {1:10, 2:40}
dicta_two = {3:10, 4:15}
dicta_tree ={5:40, 6:40}

dicta_one.update(dicta_two)

dicta_one.update(dicta_tree)

print(dicta_one)


