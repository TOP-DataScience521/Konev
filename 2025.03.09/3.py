time_in_minutes = int(input('Введите целое число минут: '))

# ИСПРАВИТЬ: одинаковые операции в большинстве случаев имеет смысл выполнить заранее
# Не очень понял замечание, наверно ИСПРАВИЛ
time_in_hours = int(time_in_minutes) // 60
remaining_time_in_minutes = (time_in_minutes) - (time_in_hours) * 60

# ИСПРАВИТЬ: вывод не соответствует требуемому формату
# ИСПРАВЛЕНО
print(f'{time_in_minutes} минут - это {time_in_hours} час {remaining_time_in_minutes} минут ')


# Введите целое число минут: 120
# 120 минут - это  2 час 0 минут

# Введите целое число минут: 153
# 153 минут - это  2 час 33 минут


# ИТОГ: 1/3

