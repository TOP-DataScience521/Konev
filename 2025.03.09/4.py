chislo = input('Для выполнения математических операций введите положительное трехзначное число: ')

cifra_1_chisla = int(chislo) // 100
cifra_2_chisla = int(int(chislo) / 10 - cifra_1_chisla * 10)
cifra_3_chisla = (int(chislo) - cifra_1_chisla * 100 - cifra_2_chisla * 10)

summa_cifr_chisla = cifra_1_chisla + cifra_2_chisla + cifra_3_chisla
proizvedenie_cifr_chisla = cifra_1_chisla * cifra_2_chisla * cifra_3_chisla

print (f'Первая цифра: {cifra_1_chisla}')
print (f'Вторая цифра: {cifra_2_chisla}')
print (f'Третья цифра: {cifra_3_chisla}')
print (f'Сумма цифр числа {chislo} равна {summa_cifr_chisla}.\nПроизведение цифр равно {proizvedenie_cifr_chisla} ')

#Для выполнения математических операций введите положительное трехзначное число: 456
#Первая цифра: 4
#Вторая цифра: 5
#Третья цифра: 6
#Сумма цифр числа 456 равна 15.
#Произведение цифр равно 120