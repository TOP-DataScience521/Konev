print ('Система определить может ли введенная Вами строка являться двоичным значением.')
kod = input('Введите строку с предполагаемым двоичным значением: ')

kod_index_1 = kod[:1]
kod_index_2 = kod[:2]
kod_index_ot_2_do_konca = kod[2:]

proverka_index1i2_koda_na_b_ob = 0
proverka_index_koda_1i2_na_dvoichnost = 0
proverka_index_koda_ot2do_konec_na_dvoichnost = 0
proverka_polnogo_koda_na_dvoichnost = 0

dvoichnie_simvol = {'0','1'}
kod_index_ot_2_do_konca_set = set(kod_index_ot_2_do_konca)
kod_index_2_set = set(kod_index_2)

if (('b' == kod_index_1) + ('0b' == kod_index_2)) > 0:
    proverka_index1i2_koda_na_b_ob = 1
else:
    if 1 == kod_index_2_set.issubset(dvoichnie_simvol):
        proverka_index_koda_1i2_na_dvoichnost = 1

if 1 == kod_index_ot_2_do_konca_set.issubset(dvoichnie_simvol):
    proverka_index_koda_ot2do_konec_na_dvoichnost = 1

if ((proverka_index1i2_koda_na_b_ob + proverka_index_koda_1i2_na_dvoichnost) + proverka_index_koda_ot2do_konec_na_dvoichnost) > 1:
    proverka_polnogo_koda_na_dvoichnost = 1
    print (f'Введенная Вами строка ЯВЛЯЕТСЯ двоичным значением')  
else:
    print (f'Введенная Вами строка НЕ ЯВЛЯЕТСЯ двоичным значением')    



