#Write a small calculator application, that allows user to 
# enter two numbers and a symbol, given and then do the operation and print an answer.

number_one, operation, number_two = input("Enter condicion: ")
number_one = int(number_one)
number_two = int(number_two)
operation_list=["+", "-", "*", "/"]

if operation in operation_list:
    if operation == "+":
        answer = number_one + number_two    
    elif operation == "-":
        answer = number_one - number_two    
    elif operation == "*":
        answer = number_one * number_two    
    elif operation == "/":
        answer = number_one / number_two    
print("Answer =", answer)
