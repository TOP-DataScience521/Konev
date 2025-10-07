ticket = input('введите номер билета: ')

left_sum = 0
right_sum = 0

for i in range(3):
    left_sum += int(ticket[i])

for i in range(3, 6):
    right_sum += int(ticket[i])

print('да' if left_sum == right_sum else 'нет')

