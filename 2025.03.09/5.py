probeg_mili_celyi = int(input('В целях приведения пробега автомобиля к российским стандартам \nвведите целое значение пройденных миль: '))
probeg_mili_desiatie = int(input('Спасибо, теперь введите первую цифру пробега после запятой: '))

MILI_KM = 1.61

probeg_km_polnyi = probeg_mili_celyi * MILI_KM + int(probeg_mili_desiatie) / 10 * MILI_KM
probeg_km_okruglen = round(probeg_km_polnyi,1)

print (f'Ваш текущий пробег {probeg_mili_celyi}.{probeg_mili_desiatie} миль был стандартизирован в пробег {probeg_km_okruglen} км.')

#В целях приведения пробега автомобиля к российским стандартам
#введите целое значение пройденных миль: 151
#Спасибо, теперь введите первую цифру пробега после запятой: 9
#Ваш текущий пробег 151.9 миль был стандартизирован в пробег 244.6 км.