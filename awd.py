tupoepervoezadanie = []
kostylnyy_spisok = []
chisla = input('Введите число (или "стоп" для выхода): ')
while str(chisla) != 'стоп':
    if tupoepervoezadanie.count(chisla) == 0:
        tupoepervoezadanie.append(chisla)
    kostylnyy_spisok.append(chisla)
    chisla = input('Введите число (или "стоп" для выхода): ')
print('Исходный список: ', kostylnyy_spisok)
print('Список без дупликатов: ', tupoepervoezadanie)