# обьявление переменных
cycle_enabled = 1
list_numbers = []

while cycle_enabled == 1:
    input_numbers = int(input('Введите любое целое число на Ваш взгляд кратное 7: '))
    if input_numbers % 7 == 0 :
        cycle_enabled = 1
        list_numbers.append(input_numbers) 
    else: 
        cycle_enabled = 0
        
list_numbers.reverse()
numbers_str = ' '.join(map(str, list_numbers))

print (f'Вывод правильно введеных Вами значений в обратном порядке: \n {numbers_str}')       
    
# Введите любое целое число на Ваш взгляд кратное 7: 7
# Введите любое целое число на Ваш взгляд кратное 7: 14
# Введите любое целое число на Ваш взгляд кратное 7: 21
# Введите любое целое число на Ваш взгляд кратное 7: 77
# Введите любое целое число на Ваш взгляд кратное 7: 777
# Введите любое целое число на Ваш взгляд кратное 7: 45
#Вывод правильно введеных Вами значений в обратном порядке:
# 777 77 21 14 7