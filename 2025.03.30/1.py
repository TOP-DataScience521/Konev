high_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ಭಾರತ', '한국', 'ଭାରତ', 'ভাৰত', 'ভারত', 'ישראל', 'বাংলা', 'қаз', 'срб', 'бг', 'бел', 'சிங்கப்பூர்', 'мкд', 'ею', '中国', '中國', 'భారత్', 'ලංකා', 'ભારત', 'भारतम्', 'भारत', 'भारोत', 'укр', '香港', '台湾', '台灣', 'мон', 'الجزائر', 'عمان', 'ایران', 'امارات', 'موريتانيا', 'پاکستان', 'الاردن', 'بارت', 'بھارت', 'المغرب', 'البحرين', 'السعودية', 'ڀارت', 'سودان', 'عراق', 'مليسيا', '澳門', 'გე', 'ไทย', 'سورية', 'рф', 'تونس', 'ລາວ', 'ευ', 'ελ', 'ഭാരതം', 'ਭਾਰਤ', 'مصر', 'قطر', 'இலங்கை', 'இந்தியா', 'հայ', '新加坡', 'فلسطين', 'ye', 'yt', 'za', 'zm', 'zw']
adres_pochti = str(input('Для регистрации в системе введите вашу электронную почту : '))

# чистка прихода, убераем регистры и пробелы, итоговая  

adres_pochti = adres_pochti.lower()
adres_pochti = adres_pochti.strip()

# Проверяем на наличие обязательных символов собаки 
if '@' in adres_pochti:
    proverka_sobaka = 1
else:
    proverka_sobaka = 0
    
# Проверяем на наличие коректного домена высокого уровня
poslednia_tocka_adresa = adres_pochti.rfind(".")
domen = adres_pochti[poslednia_tocka_adresa+1:]

if domen in high_domains:
    proverka_domena = 1
else:
    proverka_domena = 0
    
# отделяем строку до @, итоговая
adres_do_sobaki = adres_pochti.split('@')[0]

# отделяем строку после @ и до домена
adres_posle_sobaki = adres_pochti[adres_pochti.rfind("@")+1:adres_pochti.rfind('.')]

# Проверяем часть адреса до собаки на наличие разрешенных символов и знаков
kolichestvo_bukv = 0
kolichestvo_cifr = 0
kolichestvo_tochka_tire = 0
for simvol_adresa in adres_do_sobaki:
    if simvol_adresa.isalpha():
        kolichestvo_bukv = kolichestvo_bukv + 1
    else:
        kolichestvo_bukv = kolichestvo_bukv
    if simvol_adresa.isdigit():
        kolichestvo_cifr = kolichestvo_cifr + 1
    else:
        kolichestvo_cifr = kolichestvo_cifr
    if simvol_adresa in ['_','.']:
        kolichestvo_tochka_tire = kolichestvo_tochka_tire + 1
    else:
        kolichestvo_tochka_tire = kolichestvo_tochka_tire
    
razrechonie_simvoli = kolichestvo_tochka_tire + kolichestvo_cifr + kolichestvo_bukv

if len(adres_do_sobaki) == razrechonie_simvoli:
    proverka_razrechonie_simvoli_do_sobaki = 1
else:
    proverka_razrechonie_simvoli_do_sobaki = 0

# Проверяем часть адреса после собаки на наличие разрешенных символов и знаков до домена
adresposledodomen = adres_pochti[(adres_pochti.find("@")+1):poslednia_tocka_adresa]

kolichestvo_bukv = 0
kolichestvo_cifr = 0
kolichestvo_tochka_tire = 0

for simvol_adresa in adresposledodomen:
    if simvol_adresa.isalpha():
        kolichestvo_bukv = kolichestvo_bukv + 1
    else:
        kolichestvo_bukv = kolichestvo_bukv
    if simvol_adresa.isdigit():
        kolichestvo_cifr = kolichestvo_cifr + 1
    else:
        kolichestvo_cifr = kolichestvo_cifr
    if simvol_adresa in ['_','.']:
        kolichestvo_tochka_tire = kolichestvo_tochka_tire + 1
    else:
        kolichestvo_tochka_tire = kolichestvo_tochka_tire
    
razrechonie_simvoli = kolichestvo_tochka_tire + kolichestvo_cifr + kolichestvo_bukv
if len(adresposledodomen) == razrechonie_simvoli:
    proverka_razrechonie_simvoli_posle_sobaki = 1
else:
    proverka_razrechonie_simvoli_posle_sobaki = 0
    
# Итоговый вывод
if (proverka_sobaka + proverka_domena + proverka_razrechonie_simvoli_do_sobaki + proverka_razrechonie_simvoli_posle_sobaki) == 4:
    print(f'Введенный электронный адрес успешно ПРИНЯТ системой.')
else:
    print(f'Введенный электронный адрес НЕ ПРИНЯТ системой.')
if proverka_sobaka == 0:
    print(f'Возможно Вы пропустили символ @.')
else:
    ...
if proverka_domena == 0:
    print(f'Возможно Вами указан не существующий домен почтовой службы.')
else:
    ...
if proverka_razrechonie_simvoli_do_sobaki == 0:
    print(f'Возможно Вы ввели недопустимые символы в первой части адреса (до @).')
else:
    ...    
if proverka_razrechonie_simvoli_posle_sobaki == 0:
    print(f'Возможно Вы ввели недопустимые символы во второй части адреса (после @).')
else:
    ...    
 

#Для регистрации в системе введите вашу электронную почту : nich90@mail.ru
#Введенный электронный адрес успешно ПРИНЯТ системой.


#Для регистрации в системе введите вашу электронную почту : nkonev@vnov.acron.ru
#Введенный электронный адрес успешно ПРИНЯТ системой.


#Для регистрации в системе введите вашу электронную почту : ghd//dhg@fj.er.ru
#Введенный электронный адрес НЕ ПРИНЯТ системой.
#Возможно Вы ввели недопустимые символы в первой части адреса (до @).


#Для регистрации в системе введите вашу электронную почту : nich/90@mail//ru
#Введенный электронный адрес НЕ ПРИНЯТ системой.
#Возможно Вами указан не существующий домен почтовой службы.
#Возможно Вы ввели недопустимые символы в первой части адреса (до @).
#Возможно Вы ввели недопустимые символы во второй части адреса (после @). 

#Для регистрации в системе введите вашу электронную почту : defhgrtrthrth.ru
#Введенный электронный адрес НЕ ПРИНЯТ системой.
#Возможно Вы пропустили символ @.

