print('Система выведет числовой ряд Фибаначчи по Вашему запросу.')

quantity_number = int(input('Введите необходимое количество последовательных чисел Фибоначчи: '))
fibanachi_list = [1,1]

for number in range(2,quantity_number,1):
    number_fibanachi = fibanachi_list[-1] + fibanachi_list[-2]
    fibanachi_list.append(number_fibanachi)
fibanachi_str = ' '.join(map(str, fibanachi_list))
print(f'{fibanachi_str}')

# Система выведет числовой ряд Фибаначчи по Вашему запросу.
# Введите необходимое количество последовательных чисел Фибоначчи: 10
# 1 1 2 3 5 8 13 21 34 55
