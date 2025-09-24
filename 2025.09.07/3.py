# в  этом файле с ненормированными высотами

from matplotlib import pyplot as plt
from numpy import array, where
from data import temperatures_2023 


sample = temperatures_2023
n = len(sample)

print(f"значений в генеральной совокупности {n}")

# преобразую в дискретный ряд
X = array(sorted(set(sample)))
m = array([sample.count(round(elem, 1)) for elem in X])
W = m / n

print(f"в дискретном ряду {len(X)} уникальных значений")

# разделю на 4 интервала аналогично температурным сезонам
X_intervals_4 = [(-30, -13), (-13, 4), (4, 21), (21, 40)]
m_intervals_4 = []

# Расчет частот для интервалов
for j, (x1, x2) in enumerate(X_intervals_4):
    m_total = 0
    for i, x in enumerate(X):
        if j == 0:  # первый интервал
            if x1 <= x < x2:
                m_total += m[i]
            elif x == x2:
                m_total += sum(divmod(m[i], 2))
        elif j == len(X_intervals_4) - 1:  # последний интервал
            if x == x1:
                m_total += divmod(m[i], 2)[0]
            elif x1 < x <= x2:
                m_total += m[i]
        else:  # промежуточные интервалы
            if x == x1:
                m_total += divmod(m[i], 2)[0]
            elif x1 < x < x2:
                m_total += m[i]
            elif x == x2:
                m_total += sum(divmod(m[i], 2))
    m_intervals_4.append(m_total)

X_intervals_means_4 = [sum(interval)/2 for interval in X_intervals_4]
X_intervals_widths_4 = [interval[1] - interval[0] for interval in X_intervals_4]

# разделю совокупность на 12 интервалов
X_intervals_12 = [(-30, -25), (-25, -10), (-10, -5), (-5, 0), (0, 5), (5, 10), 
                  (10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40)]
m_intervals_12 = []

for j, (x1, x2) in enumerate(X_intervals_12):
    m_total = 0
    for i, x in enumerate(X):
        if j == 0:
            if x1 <= x < x2:
                m_total += m[i]
            elif x == x2:
                m_total += sum(divmod(m[i], 2))
        elif j == len(X_intervals_12) - 1:
            if x == x1:
                m_total += divmod(m[i], 2)[0]
            elif x1 < x <= x2:
                m_total += m[i]
        else:
            if x == x1:
                m_total += divmod(m[i], 2)[0]
            elif x1 < x < x2:
                m_total += m[i]
            elif x == x2:
                m_total += sum(divmod(m[i], 2))
    m_intervals_12.append(m_total)

X_intervals_means_12 = [sum(interval)/2 for interval in X_intervals_12]
X_intervals_widths_12 = [interval[1] - interval[0] for interval in X_intervals_12]

# построим три графика без нормировки
fig = plt.figure(figsize=(10, 5), dpi=100)
axs = fig.subplots(1, 3)

# 4 интервала без нормировки - использую частоты m вместо h
axs[0].bar(
    x=X_intervals_means_4,
    height=m_intervals_4,  
    width=X_intervals_widths_4,
)
axs[0].set_title('4 интервала (сезоны)')
axs[0].set_ylabel('частота')

# 12 интервалов без нормировки
axs[1].bar(
    x=X_intervals_means_12,
    height=m_intervals_12,  
    width=X_intervals_widths_12,
)
axs[1].set_title('12 интервалов (месяцы)')
axs[1].set_ylabel('частота')

# столбчатая диаграмма дискретного ряда
axs[2].bar(x=X, height=m)
axs[2].set_title('дискретный ряд')
axs[2].set_ylabel('частота')

plt.tight_layout()
plt.show()

# автоматические графики без нормировки
fig2 = plt.figure(figsize=(10, 5), dpi=100)
axs2 = fig2.subplots(1, 2)

# тут меняю  density=True на False для ненормированных гистограмм
axs2[0].hist(x=sample, bins=4, density=False)  
axs2[0].set_title('авто 4 интервала')
axs2[0].set_ylabel('Частота')

axs2[1].hist(x=sample, bins=12, density=False)  
axs2[1].set_title('авто 12 интервалов')
axs2[1].set_ylabel('Частота')

plt.tight_layout()
plt.show()