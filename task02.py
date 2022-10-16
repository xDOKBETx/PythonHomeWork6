# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

math_signs = {
    '+': (1, lambda x, y: float(x + y)),
    '-': (1, lambda x, y: float(x - y)),
    '*': (2, lambda x, y: float(x * y)),
    '/': (2, lambda x, y: float(x / y))
}


def parsing(line):
    num = ''
    for i in line:
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in math_signs or i in '()':
            yield i
    if num:
        yield float(num)


def sorting(parsed):
    tmp = []
    for i in parsed:
        if i in math_signs:
            while tmp and tmp[-1] != '(' and math_signs[i][0] <= math_signs[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()


def mathematical_expression_calculation(sort):
    tmp = []
    for i in sort:
        if i in math_signs:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(math_signs[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]


expression = input('Введите математическое выражение: ')
print('Результат вычисления: ', mathematical_expression_calculation(sorting(parsing(expression))))
