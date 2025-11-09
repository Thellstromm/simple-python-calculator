print("Enter first number: ")
while True:
    try:
        firstNumber = float(input()) #input for first number
        break
    except ValueError: # if input is not a valid float
        print("Invalid input. Please enter a valid number:")


print("Enter operator (+, -, *, /): ")
operator = input() # input for operator
while operator not in ["+", "-", "*", "/"]: # loop to get valid operator input
 print("Invalid operator. Please enter a valid operator:")
 operator = input() 

print("Enter second number: ")
while True:
    try:
        secondNumber = float(input()) #input for second number
        break
    except ValueError: # if input is not a valid float
        print("Invalid input. Please enter a valid number:")


if operator == "+": # checks which operator to use
    result = firstNumber + secondNumber 
elif operator == "-":
    result = firstNumber - secondNumber
elif operator == "*":
    result = firstNumber * secondNumber
elif operator == "/":
    result = firstNumber / secondNumber

if firstNumber.is_integer(): # checks if first number is integer or float
   firstNumber = int(firstNumber) # converts to integer if no decimal part

if secondNumber.is_integer(): # checks if second number is integer or float
    secondNumber = int(secondNumber) # converts to integer if no decimal part

if result.is_integer(): # checks if result is integer or float
        result = int(result) # converts to integer if no decimal part
        print(firstNumber, operator, secondNumber, "=", result) # prints the result
else:
        result = float(result) # keeps as float if float
        print(firstNumber, operator, secondNumber, "=", result) # prints the result
