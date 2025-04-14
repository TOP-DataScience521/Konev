def central_tendency(num_1: float, num_2: float,/, *num_x: float):
      
    numbers_list = [num_1, num_2] + list(num_x)
    
    numbers_list.sort()
    long_numbers_list = len(numbers_list)

# считаем медиану
    if long_numbers_list % 2 == 0:
        median = (numbers_list[long_numbers_list // 2 - 1] + numbers_list[long_numbers_list // 2]) / 2
    else:
        median = numbers_list[long_numbers_list // 2]
        
# считаем среднее арифметическое
    arithmetic = sum(numbers_list) / len(numbers_list)
# считаем среднее геометрическое
    for number in numbers_list:
        multiplication_numbers *= number
        geometric = multiplication_numbers ** (1/long_numbers_list)
# считаем среднее гармоническое
    for number_1 in numbers_list:
        sum_numbers_divided_on_1 += 1/number
        harmonic = sum_numbers_divided_on_1 /long_numbers_list
    return print ({'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781})


       
def central_tendency(num_1: float, num_2: float, /, *num_x: float) -> dict[str, float]:
    
    numbers_list = [num_1, num_2] + list(num_x)
    
    numbers_list.sort()
    long_numbers_list = len(numbers_list)

    if long_numbers_list % 2 == 0:
        median = (numbers_list[long_numbers_list // 2 - 1] + numbers_list[long_numbers_list // 2]) / 2
    else:
        median = numbers_list[long_numbers_list // 2]
        
    arithmetic = sum(numbers_list) / long_numbers_list

    multiplication_numbers = 1.0
    for number in numbers_list:
        multiplication_numbers *= number
    geometric = multiplication_numbers ** (1 / long_numbers_list)

    sum_numbers_divided_on_1 = 0.0
    for number in numbers_list:
        sum_numbers_divided_on_1 += 1 / number
    harmonic = long_numbers_list / sum_numbers_divided_on_1

    return {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }

# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
# >>> sample1 = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample1)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
# >>>