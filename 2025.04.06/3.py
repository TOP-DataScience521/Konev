def countable_nouns(number: int, noun: tuple[str, str, str]):
    
       
    # Определение формы существительного в зависимости от числа
    if (number % 10 == 1) + (number % 100 != 11) == 2:
# год
        return noun[0]  
    elif (number % 10 in [2, 3, 4]) + (number % 100 not in [12, 13, 14]) == 2:
# года
        return noun[1]  
    else:
# лет        
        return noun[2]  
        
# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(37, ("год", "года", "лет"))
# 'лет'
# >>>
