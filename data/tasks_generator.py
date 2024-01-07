import random
import sqlite3

con = sqlite3.connect('C:/Users/Gleb/Desktop/statpar/pythonProject/pythonProject/pythonProject1/data/tasks.db')
cur = con.cursor()
for i in range(300):
    operator = ('+', '-', '*', '/')[random.randint(0, 3)]
    if operator == '-':
        number2 = random.randint(0, 10)
        number1 = random.randint(number2, 30)
        print('-')
    if operator == '+':
        number1 = random.randint(0, 20)
        number2 = random.randint(0, 20)
        print('+')
    if operator == '*':
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        print('*')
    if operator == '/':
        print('/')
        number1 = random.randint(0, 20)
        number2 = 931
        while number1 % number2 != 0:
            number2 = random.randint(1, 20)

    cur.execute('INSERT INTO tasks (number1, operator, number2, answer) VALUES (?, ?, ?, ?)',
                (number1, operator, number2, int(eval(f'{number1} {operator} {number2}'))))
con.commit()
con.close()