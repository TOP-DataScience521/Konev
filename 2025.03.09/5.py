whole_value_miles = str(input('Введите целое число миль: '))
fractions_value_miles = str(input('Введите дробную часть миль: '))

MILI_IN_KM = 1.61

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше одного (см. тест ниже) — придумайте более универсальное решение
# ИСПРАВЛЕНО
combining_integers_fractions_str = whole_value_miles + '.' + fractions_value_miles
conversion_to_km = round(float(combining_integers_fractions_str) * MILI_IN_KM,1)

# ИСПРАВИТЬ: вывод не соответствует требуемому формату
# ИСПРАВЛЕНО
print(f'{combining_integers_fractions_str} миль = {conversion_to_km} ')


# Введите целое число миль: 254
# Введите дробную часть миль: 45
# 254.45 миль = 409.7 .


# ИТОГ: 2/5

