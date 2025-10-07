result = ''
while True:
    num = input('введите число: ')
    if int(num) % 7:
        break
    result = f'{num} ' + result

print(result)

