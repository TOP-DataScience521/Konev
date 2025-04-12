high_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ಭಾರತ', '한국', 'ଭାରତ', 'ভাৰত', 'ভারত', 'ישראל', 'বাংলা', 'қаз', 'срб', 'бг', 'бел', 'சிங்கப்பூர்', 'мкд', 'ею', '中国', '中國', 'భారత్', 'ලංකා', 'ભારત', 'भारतम्', 'भारत', 'भारोत', 'укр', '香港', '台湾', '台灣', 'мон', 'الجزائر', 'عمان', 'ایران', 'امارات', 'موريتانيا', 'پاکستان', 'الاردن', 'بارت', 'بھارت', 'المغرب', 'البحرين', 'السعودية', 'ڀارت', 'سودان', 'عراق', 'مليسيا', '澳門', 'გე', 'ไทย', 'سورية', 'рф', 'تونس', 'ລາວ', 'ευ', 'ελ', 'ഭാരതം', 'ਭਾਰਤ', 'مصر', 'قطر', 'இலங்கை', 'இந்தியா', 'հայ', '新加坡', 'فلسطين', 'ye', 'yt', 'za', 'zm', 'zw']
email_address = str(input('Для регистрации в системе введите вашу электронную почту : '))

# чистка прихода, убераем регистры и пробелы, итоговая  

email_address = email_address.lower()
email_address = email_address.strip()

# Проверяем на наличие обязательных символов собаки 
if '@' in email_address:
    checking_dog_symbol = 1
else:
    checking_dog_symbol = 0
    
# Проверяем на наличие коректного домена высокого уровня
email_address_last_point = email_address.rfind(".")
domen = email_address[email_address_last_point+1:]

if domen in high_domains:
    checking_domen = 1
else:
    checking_domen = 0
    
# отделяем строку до @, итоговая
address_before_dog_symbol = email_address.split('@')[0]

# отделяем строку после @ и до домена
address_after_dog_symbol = email_address[email_address.rfind("@")+1:email_address.rfind('.')]

# Проверяем часть адреса до собаки на наличие разрешенных символов и знаков
number_of_letters = 0
number_of_digits = 0
number_dots_and_dashes = 0
for address_symbol in address_before_dog_symbol:
    if address_symbol.isalpha():
        number_of_letters = number_of_letters + 1
    else:
        number_of_letters = number_of_letters
    if address_symbol.isdigit():
        number_of_digits = number_of_digits + 1
    else:
        number_of_digits = number_of_digits
    if address_symbol in ['_','.']:
        number_dots_and_dashes = number_dots_and_dashes + 1
    else:
        number_dots_and_dashes = number_dots_and_dashes
    
allowed_characters = number_dots_and_dashes + number_of_digits + number_of_letters

if len(address_before_dog_symbol) == allowed_characters:
    ckecking_symbol_befor_dog = 1
else:
    ckecking_symbol_befor_dog = 0

# Проверяем часть адреса после собаки на наличие разрешенных символов и знаков до домена
mail_after_dog_befor_domen = email_address[(email_address.find("@")+1):email_address_last_point]

number_of_letters = 0
number_of_digits = 0
number_dots_and_dashes = 0

for address_symbol in mail_after_dog_befor_domen:
    if address_symbol.isalpha():
        number_of_letters = number_of_letters + 1
    else:
        number_of_letters = number_of_letters
    if address_symbol.isdigit():
        number_of_digits = number_of_digits + 1
    else:
        number_of_digits = number_of_digits
    if address_symbol in ['_','.']:
        number_dots_and_dashes = number_dots_and_dashes + 1
    else:
        number_dots_and_dashes = number_dots_and_dashes
    
allowed_characters = number_dots_and_dashes + number_of_digits + number_of_letters
if len(mail_after_dog_befor_domen) == allowed_characters:
    ckecking_symbol_after_dog = 1
else:
    ckecking_symbol_after_dog = 0
    
# Итоговый вывод
if (checking_dog_symbol + checking_domen + ckecking_symbol_befor_dog + ckecking_symbol_after_dog) == 4:
    print(f'Введенный электронный адрес успешно ПРИНЯТ (ДА) системой.')
else:
    print(f'Введенный электронный адрес НЕ ПРИНЯТ (НЕТ) системой.')
if checking_dog_symbol == 0:
    print(f'Возможно Вы пропустили символ @.')
else:
    ...
if checking_domen == 0:
    print(f'Возможно Вами указан не существующий домен почтовой службы.')
else:
    ...
if ckecking_symbol_befor_dog == 0:
    print(f'Возможно Вы ввели недопустимые символы в первой части адреса (до @).')
else:
    ...    
if ckecking_symbol_after_dog == 0:
    print(f'Возможно Вы ввели недопустимые символы во второй части адреса (после @).')
else:
    ...    
 

#Для регистрации в системе введите вашу электронную почту : nich90@mail.ru
#Введенный электронный адрес успешно ПРИНЯТ (ДА) системой.


#Для регистрации в системе введите вашу электронную почту : nkonev@vnov.acron.ru
#Введенный электронный адрес успешно ПРИНЯТ (ДА) системой.


#Для регистрации в системе введите вашу электронную почту : ghd//dhg@fj.er.ru
#Введенный электронный адрес НЕ ПРИНЯТ (НЕТ) системой.
#Возможно Вы ввели недопустимые символы в первой части адреса (до @).


#Для регистрации в системе введите вашу электронную почту : nich/90@mail//ru
#Введенный электронный адрес НЕ ПРИНЯТ (НЕТ) системой.
#Возможно Вами указан не существующий домен почтовой службы.
#Возможно Вы ввели недопустимые символы в первой части адреса (до @).
#Возможно Вы ввели недопустимые символы во второй части адреса (после @). 

#Для регистрации в системе введите вашу электронную почту : defhgrtrthrth.ru
#Введенный электронный адрес НЕ ПРИНЯТ (НЕТ) системой.
#Возможно Вы пропустили символ @.

