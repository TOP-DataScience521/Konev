
vvod_filov = input('Введите имена файлов, разделенные ";" и последующим пробелом ').strip()

spisok_vvoda_filov = vvod_filov.split('; ')

slovar_proverka_povtor_filov = {}

for file in spisok_vvoda_filov:
    if file in slovar_proverka_povtor_filov:
        slovar_proverka_povtor_filov[file] += 1
    else:
        slovar_proverka_povtor_filov[file] = 1


spisok_filov = []

for file in spisok_vvoda_filov:
    kolichestvo_failov = slovar_proverka_povtor_filov[file]
    
    if kolichestvo_failov == 1:
        spisok_filov.append(file)
    else:
        # Работаю со строками для новых имен
        if '.' in file:
            name_fail_bez_formata, format_faila = file.split('.', 1)
        else:
            name_fail_bez_formata, format_faila = file, ''
        novoe_name_faila = f"{name_fail_bez_formata}_{slovar_proverka_povtor_filov[file]}.{format_faila}" 
        if format_faila:
            novoe_name_faila = f"{name_fail_bez_formata}_{slovar_proverka_povtor_filov[file]}.{format_faila}"
        else:
            novoe_name_faila = f"{name_fail_bez_formata}_{slovar_proverka_povtor_filov[file]}"
            
        spisok_filov.append(novoe_name_faila)
        # Подбиваю индекс повторов
        slovar_proverka_povtor_filov[file] = slovar_proverka_povtor_filov[file] -1

spisok_filov.sort()

for file in spisok_filov:
    print(file)
    
    
    
#Введите имена файлов, разделенные ";" и последующим пробелом 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
#1.py
#1_2.py
#1_3.py
#aux.h
#functions.h
#main.cpp
#main_2.cpp
#main_3.cpp
#src.tar.gz
#src_2.tar.gz