n = int(input('введите количество разрядов: '))
left = 10**(n-1)
right = 10**n

cnt = 0
for num in range(left, right):
    for div in range(2, int(num**0.5)+1):
        if not num % div:
            break
    else:
        cnt += 1

print(cnt)

