



import tkinter as my_interface
from tkinter import ttk
from pandas import read_csv
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from ts_init import births
import warnings

 
# когда я еще в терминале переберал циклы с параметрами модели 
#  что-бы автоматизировать поиск лучших параметров
# циклов было 1369 и вылезали всякие надписи 
# которые как будто блокировали межцикловые выводы
# которые мне мешали отслеживать прогресс
# пришлось все переделать на ручной лад
# и найти как убрать эту ошибку https://docs.python.org/3/library/warnings.html#warnings.filterwarnings
warnings.filterwarnings("ignore")

# 
y = births

# 
test_rate = 0.2
n = len(y)
test_size = int(n * test_rate)
train_size = n - test_size

y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]


# переделываю обучение в функцию

def poprobyem(p, d, q):
    model = ARIMA(y_train, order=(p, d, q))
    model_fit = model.fit()
    
    #  прогназирование на 73 шага вперед    1/5 от 365
    y_pred = model_fit.forecast(steps=test_size)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    return y_pred, rmse, r2



# сначала сделал по другому но гдето напортачил с выводом в многострочное окно
# решил сделать отдельную функцию, ато немного запутался

def pysk():
    output_text.delete(1.0, my_interface.END)
    
    p = int(text_vvod1.get())
    q = int(text_vvod2.get())
    
# d = 2 и выше уж совсем все портит, 1 терпимо но почему то метрики хуже чем у 0, 
# видимо потому что рождаемость  хорошо стационарный ряд
    d = 0
    
    
    y_pred, rmse, r2 = poprobyem(p, d, q)
    output_text.insert(my_interface.END, f"параметры аримы({p},{d},{q})\n")
    output_text.insert(my_interface.END, f"RMSE = {rmse:.2f}\n")
    output_text.insert(my_interface.END, f"R² = {r2:.1%}\n")
    

# главное окно
window = my_interface.Tk()
window.title("арима")
window.geometry("400x300")

# поле для ввода p
label1 = my_interface.Label(window, text="введите p:")
label1.pack(pady=5)
text_vvod1 = my_interface.Entry(window, width=20)
text_vvod1.pack(pady=5)
text_vvod1.insert(0, "1")  

# поле для ввода q
label2 = my_interface.Label(window, text="введите q:")
label2.pack(pady=5)
text_vvod2 = my_interface.Entry(window, width=20)
text_vvod2.pack(pady=5)
text_vvod2.insert(0, "1")  

# кнопка
button = my_interface.Button(
    window,
    text="запуск модели",
    command=pysk,
    bg="lightblue"
)
button.pack(pady=10)

# поле для вывода результатов
output_text = my_interface.Text(window, height=8, width=40)
output_text.pack(pady=10)

window.mainloop()