print ('Система проверяет корректность хода ладьи.')

otkuda_hod = input('Введите координаты положении ладьи: ')
kuda_hod = input ('Введите координаты предстоящего хода: ')

cifra_otkuda_hod = otkuda_hod[:1]
bukva_otkuda_hod = otkuda_hod [1:]

cifra_kuda_hod = kuda_hod[:1]
bukva_kuda_hod = kuda_hod [1:]

if ((cifra_otkuda_hod == cifra_kuda_hod) + (bukva_otkuda_hod == bukva_kuda_hod)) > 0:
    print ('Система считает Ваш ход ВОЗМОЖНЫМ')
else:
    print ('Система считает Ваш ход НЕ ВОЗМОЖНЫМ')



#Система проверяет корректность хода ладьи
#Введите координаты положении ладьи: h4
#Введите координаты предстоящего хода: b4
#Система считает Ваш ход ВОЗМОЖНЫМ


#Система проверяет корректность хода ладьи
#Введите координаты положении ладьи: g3
#Введите координаты предстоящего хода: g1
#Система считает Ваш ход ВОЗМОЖНЫМ


#Система проверяет корректность хода ладьи
#Введите координаты положении ладьи: b4
#Введите координаты предстоящего хода: d2
#Система считает Ваш ход НЕ ВОЗМОЖНЫМ