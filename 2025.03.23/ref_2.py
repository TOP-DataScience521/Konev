n = int(input('введите количество чисел: '))

total = 0
for _ in range(n):
    num = int(input('введите число: '))
    if num > 0:
        total += num

print(total)

