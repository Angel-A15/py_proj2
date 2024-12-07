# get_number function will gather input from user to define operands selected by user
def get_number(number):
    while True:     # Loop will repeat until two operands are selected by user 
        operand = input("Number " + str(number) + ": ") # variable input will display how many/which number the user needs to fill in; based on parameter from function
        try:            #If a valid operand is selected, the user will be asked to choose a number until function calls are used up
            return  float(operand)
        except:
            # If theres an invalid number,this would catch it and tell the user to try a valid option
            print("Invaled number, try again.")
            
# variables will each call the function with a listed argument
operand = get_number(1)
operand2 = get_number(2)

#sign will be next to select 
sign = input("Sign: ")


# based on sign selected, operands will follow selected arithmatic operation 
result = 0
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "**":
    result = operand **operand2
elif sign == "%":
    result = operand % operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Division by zero.")
elif sign == "*":
    result = operand * operand2

print(result)

