def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'Can\'t divide by 0!'
    elif operator == '*':
        return num1 * num2
    elif operator == '-':
        return num1 - num2
    else:
        pass


def calculator(num1, operator, num2):
    try:
        return eval(str(num1) + operator + str(num2))
    except ZeroDivisionError:
        return "Can\'t divide by 0!"
