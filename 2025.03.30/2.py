print ('Для сосотавления списка покупок для фруктовой корзины, \nВам будет необходимо ввести список покупок.')

pustoi_vvod = 0
vsefrukt = []
nomer_frukta = 0
# прекращаем запросы после ввода пустой строки
while pustoi_vvod == 0:
    frukt = str(input('Введите фрукт : '))
    nomer_frukta = nomer_frukta + 1
    if frukt == "":
        pustoi_vvod = 1
    else:
        pustoi_vvod = 0
    vsefrukt.append(frukt) 
    
# ввод "и" перед последним фруктом
vse_frukt_str = ','.join(vsefrukt)
index_posledne_zapiatoi = vse_frukt_str.rfind(",")
vse_frukt_str_mod = vse_frukt_str[:index_posledne_zapiatoi]
index_predposledne_zapiatoi = vse_frukt_str_mod.rfind(",")
vse_frukt_str_mod = vse_frukt_str_mod[:index_predposledne_zapiatoi] + ' и ' + vse_frukt_str_mod[index_predposledne_zapiatoi+1:]

if nomer_frukta == 2:
    odin_frukt = ''.join(vsefrukt)
    print (f'Итоговый список покупок: {odin_frukt}') 
else:
    print (f'Итоговый список покупок: {vse_frukt_str_mod}') 


    
 

#Для сосотавления списка покупок для фруктовой корзины,
#Вам будет необходимо ввести список покупок.
#Введите фрукт : апельсин
#Введите фрукт : лимон
#Введите фрукт : ананас
#Введите фрукт : яблоко
#Введите фрукт :
#Итоговый список покупок: апельсин,лимон,ананас и яблоко