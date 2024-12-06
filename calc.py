operand = input("Number 1: ")
operand2 = input("Number 2: ")
sign = input("Sign: ")


valid = False
# If an invalid number(s) were to be input, this would catch it and
# respond to display why; also cleans our code(DRY method)
try:
    operand = float(operand)
    operand2 = float(operand2)
    valid = True
except:
    print("Ivalid operand")

if valid:
    result = 0
    if sign == "+":
        result = operand + operand2
    elif sign == "-":
        result = operand - operand2
    elif sign == "/":
        if operand2 != 0:
            result = operand / operand2
        else:
            print("Division by zero.")
    elif sign == "*":
        result = operand * operand2
    # elif sign == "**":
    #     result = operand **operand2
    # elif sign == "%":
    #     result = operand % operand2
    print(result)