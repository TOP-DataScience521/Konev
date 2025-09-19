# ради практики поработаем с математической библиотекой
import math

#  класс Tetrahedron 
class Tetrahedron:
    #  __init__ как конструктор
    def __init__(self, edge):
        # смотрю положительна ли длинна ребра
        if edge <= 0:
            raise ValueError("длина ребра должна быть больше 0")
        
        # сохраню  значение ребра в атрибут self.edge
        self.edge = float(edge)  # float для чистоты эксперемента
    
    # вариант расчета площади
    def surface(self) -> float:
        surface_area = math.sqrt(3) * (self.edge ** 2)
        return surface_area
    
    # вариант расчета обьема
    def volume(self) -> float:
        volume_value = (self.edge ** 3) * math.sqrt(2) / 12
        return volume_value


# C:\Users\Admin\Konev\2025.05.18>python -i 1.py
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 12
# >>> t1.surface()
# 249.4153162899183
# >>>