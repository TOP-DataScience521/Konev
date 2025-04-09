print ('Вам необходимо ввести список значений, положительные из них будут сумированны')

number_of_values = int(input('Введите количество значений которые планируете перечислить: '))

attempt_number = 0
sum_natural_numbers = 0

while attempt_number < number_of_values:
    attempts_to_enter = int(input (f'введите значение, осталось {number_of_values-attempt_number} значений:  '))
    attempt_number = attempt_number + 1
    if attempts_to_enter > 0:
        sum_natural_numbers = sum_natural_numbers + attempts_to_enter
    else:
        sum_natural_numbers = sum_natural_numbers  
        
print (f'Сумма введенных Вами положительных чисел: {sum_natural_numbers}')
        
        
#Вам необходимо ввести список значений, положительные из них будут сумированны
#Введите количество значений которые планируете перечислить: 6
#введите значение, осталось 6 значений:  -3
#введите значение, осталось 5 значений:  3
#введите значение, осталось 4 значений:  -2
#введите значение, осталось 3 значений:  2
#введите значение, осталось 2 значений:  -18
#введите значение, осталось 1 значений:  18
#Сумма введенных Вами положительных чисел: 23