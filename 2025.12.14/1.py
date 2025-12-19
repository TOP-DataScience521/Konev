


from numpy import arange, append, concatenate

# export_text  - нашел такую штуку, если смогу то попоробую воспользоваться
# для текстового представления дерева
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import tkinter as my_interface
from tkinter import ttk, scrolledtext
from pathlib import Path
from sys import path
import pandas as pd
from numpy.random import default_rng
from itertools import pairwise
from pandas import DataFrame
import numpy as np  

# загружаю данные
data_raw = load_breast_cancer()
X, y = data_raw.data, data_raw.target
#------------------------------ перераспределение данных чередованием классов
# постоянно при определении точности при кросвалидации расчитываются разные значения точности
# буду уберать оттуда каждый раз новую рандомность и  поэтому на всякий случай
# идеально перечередую выборку по классам

# беру все данные с классом 1 и классом 0 
i0 = np.where(y == 0)[0]  
i1 = np.where(y == 1)[0]  

# определяю тот класс которого больше и меньше
if len(i0) < len(i1):
    s, l = i0, i1
else:
    s, l = i1, i0

# вычисляю соотношение классов и округлю в большую сторону 
# (-1)должно быть правельно при целых числах
#что-бы определить через какое количество одного класса  должны чередоваться с другим классом
r = (len(l) + len(s) - 1) // len(s)



# создаю идеально чередованные индексы, 
idx = []
for i in range(len(s)):
    idx.append(s[i])           # 1 элемент меньшего класса
    idx.extend(l[i*r:i*r+r])   # r элементов большего класса

# добавлю оставшиеся элементы большего класса
idx.extend(l[len(s)*r:])

# применяю чередование
X, y = X[idx], y[idx]

# разделю на тренировочную и тестовую выборки

test_size = 0.3
n_test = int(len(X) * test_size)
X_train, X_test = X[:-n_test], X[-n_test:]
y_train, y_test = y[:-n_test], y[-n_test:]


# функция для решающего дерева
def my_tree():
    # будем глубину дерева получать сюда из выпадающего списка
    selected_value = spisok1.get()
    
    # тут просто так зеначение нон не сработало, пришлось написать условие
    if selected_value == "None":
        max_depth_param = None
        depth_display = "None"
    else:
        max_depth_param = int(selected_value)
        depth_display = selected_value
    
    # тут использую ранее заготовленные тестовые и боевые данные
    model = DecisionTreeClassifier(criterion='entropy', max_depth=max_depth_param)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # вывод в текстовое поле
    result_text = f"Обученное дерево (глубина={depth_display}): точность {accuracy:.2%}\n"
    output_text.insert(my_interface.END, result_text)
    output_text.see(my_interface.END)
    #print(f"точность  {accuracy:.2%}")




# функция для к фолдов
def k_fold_split(data, k):
    fold_len, res = divmod(data.shape[0], k)
    slices_idx = [0]
    acc = 0
    for fl, res_add in zip([fold_len]*k, [1]*res + [0]*(k-res)):
        acc += fl + res_add
        slices_idx.append(acc)
    folds = []
    for i, j in pairwise(slices_idx):
        folds.append(data[i:j])
    return folds




# функция для кросс-валидации
def my_k_valid():
    # выпадающий список с выбором количества фолдов
    selected_value1 = spisok2.get()
    k = int(selected_value1)
    
    # вот хочу тут использовать глобальные X, y ,без перемешивания
    data = np.column_stack([X, y])  
    
    folds = k_fold_split(data, k)
    
    accuracies = []
    for i in range(k):
        train = concatenate(folds[:i] + folds[i+1:])
        test = folds[i]
        
        x_train, y_train = train[:, :-1], train[:, -1]
        x_test, y_test = test[:, :-1], test[:, -1]
        
        model = DecisionTreeClassifier(criterion='entropy')
        model.fit(x_train, y_train)
        
        y_pred = model.predict(x_test)
        accuracies.append(accuracy_score(y_test, y_pred))
    
    accuracy_mean = sum(accuracies) / len(accuracies)
    result_text = f"кросс-валидация (K={k})  Точность {accuracy_mean:.1%}\n"
    output_text.insert(my_interface.END, result_text)
    output_text.see(my_interface.END)

# главное окно
window = my_interface.Tk()
window.title("деревья решений")
window.geometry("600x500")

# улучшаем интерфейс
title_label = my_interface.Label(
    window,
    text="классификация рака груди с идеальным чередованием",
    font=("Arial", 12, "bold")
)
title_label.pack(pady=10)

# секция для обычного дерева
frame1 = my_interface.Frame(window)
frame1.pack(pady=10)

label1 = my_interface.Label(frame1, text="Глубина дерева:")
label1.pack(side=my_interface.LEFT, padx=5)

spisok1 = ttk.Combobox(frame1, values=["None", "2", "3", "4","5", "6", "7", "8","9", "10"], width=10)
spisok1.pack(side=my_interface.LEFT, padx=5)
spisok1.set("2")

search_button = my_interface.Button(
    window, 
    text="Обучить обычное дерево", 
    command=my_tree,
    bg="lightblue"
)
search_button.pack(pady=10)

# разделительная полоса
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', padx=20, pady=10)

# зона для кросс-валидации
frame2 = my_interface.Frame(window)
frame2.pack(pady=10)

label2 = my_interface.Label(frame2, text="количество фолдов K:")
label2.pack(side=my_interface.LEFT, padx=5)

spisok2 = ttk.Combobox(frame2, values=["2", "3", "4", "5", "6", "7", "8"], width=10)
spisok2.pack(side=my_interface.LEFT, padx=5)
spisok2.set("5")

search_button1 = my_interface.Button(
    window, 
    text="выполнить кросс-валидацию", 
    command=my_k_valid,
    bg="lightgreen"
)
search_button1.pack(pady=10)

# разделительная полоса
separator2 = ttk.Separator(window, orient='horizontal')
separator2.pack(fill='x', padx=20, pady=10)

# зона результатов
results_label = my_interface.Label(window, text="Результаты:", font=("Arial", 10, "bold"))
results_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(window, height=10)
output_text.pack(pady=10, padx=10, fill=my_interface.BOTH, expand=True)

# основной цикл
window.mainloop()