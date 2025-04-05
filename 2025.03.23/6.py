print('Вам приветсвует система выявления счастливых билетов.')

nomer_bileta = str(input('Введите шестизначный номер вашего билета: №'))
cifra_bileta_1 = int(nomer_bileta[0:1])
cifra_bileta_2 = int(nomer_bileta[1:2])
cifra_bileta_3 =int(nomer_bileta[2:3])
cifra_bileta_4 =int(nomer_bileta[3:4])
cifra_bileta_5 =int(nomer_bileta[4:5])
cifra_bileta_6 =int(nomer_bileta[5:6])

cirra_bileta_123 = int(cifra_bileta_1 + cifra_bileta_2 + cifra_bileta_3) 
cirra_bileta_456 = int(cifra_bileta_4 + cifra_bileta_5 + cifra_bileta_6) 

if cirra_bileta_123 == cirra_bileta_456:
    print (f'Вам повезло, у Вас счастливый билет')
else:
    print (f'Упс, Ваш билет не счастливый')
    
    
