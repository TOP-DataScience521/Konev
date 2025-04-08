print('Вам приветсвует система выявления счастливых билетов.')

ticket_number = str(input('Введите шестизначный номер вашего билета: №'))
ticket_number_1 = int(ticket_number[0:1])
ticket_number_2 = int(ticket_number[1:2])
ticket_number_3 =int(ticket_number[2:3])
ticket_number_4 =int(ticket_number[3:4])
ticket_number_5 =int(ticket_number[4:5])
ticket_number_6 =int(ticket_number[5:6])

ticket_number_123 = int(ticket_number_1 + ticket_number_2 + ticket_number_3) 
ticket_number_456 = int(ticket_number_4 + ticket_number_5 + ticket_number_6) 

if ticket_number_123 == ticket_number_456:
    print (f'ДА')
else:
    print (f'НЕТ')
    
    
# Вам приветсвует система выявления счастливых билетов.
# Введите шестизначный номер вашего билета: №123123
# ДА


# Вам приветсвует система выявления счастливых билетов.
# Введите шестизначный номер вашего билета: №123111
# НЕТ