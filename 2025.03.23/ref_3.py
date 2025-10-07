num = int(input('введите число: '))

# описание использованного алгоритма:
# https://younglinux.info/algorithm/divider

div_sum = num + 1
for div in range(2, int(num**0.5)+1):
    if not num % div:
        div_sum += div
        div_r = num / div
        if div != div_r:
            div_sum += int(div_r)

print(div_sum)

