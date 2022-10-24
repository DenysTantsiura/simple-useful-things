result = None
operand = None
operator = None
wait_for_number = True

input_value = ''

print("Welcome to the simple calculator ;)\n\nYou can enter operand '+ - / *' and number one by one, starting with a number\nEntering '=' printed result\n")
while operator != "=":
    input_value = input("")
    if wait_for_number:
        try:
            operand = float(input_value)
        except ValueError:
            print(
                "Incorrect input, please try again! ")
            # operator = None  # ?
            continue
        if operator == None:
            result = operand
        else:
            result = (result + operand) if operator == "+" else result
            result = (result / operand) if operator == "/" else result
            result = (result * operand) if operator == "*" else result
            result = (result - operand) if operator == "-" else result
        wait_for_number = False
    else:
        if input_value not in "+-=/*":
            print(
                "Incorrect input, please try again! ")
            continue
        else:
            operator = input_value
            wait_for_number = True

print(result)
