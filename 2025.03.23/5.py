print('Вам приветсвует телеграфная служба.')

soobchenie = str(input('Введите Ваше сообщение для расчета стоимости отправки: '))

dlinna_soobchenia = len(soobchenie)
soobchenie_bez_probelov = soobchenie.replace(" ","")
dlinna_soobchenia_bez_probel = len(soobchenie_bez_probelov)

obchia_stoimost_otpravki = dlinna_soobchenia_bez_probel * 0.3

stoimost_tolko_rubli = int(obchia_stoimost_otpravki)
stoimost_tolko_kopeiki = int((obchia_stoimost_otpravki - stoimost_tolko_rubli)*100)
stoimost_tolko_kopeiki = str(stoimost_tolko_kopeiki)[:2]

print (f'Стоимость отправки Вашего сообщения {stoimost_tolko_rubli} рублей  {stoimost_tolko_kopeiki} копеек.')

#Вам приветсвует телеграфная служба.
#Введите Ваше сообщение для расчета стоимости отправки: через несколько дней я приеду
#Стоимость отправки Вашего сообщения 7 рублей  50 копеек.
