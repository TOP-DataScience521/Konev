text = input('введите текст телеграммы: ')

spaces = 0
for ch in text:
    if ch == ' ':
        spaces += 1

total = (len(text) - spaces) * 30
rub = total // 100
kop = total % 100

print(f'{rub} руб. {kop} коп.')

