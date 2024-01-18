import random
def tasks_generator():
    operator = ('+', '-', '*', '/')[random.randint(0, 3)]
    if operator == '-':
        number2 = random.randint(3, 10)
        number1 = random.randint(number2, 30)
    if operator == '+':
        number1 = random.randint(3, 20)
        number2 = random.randint(2, 20)
    if operator == '*':
        number1 = random.randint(2, 10)
        number2 = random.randint(2, 10)
    if operator == '/':
        number1 = random.randint(2, 20)
        number2 = 931
        while number1 % number2 != 0:
            number2 = random.randint(2, 20)
    return (number1, operator, number2, int(eval(f'{number1} {operator} {number2}')))
