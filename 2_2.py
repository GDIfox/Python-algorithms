
def recursia(num, beda=0, ad=0):
    if num == 0:
        return beda, ad
    else:
        chislo = num % 10
        num = num // 10

        if chislo % 2 == 0:
            beda += 1
        else:
            ad += 1
        return recursia(num, beda=0, ad=0)

try:
    NUM = int(input('Введите целое число: '))
    print(f'Количество четных и нечетных цифр: {recursia(NUM)}')
except ValueError:
    print('Введена строка. Введите пожалуйста число')