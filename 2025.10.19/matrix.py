from pathlib import Path
from sys import path
import pandas as pd
import matplotlib.pyplot as plt

script_dir = Path(path[0])

# Предполагаем, что функция read_csv определена ранее
data = pd.read_csv(script_dir / 'boston.csv', comment='#')

# Вычисляем корреляционные матрицы
corr_pearson_matrix = data.corr()
corr_spearman_matrix = data.corr('spearman')
corr_average_matrix = (corr_pearson_matrix + corr_spearman_matrix) / 2

# Выводим матрицы
print("Матрица Пирсона")
print(corr_pearson_matrix.round(3))


print("Матрица Спирмена")
print(corr_spearman_matrix.round(3))


print("Матрица средних значений")
print(corr_average_matrix.round(3))

