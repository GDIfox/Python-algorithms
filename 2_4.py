
def sum_elem_met(i, chislo, kol_elem, sum_elem):
    if i == kol_elem:
        print(f'Количество эелементов - {kol_elem}, их сумма- {sum_elem}')
    elif i < kol_elem:
        return sum_elem_met(i + 1, chislo / 2 * -1, kol_elem, sum_elem + chislo)


try:
    kol_elem = int(input('Введите количество элементов: '))
    sum_elem_met(0, 1, kol_elem, 0)
except ValueError:
    print('Введена строка, необходимо ввести число')

# метод решения через тернарный оператор
# def sum_elem_met(element):
#   return 0 if element == 0 else 1 + sum_elem_met(element - 1) / 2
#
#
# kol_elem = int(input()"Введеите количество элементов: ")
# print(f"Количество эементов: {kol_elem}, их сумма: {sum_elem_met(kol_elem)}")
