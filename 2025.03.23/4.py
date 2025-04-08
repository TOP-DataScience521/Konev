print('Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности \nи сообщит Вам их количество.')
number_digits = int(input('Введите любую разрядность: '))

max_number_int = int(str(9) * number_digits)
min_number_int = int(str(9) * (number_digits - 1))+1

list_all_number = list(range(min_number_int, max_number_int, 1))
number_prime_numbers = 0



for number_of_list in list_all_number:
    if number_of_list < 2:
        continue 
    sign_of_prime_number = 1
    root_number_of_list =(int(number_of_list ** (1/2)) +1)
    for possible_divisor in range(2, root_number_of_list, 1):
        if number_of_list % possible_divisor == 0:
            sign_of_prime_number = 0
            break
    if sign_of_prime_number > 0:
        number_prime_numbers = number_prime_numbers + 1

print(f'Количество всех простых чисел в пределах Вашей разрядности: {number_prime_numbers}')



#Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности
#и сообщит Вам их количество.
#Введите любую разрядность: 3
#Количество всех простых чисел в пределах Вашей разрядности: 143

#Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности
#и сообщит Вам их количество.
#Введите любую разрядность: 2
#Количество всех простых чисел в пределах Вашей разрядности: 21