
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

obshee_mnogestvo_gorodov = {}

for gorod_slovar in cities:
    for goroda, info_o_gorode in gorod_slovar.items():
        if goroda not in obshee_mnogestvo_gorodov:
            obshee_mnogestvo_gorodov[goroda] = set()  
        obshee_mnogestvo_gorodov[goroda].add(info_o_gorode)  


for goroda, obchia_info_o_gorodah in obshee_mnogestvo_gorodov.items():
    print(f"'{goroda}': {obchia_info_o_gorodah}")



