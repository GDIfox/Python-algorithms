
def obratnoe_chislo(chislo):
    obr_chislo, cifra = divmod(chislo, 10)
    if obr_chislo == 0:
        return str(cifra)
    else:
        return str(cifra) + str(obratnoe_chislo(obr_chislo))


chislo = int(input('Введите число пожалуйста: '))
print(f'Перевернутое число: {obratnoe_chislo(chislo)}')

#
# def obratnoe_chislo(chislo):
# return str(chislo) if chislo < 10 else str(chislo % 10) + return str(chislo // 10)
# - решение через тернарный оператор.