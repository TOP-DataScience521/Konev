from numpy import array, corrcoef, linspace
from matplotlib import pyplot as plt
from pathlib import Path
from sys import path

# попробую составить функцию , как я понял допустимую для малых данных и не рекемендованную для больших
def read_csv_data(filename):
   
   
# полный путь к файлу
    file_path = Path(path[0]) / filename
# читаю весь файл в виде одной строке в русской кодировке
    text = file_path.read_text(encoding='utf-8')
# разбиваю общую строку на список маленьких    
    lines = text.split('\n')
    
# раз тут всего две колонки то на ум приходит словарь, попробую им и поработать
    data = {}
# это будет цикл по каждой строке из списка строк    
    for row in lines:
        # буду удалять пробелы и переносы,  а так же игнорировать закоментированные строки
        if row.strip() and not row.startswith('#'):
            # буду разбивать строки по частям если там где есть пробел
            parts = row.split()
            # на всякий случай проверю что будет только два значения
            if len(parts) == 2:
            # буду помещать значения в две переменные
                year, value = parts
                # вообще хотелось бы все округлить до целого , но оставлю вторую колонку значений не целыми
                # и помещю в словарь
                data[int(year)] = float(value)
    # коплю прочтенные значения в словарь
    return data


# читаю данные по инвестициям в медицину
medical_investments = read_csv_data('science_investetions.csv')

# читаю данные о больних
сancer_patients = read_csv_data('early_malignancy.csv')

# print("Смотрю что получилось с затратами на исследование :", medical_investments)
# print("смотрю что получилось с больными:", сancer_patients)
# на первый взгляд вроде все норм.


# теперь хочу написать функцию которая подстелит солому сразу под несколько задач
# dataset1 - это будет первый словарь со сзначениями
# dataset2 - это будет второй словарь со сзначениями
# common_starting_year - общий начальный год
# shift_in_years - заложу сразу смещение по годам
# series_length - после нескольких неудачных эксперементов решил заложить сразу и длинну создаваемых рядов
def create_synchronized_series(dataset1, dataset2, common_starting_year, shift_in_years, series_length):
    
    #  пустые списки для датасетов
    list_dataset1 = []
    list_dataset2 = []
    
    # тут буду для каждого года составлять пары с заданным сдвигом
    for i in range(series_length):
        year1 = common_starting_year + i
        year2 = common_starting_year + i + shift_in_years
    
    #  тут очень важный момент, так как наборы годов из csv  файлов не одинаковы по количеству годов 
    # а то у меня ничего ничего не полачется(    
        if year1 in dataset1 and year2 in dataset2:
            list_dataset1.append(dataset1[year1])
            list_dataset2.append(dataset2[year2])
        else:
            return None, None
    # целью будет являться преобразование моих списков в массивы
    return array(list_dataset1), array(list_dataset2)



#science_years = (medical_investments.keys())
#cancer_years = (сancer_patients.keys())
#print (f'проверка {science_years} {cancer_years}')




# функция для вычисления корреляции со сдвигом
# shift_in_years - насколько сдвигаем по годам
 
 
def calculate_correlation_with_shift_in_years(shift_in_years):
   
    
    #  смотрим какие есть года , так как они являются ключами в словаре, 
    #  в другой ситуации я бы сразу отсортировал года, но в исходниках уже все по порядку
    science_years =(medical_investments.keys())
    cancer_years = (сancer_patients.keys())
    
    # настраиваю диапозоны годов с учетом сдвигов и что-бы не попасть в несуществующие данные
    start_science = max(min(science_years), min(cancer_years) - shift_in_years)
    end_science = min(max(science_years), max(cancer_years) - shift_in_years)
    
    # тут упустил подводный камень, прибавил неучтенный год к количеству
    series_length = end_science - start_science + 1
    
        
    # а вот подстеленная солома, создаст два массива данных из парных значений
    science_series, cancer_series = create_synchronized_series(
        medical_investments, сancer_patients, start_science, shift_in_years, series_length
    )
        
        # отнормализую данные что-бы можно было сравнить рубли с процентами
    science_norm = (science_series - science_series.mean()) / science_series.std()
    cancer_norm = (cancer_series - cancer_series.mean()) / cancer_series.std()
    
    # теперь непосредственно вычислю кэффицент корреляции между инвестициями и больными
    corr_coef = corrcoef(science_norm, cancer_norm)[0, 1]
    
    return corr_coef, science_series, cancer_series, start_science, series_length


# головная функция для расчета корреляции

def analyze_correlations():
    
    science_years = (medical_investments.keys())
    cancer_years = (сancer_patients.keys())
    
    # на 500 раз запуска кода уже все слимвается, добавил разделительную полосу
    print("\n" + "=|="*40)
    
    # возьму сдвиги от 0 до +5 лет
    min_shift_in_years = 0
    max_shift_in_years = 5
    
    # цикл для вывода заголовка по каждому сдвигу
    for shift_in_years in range(min_shift_in_years, max_shift_in_years + 1):
        
     
        # как раз вычисляет корреляцию для текущего сдвига в цикле
        result = calculate_correlation_with_shift_in_years(shift_in_years)
        
        # распоковываем кортеж
        corr, science_series, cancer_series, common_starting_year, series_length = result
            
        # определяем годы для вывода
        science_years_used = []
        for i in range(series_length):
            year = common_starting_year + i
            science_years_used.append(year)

        # медицинские года со сдвигом
        cancer_years_used = []
        for i in range(series_length):
            year = common_starting_year + i + shift_in_years
            cancer_years_used.append(year)
         
        print (f'Вариационные ряды (горизонтально) \n')         
        print(f'Годы затрат на науку: {science_years_used}')
        print(f'Сумма затрат: {science_series}')
        print(f'Годы ранней диагностики: {cancer_years_used}')
        print(f'Процент выявления заболеваний: {cancer_series} \n')
        print(f'Величина сдвига значений показателей по временной шкале (в годах) {shift_in_years} \n ')
        print(f'Коэффициент корреляции: {corr:.4f}')
        print("\n" + "-"*40)

if __name__ == '__main__':
    # запуск анализа
    analyze_correlations()