
cities = [
    {
        'Барнаул': 2,
        'Ижевск': 4,
        'Иркутск': 5,
        'Казань': 4,
        'Новокузнецк': 5,
        'Пермь': 1,
        'Уфа': 5,
        'Хабаровск': 5,
        'Ярославль': 5
    },
    {
        'Барнаул': 2,
        'Воронеж': 3,
        'Иркутск': 6,
        'Казань': 1,
        'Оренбург': 6,
        'Тюмень': 5
    },
    {
        'Казань': 2,
        'Краснодар': 6,
        'Красноярск': 7,
        'Новосибирск': 1,
        'Пермь': 5,
        'Уфа': 3
    },
    {
        'Владивосток': 5,
        'Екатеринбург': 2,
        'Краснодар': 1,
        'Москва': 4,
        'Новосибирск': 6,
        'Самара': 4,
        'Тольятти': 7,
        'Тюмень': 5,
        'Ярославль': 5
    }
]

total_set_city = {}

for dictionary_city in cities:
    for cities, info_city in dictionary_city.items():
        if cities not in total_set_city:
            total_set_city[cities] = set()  
        total_set_city[cities].add(info_city)  


for cities, total_info_cities in total_set_city.items():
    print(f"'{cities}': {total_info_cities}")



