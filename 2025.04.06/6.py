# словарь до 32 счислений
dict_32 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
    15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O',
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
    30: 'U', 31: 'V'
}
check = 0

# решил сделать отдельную функцию для работы со словарем
def character_symbol(symbol: str)-> str:

    """
    Преобразует символы в строке в их числовые эквиваленты согласно словарю dict_32.
    Если символ не найден в словаре, оставляет его без изменений.

    параметры:
        symbol (str): Входная строка для преобразования

    returns:
        str: Строка с замененными символами на их числовые представления
    """

    new_symbol = ''
    for sign in symbol:    
        for key, val in dict_32.items():
            if val == sign:
                new_symbol += str(key)
                break
        else:
            new_symbol += sign 
    return new_symbol

# Основная функция, в которую подаю "значение, то в каком счислении оно находится и то, в какое надо преобразовать"
def int_base(value: str, from_counting: int, in_counting: int):

    """
    Конвертирует число из одной системы счисления в другую (до 32-ричной).

    параметры:
        value (str): Число для конвертации
        from_counting (int): Исходная система счисления (2-32)
        in_counting (int): Целевая система счисления (2-32)

    returns:
        str | None: Преобразованное число в целевой системе счисления или None, если:
                   - исходная система < 11, но число содержит буквы
                   - некорректные параметры
    """




    global check  
    check = 0 
    for char in value:
        if char.isalpha():
            check += 1        
   
   
    if from_counting < 11 and check > 0:
        return None
    else:
        conversion_num_10 = in_10_number(value, from_counting)  
        return from_10_number(conversion_num_10, in_counting)

# Функция для перевода значений в десятичное исчисление
def in_10_number(value: str, from_counting: int):
    num_10 = 0
    long_str = len(value) 
    for i in range(long_str):
        symbol_to_num = int(value[long_str - 1 - i], from_counting)  
        num_10 += symbol_to_num * (from_counting ** i) 
    return num_10

# Функция пересчета значения из десятичного счисления в любое другое до 32-го счисления
def from_10_number(decimal_value: int, size: int):
    if decimal_value == 0:
        return "0"

    x_numerical_value = []
    while decimal_value > 0:
        remains = decimal_value % size
        x_numerical_value.append(dict_32[remains])  
        decimal_value //= size     
    return ''.join(reversed(x_numerical_value))
    
    
    
    
# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3G'
# >>> int_base('1010', 2, 30)
# 'A'
# >>>