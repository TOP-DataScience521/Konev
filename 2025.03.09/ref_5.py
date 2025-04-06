miles_int = input('введите целую часть миль: ')
miles_frac = input('введите дробную часть миль: ')
miles = float(f'{miles_int}.{miles_frac}')

km = miles * 1.61
print(f'{miles} миль = {km:.1f} км')

