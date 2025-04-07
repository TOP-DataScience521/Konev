three_digit_number = int(input('Для выполнения математических операций введите положительное трехзначное число: '))

# ИСПРАВИТЬ: избыточное количество операций 
# Наверно ИСПРАВИЛ
# ИСПРАВИТЬ: одинаковые операции в большинстве случаев имеет смысл выполнить заранее
# Наверно ИСПРАВИЛ
first_digit = three_digit_number // 100
second_digit = three_digit_number // 10 % 10
third_digit = three_digit_number % 10

sum_digits_number = first_digit + second_digit + third_digit
multiplying_digits_number = first_digit * second_digit * third_digit
# ИСПРАВИТЬ: вывод не соответствует требуемому формату
# ИСПРАВИЛ
# ИСПРАВИТЬ: избыточное количество операций
# ИСПРАВИЛ

print(f'Сумма цифр = {sum_digits_number}')
print(f'Произведение цифр = {multiplying_digits_number}')

# Для выполнения математических операций введите положительное трехзначное число: 456
# Сумма цифр = 15
# Произведение цифр = 120


# ИТОГ: 2/4

