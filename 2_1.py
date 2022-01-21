
def calculator():
    oper_input = input('Введите операцию (+, -, *, /, или 0 для выхода): ')

    if oper_input == '0':
        return 'Выход'
    else:
        if oper_input in '+-*/':
            try:
                num_1 = int(input('Введите первое число: '))
                num_2 = int(input('Введите второе число: '))

                if oper_input == '+':
                    res = num_1 + num_2
                    print(f'Решение {res}')
                    return calculator()

                elif oper_input == '-':
                    res = num_1 - num_2
                    print(f'Решение {res}')
                    return calculator()

                elif oper_input == '*':
                    res = num_1 * num_2
                    print(f'Решение {res}')
                    return calculator()

                elif oper_input == '/':
                    try:
                        res = num_1 / num_2
                    except ZeroDivisionError:
                        print('Деление на Ноль(0) не возможно')
                    else:
                        print(f'Решение {res}')
                        return calculator()
            except ValueError:
                print('Введена строка, необходимо исправить')
                return calculator()
        else:
            print('Введен неверный символ, необходимо исправить')
            return calculator()