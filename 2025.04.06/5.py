def orth_triangle(cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:


    """
    Функция принимает в качестве аргументов длины двух сторон: это могут быть два катета или один из катетов и гипотенуза.

    параметры:
        cathetus1 (float): Длина первого катета. По умолчанию 0.
        cathetus2 (float): Длина второго катета. По умолчанию 0.
        hypotenuse (float): Длина гипотенузы. По умолчанию 0.

    returns:
        float | None: Длина недостающей стороны треугольника или None, если:
                     - передано более двух сторон
                     - не передано ни одной стороны
                     - переданные стороны не образуют прямоугольный треугольник
                     - гипотенуза меньше катета 
    """



   
    if (cathetus1 > 0) + (cathetus2 > 0) + (hypotenuse > 0) > 2:
        return None

    # Проверка на отсутствие переданных сторон
    if (cathetus1 == 0) + (cathetus2 == 0) + (hypotenuse == 0) == 3:
        return None

    # Расчет гипотенузы по двум катетам
    if (cathetus1 > 0) and (cathetus2 > 0):
        return (cathetus1 ** 2 + cathetus2 ** 2) ** (1/2)

    # Расчет второго катета по первому катету и гипотенузе
    if (cathetus1 > 0) and (hypotenuse > 0):
        if hypotenuse < cathetus1:
            return None
        return (hypotenuse ** 2 - cathetus1 ** 2) ** (1/2)

    # Расчет первого катета по второму катету и гипотенузе
    if (cathetus2 > 0) and (hypotenuse > 0):
        if hypotenuse < cathetus2:
            return None
        return (hypotenuse ** 2 - cathetus2 ** 2) ** (1/2)
        
        
        
        
 # >>> orth_triangle(cathetus1=3, hypotenuse=5)
 # 4.0
 # >>> orth_triangle(cathetus1=8, cathetus2=15)
 # 17.0
 # >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
 # None
 # >>> orth_triangle(cathetus1=3, cathetus2=19)
 # 19.235384061671343
 # >>>