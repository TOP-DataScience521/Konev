
# очень крутая задача, много чего перепробовал пока не вычитал метод с корнями, спасибо

print ('Вам потребуется ввести положительное число, система определит все делители числа и сумирует их')

vvod_chisla = int(input('Введите любое целое положительное число: '))

koren_vvod_chisla = int(vvod_chisla ** (1/2)) + 1
spisok_chisel_dla_perebora  = list(range(2,koren_vvod_chisla,1)) 
spisok_deliteli_is_perebora = []
spisok_parni_deliteli = []
symma_delitelei = 0
kolichestvo_iteraci = 0

for chislo_is_perebora in spisok_chisel_dla_perebora :
    kolichestvo_iteraci = kolichestvo_iteraci + 1
    if vvod_chisla % chislo_is_perebora == 0:
        spisok_deliteli_is_perebora.append(chislo_is_perebora)
        parni_delitel = int(vvod_chisla / chislo_is_perebora)
        spisok_parni_deliteli.append(parni_delitel)
        
spisok_deliteli_is_perebora.extend(spisok_parni_deliteli)
print (f'вывод всех делителей кроеме 1 и {vvod_chisla}: {spisok_deliteli_is_perebora}')
symma_delitelei = sum(spisok_deliteli_is_perebora) + 1 + vvod_chisla
print (f'вывод суммы всех делителей: {symma_delitelei}')
print (f'количество произведенных итераций: {kolichestvo_iteraci}, это меньше чем количество итераций при прямом переборе на {vvod_chisla - kolichestvo_iteraci}')
        

#Вам потребуется ввести положительное число,
# система определит все делители числа и сумирует их
#Введите любое целое положительное число: 50
#вывод всех делителей кроеме 1 и 50: [2, 5, 25, 10]
#вывод суммы всех делителей: 93
#количество произведенных итераций: 6, это меньше чем количество итераций при прямом переборе на 44


#Вам потребуется ввести положительное число,
# система определит все делители числа и сумирует их
#Введите любое целое положительное число: 65482
#вывод всех делителей кроеме 1 и 65482: [2, 29, 58, 32741, 2258, 1129]
#вывод суммы всех делителей: 101700
#количество произведенных итераций: 254, это меньше чем количество итераций при прямом переборе на 65228

