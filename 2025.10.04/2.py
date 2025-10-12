from numpy import array, corrcoef, cov, linspace
from matplotlib import pyplot as plt
from pathlib import Path
from sys import path
import datetime


# читаю csv файл и преобразую в словарь
def read_time_series_data(filename):
   
    file_path = Path(path[0]) / filename
    text = file_path.read_text(encoding='utf-8')
    lines = text.split('\n')
    
    monthly_data = {}
    
    for row in lines:
        if row.strip() and not row.startswith('#'):
            parts = row.split()
            if len(parts) == 2:
                date_str, value_str = parts
                year, month = parse_date_to_year_month(date_str)
                monthly_data[(year, month)] = float(value_str)
    
    return monthly_data

# вообщем я решил что конкретные числовые даты из csv файлов не имеют большого значения, я поставил задачу парсинга в год,месяц
def parse_date_to_year_month(date_str):
    # разобью даты между точек на сосотавляющте 
    day, shortened_month, year_str = date_str.split('.')
    # словарь для преобразования сокращений месяцев в числовые обозначения
    month_map = {
        'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'июн': 6,
        'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12
    }
    # само преобразование месяцев в числовые обозначения
    month = month_map[shortened_month]
    
    # долго не думая, решил года преобразовать в стандартный вид и просто добавил в начало 20
    full_year_str = "20" + year_str
    year = int(full_year_str)
    
    return year, month


# на этот раз  подготовлю функцию где буду определять пересекающиеся периоды по нефти и газу
def analyze_data_periods(oil_data, diesel_data):
    # без сортировки скорее всего возникнут проблемы, так что на этот раз отсортирую данные
    oil_months = sorted(oil_data.keys())
    diesel_months = sorted(diesel_data.keys())
    
    
    #print(f"нефть с {oil_months[0]} по {oil_months[-1]} ({len(oil_months)} месяцев)")
    #print(f"дизель с {diesel_months[0]} по {diesel_months[-1]} ({len(diesel_months)} месяцев)")
    # вроде все правельно
    
    # нахожу пересекающийся период
    common_start = max(oil_months[0], diesel_months[0])
    common_end = min(oil_months[-1], diesel_months[-1])
    
    #print(f"gересекающийся период с {common_start} по {common_end}")
    
    
    # буду возвращать кортежи с началом и концом пересекающимся периодом
    return common_start, common_end


# функция для сопоставленных рядов со сдвигами
# dataset1 - первый набор данных
# dataset2 - второй набор данных
# shift_months - сдвиг по месяцам

def create_aligned_series_monthly(dataset1, dataset2, shift_months):
  
    
    # заготавливаю пустые списки
    aligned_values1 = []
    aligned_values2 = []
    
    # перебираю все месяцы из первого набора
    for (year1, month1), value1 in dataset1.items():
        # выявляю целевой месяц со сдвигом
        total_months = month1 + shift_months
        # определяю сколько полных лет
        target_year = year1 + (total_months - 1) // 12
        target_month = (total_months - 1) % 12 + 1
        # это будет ключ для поиска во втором наборе данных
        target_key = (target_year, target_month)
        
        # проверяем сопоставление месяцев
        if target_key in dataset2:
            aligned_values1.append(value1)
            aligned_values2.append(dataset2[target_key])
    
    # возращаем сопоставленные массивы цен на нефть и дизель
    return array(aligned_values1), array(aligned_values2)


# буду расчитывать корреляцю и регрессию
def calculate_correlation_and_regression(series1, series2):
    # тут будет расчет кореляции через индексы матриц
    
    
    correlation = corrcoef(series1, series2)[0, 1]
    
    # считаю регрессию вида  y = a + b*x 
    cov_xy = cov(series1, series2, ddof=1)[0, 1]
    var_x = series1.var(ddof=1)
    
    if var_x > 0:
        b = cov_xy / var_x
        a = series2.mean() - b * series1.mean()
    else:
        a, b = 0, 0
    
    return correlation, a, b


# теперь использую проверенную функцию корреляции со сдвигом
def analyze_temporal_correlations():
   
    # непосредственно используем функцию чтения csv файлов
    oil_data = read_time_series_data('urals_oil_rus_export_prices.csv')
    diesel_data = read_time_series_data('dizel_fuel_rus_prices.csv')
    
    #print("проверка")
   
    
    # запускаю функцию по пересекающимся периодам
    common_start, common_end = analyze_data_periods(oil_data, diesel_data)
    
    # цикл с выводом вариационных рядов и сдвигов, пока сдвиги меняю прям в коде
    for shift_months in range(-3, 4):
        oil_aligned, diesel_aligned = create_aligned_series_monthly(
            oil_data, diesel_data, shift_months
        )
        
        # получаю полные данные с датами для вывода
        oil_dates, oil_values, diesel_dates, diesel_values = create_aligned_series_with_dates(
            oil_data, diesel_data, shift_months
        )
        
        
        if oil_aligned is not None and len(oil_aligned) > 0:
            correlation, a, b = calculate_correlation_and_regression(oil_aligned, diesel_aligned)
            
            # вывод в консоль 
            print("-" * 60)
                    
            print("Вариационные ряды:\n")
            
            # Полный вариационный ряд для нефти с годами и месяцами - ГОРИЗОНТАЛЬНО
            print("По нефти")
            oil_str = ""
            for date, price in zip(oil_dates, oil_values):
                year, month = date
                oil_str += f"({year}-{month:02d}: {price:5.2f}) "
            print(oil_str)
            
            # Полный вариационный ряд для дизеля с годами и месяцами - ГОРИЗОНТАЛЬНО
            print("по дизелю")
            diesel_str = ""
            for date, price in zip(diesel_dates, diesel_values):
                year, month = date
                diesel_str += f"({year}-{month:02d}: {price:5.2f}) "
            print(diesel_str)
            print(f"сдвиг {shift_months:3d} месяцев") 
            print(f"коэффициент корреляции равен {correlation:.4f}")

# тут я кое что не продумал, поэтому придется городить огород из похожих функций
# эта функция будет для вывода в более менее нужном мне фолрмате
def create_aligned_series_with_dates(dataset1, dataset2, shift_months):
  
    
    oil_dates = []
    oil_values = []
    diesel_dates = []
    diesel_values = []
    
    # перебераю все месяцы из первого набора
    for (year1, month1), value1 in dataset1.items():
        # вычисляю нужный месяц
        total_months = month1 + shift_months
        target_year = year1 + (total_months - 1) // 12
        target_month = (total_months - 1) % 12 + 1
        target_key = (target_year, target_month)
        
        # проверяю сопоставление месяцев
        if target_key in dataset2:
            oil_dates.append((year1, month1))
            oil_values.append(value1)
            diesel_dates.append(target_key)
            diesel_values.append(dataset2[target_key])
    
    return oil_dates, oil_values, diesel_dates, diesel_values


# пришлось еще много раз пересмотреть corr1.py строю график корреляции и регресии
# oil_prices - массив цен на нефть
# diesel_prices - массив цен на дизель
# a и b - из уравнения регрессии (y = a + b*x)
# shift_months - временной сдвиг в месяцах
# correlation - коэффициент корреляции
#
def plot_correlation_and_regression(oil_prices, diesel_prices, a, b, shift_months, correlation):
    # пока оставлю такой размер графика и разрешение точек
    fig = plt.figure(figsize=(12, 8), dpi=150)
    # общая система координат
    axs = fig.subplots()
    
    # так, oil_prices пойдет по оси х , diesel_prices по у, s - размер точек 
    axs.scatter(oil_prices, diesel_prices, s=50, 
               label=f'Сопоставленные данные')
    
    # тут будет линия регресии
    # минимальные максимальные цены нефть 
    x_min, x_max = oil_prices.min(), oil_prices.max()
    x_regr = linspace(x_min, x_max, 20)
    y_regr = a + b * x_regr
    
    # координаты линии и ее толщина и подпись смразу с самим уровнением
    axs.plot(x_regr, y_regr, 'r-', linewidth=3, 
             label=f'y = {a:.2f} + {b:.3f}·x')
    
    # настроим график
    axs.set_xlabel('цена нефти ')
    axs.set_ylabel('цена дизеля')
    axs.set_title(f'корреляция нефти по дизелю (сдвиг: {shift_months} мес.)\n' +
                  f'коэффициент корреляции r = {correlation:.4f}')
    
    # включим сетку, с ней удобнее
    axs.grid(True, alpha=0.3)
    axs.legend()
    
    # сохраняю график
    filename = f'2_{shift_months}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"график получилось сохранить '{filename}'")
    #plt.show()

#  головная функция
def main():
    
    #print("проверка1")
    
    # Сначала проанализируем какие данные у нас есть
    oil_data = read_time_series_data('urals_oil_rus_export_prices.csv')
    diesel_data = read_time_series_data('dizel_fuel_rus_prices.csv')
    
    #print("проверка2")
    #print("нефть", sorted(oil_data.keys()))
    #print("дизель", sorted(diesel_data.keys()))
    
    # запускаем анализ для вывода всех сдвигов
    analyze_temporal_correlations()
    
    # тут уже просто не хватило времени(( поэтому никакой автоматизации , все в ручную
    # смотрю глазами где корреляция лучше и ввожу только сдвиг
    best_shift = int(input("Введите сдвиг в месяцах: "))    
    
    
   
    #print(f"\n регрессия для сдвига {best_shift} месяцев")
 
    # вызовим функция для сопостовления рядов со сдвигами
    oil_aligned, diesel_aligned = create_aligned_series_monthly(oil_data, diesel_data, best_shift)
    
    
    correlation, a, b = calculate_correlation_and_regression(oil_aligned, diesel_aligned)
        
      
        
    print("\n уравнения функции прямой теоретической линии регрессии с подставленными значениями коэффициентов")
    print(f"y = {a:.4f} + {b:.4f} · x")
        
        
        # вызываю функцию для построения графика
    plot_correlation_and_regression(oil_aligned, diesel_aligned, a, b, 
                                    best_shift, correlation)
        
       

if __name__ == '__main__':
    main()