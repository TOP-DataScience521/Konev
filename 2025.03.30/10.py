
file_entry = input('Введите имена файлов, разделенные ";" и последующим пробелом ').strip()

file_entry_list = file_entry.split('; ')

repeat_files_dict = {}

for file in file_entry_list:
    if file in repeat_files_dict:
        repeat_files_dict[file] += 1
    else:
        repeat_files_dict[file] = 1


file_list = []

for file in file_entry_list:
    number_files = repeat_files_dict[file]
    
    if number_files == 1:
        file_list.append(file)
    else:
        # Работаю со строками для новых имен
        if '.' in file:
            file_name_without_format, new_name_files = file.split('.', 1)
        else:
            file_name_without_format, new_name_files = file, ''
        new_name_file = f"{file_name_without_format}_{repeat_files_dict[file]}.{new_name_files}" 
        if new_name_files:
            new_name_file = f"{file_name_without_format}_{repeat_files_dict[file]}.{new_name_files}"
        else:
            new_name_file = f"{file_name_without_format}_{repeat_files_dict[file]}"
            
        file_list.append(new_name_file)
        # Подбиваю индекс повторов
        repeat_files_dict[file] = repeat_files_dict[file] -1

file_list.sort()

for file in file_list:
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