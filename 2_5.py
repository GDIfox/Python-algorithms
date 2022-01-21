def chr_row(ascii_val=32):
    if ascii_val == 128:             # через Рекурсию
        return True                  # базовый случай
    print(f'{ascii_val} - {chr(ascii_val)}', end=' ')  # возвращение символа по коду (функ. chr())
    if (ascii_val - 31) % 10 == 0:   # формула перевода строки
        print('\n')

    chr_row(ascii_val + 1)


chr_row()