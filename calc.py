operand = input("Number 1: ")
operand2 = input("Number 2: ")
sign = input("Sign: ")

# If an invalid number(s) were to be input, this would catch it and
# respond to display why; also cleans our code(DRY method)
try:
    operand = float(operand)
    operand2 = float(operand2)
except:
    print("Ivalid operand")


if sign == "+":
    result = float(operand) + float(operand2)
elif sign == "-":
    result = float(operand) - float(operand2)
elif sign == "/":
    if float(operand2) != 0:
        result = float(operand) / float(operand2)
    else:
        print("Division by zero.")
elif sign == "*":
    result = float(operand) * float(operand2)
elif sign == "**":
    result = float(operand) ** float(operand2)
elif sign == "%":
    result = float(operand) % float(operand2)
print(result)