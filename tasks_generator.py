import random
def tasks_generator(x):
    operator = ('+', '-', '*', '/')[random.randint(0, 3)]
    if x == 1:
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
    else:
        if operator == '-':
            number2 = random.randint(20, 50)
            number1 = random.randint(number2, 70)
        if operator == '+':
            number1 = random.randint(10, 40)
            number2 = random.randint(10, 50)
        if operator == '*':
            number1 = random.randint(6, 12)
            number2 = random.randint(5, 12)
        if operator == '/':
            number1 = random.randint(10, 50)
            number2 = 931
            while number1 % number2 != 0:
                number2 = random.randint(5, 50)
    return (number1, operator, number2, int(eval(f'{number1} {operator} {number2}')))

