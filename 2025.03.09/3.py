vremia = input('Введите целое число минут затраченных на изготовление изделия ')

vremia_v_chasah = float(vremia) / 60
vremia_v_celih_chasah = int(vremia_v_chasah)
minut = float((vremia_v_chasah) - float(vremia_v_celih_chasah)) * 60

print(f'Деталь изготовлена за {vremia} минут.\nВ отчете будет указано время   {vremia_v_celih_chasah} часа и  {int(minut)} минут')


# Введите целое число минут затраченных на изготовление изделия 156
# Деталь изготовлена за 156 минут,
# В отчете будет указано время   2 часа и  36 минут

