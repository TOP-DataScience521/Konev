# очень крутая задача, много чего перепробовал пока не вычитал метод с корнями, спасибо

print ('Вам потребуется ввести положительное число, система определит все делители числа и сумирует их')

input_number = int(input('Введите любое целое положительное число: '))

# из теоремы факторизации следует, что можно при поиске делителей ограничится перебором 
# чисел от 2 до n**(1/2), в связи с этим определяем последовательность предполагаемых делителей
root_input_number = int(input_number ** (1/2)) + 1
list_numbers_iterate  = list(range(2,root_input_number,1)) 
list_brute_force_divisors = []
list_paired_divisors = []
sum_of_the_divisors = 0
number_of_iterations = 0

# Цикл добавляет в список значения на которое число делиться на цело,
# дополнительно определяется и добавляется в список парное значение нацело делящих чисел, 
# как нистранно повторных значений в списке не обнаруживается, иначе пришлось бы переводить список в множество
for number_brute_force in list_numbers_iterate :
    number_of_iterations = number_of_iterations + 1
    if input_number % number_brute_force == 0:
        list_brute_force_divisors.append(number_brute_force)
        parni_delitel = int(input_number / number_brute_force)
        list_paired_divisors.append(parni_delitel)
        
list_brute_force_divisors.extend(list_paired_divisors)
print (f'вывод всех делителей кроеме 1 и {input_number}: {list_brute_force_divisors}')
sum_of_the_divisors = sum(list_brute_force_divisors) + 1 + input_number
print (f'вывод суммы всех делителей: {sum_of_the_divisors}')

# даже если не использовать теорию факторизации то я бы выбрал последоваельность делителей от 2 до n/2
print (f'количество произведенных итераций: {number_of_iterations}, это меньше чем количество итераций при прямом переборе на {int((input_number - number_of_iterations)/2)}')
        

# Вам потребуется ввести положительное число, система определит все делители числа и сумирует их
# Введите любое целое положительное число: 65
# вывод всех делителей кроеме 1 и 65: [5, 13]
# вывод суммы всех делителей: 84
# количество произведенных итераций: 7, это меньше чем количество итераций при прямом переборе на 29

