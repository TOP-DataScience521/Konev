print ('Для сосотавления списка покупок для фруктовой корзины, \nВам будет необходимо ввести список покупок.')

empty_input = 0
all_fruits = []
number_frukt = 0
# прекращаем запросы после ввода пустой строки
while empty_input == 0:
    frukt = str(input('Введите фрукт : '))
    number_frukt = number_frukt + 1
    if frukt == "":
        empty_input = 1
    else:
        empty_input = 0
    all_fruits.append(frukt) 
    
# ввод "и" перед последним фруктом
all_fruits_str = ','.join(all_fruits)
index_last_comma = all_fruits_str.rfind(",")
all_fruits_str_mod = all_fruits_str[:index_last_comma]
index_penultimate_comma = all_fruits_str_mod.rfind(",")
all_fruits_str_mod = all_fruits_str_mod[:index_penultimate_comma] + ' и ' + all_fruits_str_mod[index_penultimate_comma+1:]

if number_frukt == 2:
    one_fruit = ''.join(all_fruits)
    print (f'Итоговый список покупок: {one_fruit}') 
else:
    print (f'Итоговый список покупок: {all_fruits_str_mod}') 


    
 

#Для сосотавления списка покупок для фруктовой корзины,
#Вам будет необходимо ввести список покупок.
#Введите фрукт : апельсин
#Введите фрукт : лимон
#Введите фрукт : ананас
#Введите фрукт : яблоко
#Введите фрукт :
#Итоговый список покупок: апельсин,лимон,ананас и яблоко