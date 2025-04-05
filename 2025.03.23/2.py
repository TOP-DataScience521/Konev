print ('Вам необходимо ввести список значений, положительные из них будут сумированны')

kolichestvo_znacheni = int(input('Введите количество значений которые планируете перечислить: '))

nomer_popitok = 0
symma_polozitelnih_chesil = 0

while nomer_popitok < kolichestvo_znacheni:
    ostalos_popitok = int(input (f'введите значение, осталось {kolichestvo_znacheni-nomer_popitok} значений:  '))
    nomer_popitok = nomer_popitok + 1
    if ostalos_popitok > 0:
        symma_polozitelnih_chesil = symma_polozitelnih_chesil + ostalos_popitok
    else:
        symma_polozitelnih_chesil = symma_polozitelnih_chesil  
        
print (f'Сумма введенных Вами положительных чисел: {symma_polozitelnih_chesil}')
        
        
#Вам необходимо ввести список значений, положительные из них будут сумированны
#Введите количество значений которые планируете перечислить: 6
#введите значение, осталось 6 значений:  -3
#введите значение, осталось 5 значений:  3
#введите значение, осталось 4 значений:  -2
#введите значение, осталось 3 значений:  2
#введите значение, осталось 2 значений:  -18
#введите значение, осталось 1 значений:  18
#Сумма введенных Вами положительных чисел: 23