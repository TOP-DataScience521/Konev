print('Вам приветсвует телеграфная служба.')

mail = str(input('Введите Ваше сообщение для расчета стоимости отправки: '))

long_mail = len(mail)
long_mail_not_space = len(mail.replace(" ",""))

total_cost = str(long_mail_not_space * 0.3)

cost_in_rubles = total_cost[:total_cost.find('.')]
cost_in_pennies = total_cost[total_cost.find('.')+1:total_cost.find('.')+3]

# Докрутил нехватающий ноль для копеек из одного числа
if len(cost_in_pennies) == 1:
    cost_in_pennies = cost_in_pennies + '0'
    


print (f'Стоимость отправки Вашего сообщения {cost_in_rubles} рублей  {cost_in_pennies} копеек.')

# Вам приветсвует телеграфная служба.
# Введите Ваше сообщение для расчета стоимости отправки: грузите апельсины бочках братья карамазовы
# Стоимость отправки Вашего сообщения 11 рублей  40 копеек.


# Вам приветсвует телеграфная служба.
# Введите Ваше сообщение для расчета стоимости отправки: через несколько дней я приеду
# Стоимость отправки Вашего сообщения 7 рублей  50 копеек.
