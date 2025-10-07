n = int(input('введите количество чисел: '))

first = second = 1
print(first, second, end=' ')

for _ in range(n - 2):
    temp = first
    first = second
    second = temp + second
    
    # альтернативный вариант, основанный на распаковке неявного кортежа:
    # first, second = second, first + second
    
    print(second, end=' ')

