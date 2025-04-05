print('Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности \nи сообщит Вам их количество.')
razrad_chisel = int(input('Введите любую разрядность: '))

max_chislo_str = str(9) * razrad_chisel
max_chislo_int = int(max_chislo_str)

min_chislo_str = str(9) * (razrad_chisel - 1)
min_chislo_int = int(min_chislo_str) + 1

spisok_vseh_chisel = list(range(min_chislo_int, max_chislo_int, 1))
kolichestvo_prostih_chisel = 0



for chislo_is_spiska in spisok_vseh_chisel:
    if chislo_is_spiska < 2:
        continue 
    priznak_prostogo_chisla = 1
    koren_chisla_is_spiska =(int(chislo_is_spiska ** (1/2)) +1)
    for vozmogni_delitel in range(2, koren_chisla_is_spiska, 1):
        if chislo_is_spiska % vozmogni_delitel == 0:
            priznak_prostogo_chisla = 0
            break
    if priznak_prostogo_chisla > 0:
        kolichestvo_prostih_chisel = kolichestvo_prostih_chisel + 1

print(f'Количество всех простых чисел в пределах Вашей разрядности: {kolichestvo_prostih_chisel}')



#Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности
#и сообщит Вам их количество.
#Введите любую разрядность: 3
#Количество всех простых чисел в пределах Вашей разрядности: 143

#Вам потребуется ввести количество разрядов числа,система определит все простые числа введенной разрядности
#и сообщит Вам их количество.
#Введите любую разрядность: 2
#Количество всех простых чисел в пределах Вашей разрядности: 21