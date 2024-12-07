

def get_number():
    while True:
        operand = input("Number 1: ")
        try:
            return  float(operand)
        except:
            print("Invaled number, try again.")
            

operand = get_number()
operand2 = get_number()

sign = input("Sign: ")


valid = False
# If an invalid number(s) were to be input, this would catch it and
# respond to display why; also cleans our code(DRY method)


if valid:
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