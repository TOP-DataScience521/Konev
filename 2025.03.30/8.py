print ('Система определить может ли введенная Вами строка являться двоичным значением.')
code = input('Введите строку с предполагаемым двоичным значением: ')

code_index_1 = code[:1]
code_index_2 = code[:2]
code_index2_to_last = code[2:]

checking_index1i2_code_na_b_ob = 0
checking_index1i2_code_na_1_0 = 0
checking_index2_code_1_1 = 0
checking_full_code_binary = 0

binary_symbol = {'0','1'}
code_index2_for_last_set = set(code_index2_to_last)
code_index_2_set = set(code_index_2)

if (('b' == code_index_1) + ('0b' == code_index_2)) > 0:
    checking_index1i2_code_na_b_ob = 1
else:
    if 1 == code_index_2_set.issubset(binary_symbol):
        checking_index1i2_code_na_1_0 = 1

if 1 == code_index2_for_last_set.issubset(binary_symbol):
    checking_index2_code_1_1 = 1

if ((checking_index1i2_code_na_b_ob + checking_index1i2_code_na_1_0) + checking_index2_code_1_1) > 1:
    checking_full_code_binary = 1
    print (f'Введенная Вами строка ЯВЛЯЕТСЯ двоичным значением')  
else:
    print (f'Введенная Вами строка НЕ ЯВЛЯЕТСЯ двоичным значением')    



