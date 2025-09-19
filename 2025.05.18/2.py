# сложное но интересное задание
import decimal  # для денежных вычислений
from datetime import datetime, time, date  
from numbers import Number  # проверка типов

class PowerMeter:
    def __init__(self, 
                 tariff1: Number = decimal.Decimal('6.9'),  # первый тариф  
                 tariff2: Number = decimal.Decimal('3.9'),  # второй тариф 
                 tariff2_starts: time = time(23, 0),  # начало ночного тарифа 
                 tariff2_ends: time = time(7, 0)):   # конец ночного тарифа
        
        # проверка тарифов в decimal.Decimal 
        self.tariff1 = decimal.Decimal(str(tariff1))
        self.tariff2 = decimal.Decimal(str(tariff2))
        
        # сохраню  действия тарифов
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        
        # обьявляю суммарную  мощность
        self.power = decimal.Decimal('0')
        
        
        # словарь, ключом будет первое число месяца (дата), значение - сумма начислений
        self.charges = {}
    
    def __repr__(self) -> str:
        # машинное представление
        return f"<PowerMeter: {float(self.power)} кВт/ч>"
    
    def __str__(self) -> str:
        # человеческое представление 
        today = date.today()
        # ключ для текущего месяца, первое число месяца
        month_key = date(today.year, today.month, 1)
        
        # тут получится сумма начислений за текущий месяц
        current_charge = self.charges.get(month_key, decimal.Decimal('0'))
        
        # округлим до 2 знака до запятой
        rounded_charge = round(current_charge, 2)
        
        # попробуем сократить название месяцев
        month_name = today.strftime('%b')
        
        # применим шаблон (Month) charge
        return f"({month_name}) {float(rounded_charge)}"
    
    def meter(self, power: Number) -> decimal.Decimal:
        # текущее время
        now = datetime.now().time()
        
        # проверка например на второй тариф
        if (self.tariff2_starts <= self.tariff2_ends and 
            self.tariff2_starts <= now < self.tariff2_ends):
            # если тарифы не смешиваются
            rate = self.tariff2
        elif (self.tariff2_starts > self.tariff2_ends and 
              (now >= self.tariff2_starts or now < self.tariff2_ends)):
            # если тарифы смешиваются ну или пересекаются
            rate = self.tariff2
        else:
            # во всез других вариантах будет первый тариф
            rate = self.tariff1
        
        # переведем мощность в decimal.Decimal
        power_dec = decimal.Decimal(str(power))
        
        # рассчитываем стоимость
        cost = power_dec * rate
        
        # округляю копейки
        rounded_cost = round(cost, 2)
        
        # сложу сумаррную мощность
        self.power += power_dec
        
        # берем текущую дату
        today = date.today()
        # ключ для текущего месяца
        month_key = date(today.year, today.month, 1)
        
        
        # буду складывать стоимости, если они есть
        self.charges[month_key] = self.charges.get(month_key, decimal.Decimal('0')) + rounded_cost
        
        # стоиомть
        return rounded_cost

