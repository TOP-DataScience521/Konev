import tkinter as my_interface
from tkinter import ttk
from pandas import read_csv
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from ts_init1 import passengers  
import warnings


# когда я еще в терминале переберал циклы с параметрами модели 
# что-бы автоматизировать поиск лучших параметров
# циклов было 1369 и вылезали всякие надписи 
# которые как будто блокировали межцикловые выводы
# которые мне мешали отслеживать прогресс
# пришлось все переделать на ручной лад
# и найти как убрать эту ошибку https://docs.python.org/3/library/warnings.html#warnings.filterwarnings
warnings.filterwarnings("ignore")

# 
y = passengers

# 
test_rate = 0.2
n = len(y)
test_size = int(n * test_rate)
train_size = n - test_size

y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]


# переделываю обучение в функцию

def poprobyem(p, d, q, P, D, Q, s):
    # 
    model = SARIMAX(
        y_train, 
        # несезонные параметры
        order=(p, d, q),     
        # сезонные параметры
        seasonal_order=(P, D, Q, s),  
        
    )
    model_fit = model.fit()
    
    # прогназирование на 28 шагов вперед
    y_pred = model_fit.forecast(steps=test_size)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    return y_pred, rmse, r2



# сначала сделал по другому но гдето напортачил с выводом в многострочное окно
# решил сделать отдельную функцию, ато немного запутался

def pysk():
    output_text.delete(1.0, my_interface.END)
    
    
    # авторегрессия   Количество лагов зависимой переменной в модели
    p = int(text_vvod1.get())  

# порядок диференциирования , сколько нужно взять разностей для стационарности   
    d = int(text_vvod3.get())  
    
    #сколзящее среднее, текущая ошибка зависит от q количества параметров
    q = int(text_vvod2.get())
    
    #сезонные лаги, пока не могу точно понять чем отличается от Q
    P = int(text_vvod4.get())  
    
    # сезонная разность
    D = int(text_vvod5.get())  
    
    #опять сезонные лаги, влияние ошибок Q периодов
    Q = int(text_vvod6.get()) 

#    период сезонности
    s = int(text_vvod7.get())  
    
    
    y_pred, rmse, r2 = poprobyem(p, d, q, P, D, Q, s)
    output_text.insert(my_interface.END, f"параметры саримакс({p},{d},{q})({P},{D},{Q})[{s}]\n")
    output_text.insert(my_interface.END, f"RMSE = {rmse:.2f}\n")
    output_text.insert(my_interface.END, f"R² = {r2:.1%}\n")
    

# главное окно
window = my_interface.Tk()
window.title("саримакс - анализ пассажиров")  # изменил заголовок
window.geometry("450x600")  # увеличил окно для дополнительных параметров

# поле для ввода p 
label1 = my_interface.Label(window, text=" p (авторегрессия):")
label1.pack(pady=5)
text_vvod1 = my_interface.Entry(window, width=20)
text_vvod1.pack(pady=5)
text_vvod1.insert(0, "1")  


label3 = my_interface.Label(window, text=" d (диференциирование):")
label3.pack(pady=5)
text_vvod3 = my_interface.Entry(window, width=20)
text_vvod3.pack(pady=5)
text_vvod3.insert(0, "1")  # значения по умолчанию


label2 = my_interface.Label(window, text=" q (скользящее среднее):")
label2.pack(pady=5)
text_vvod2 = my_interface.Entry(window, width=20)
text_vvod2.pack(pady=5)
text_vvod2.insert(0, "1")  


label4 = my_interface.Label(window, text=" P (влияние сезонности):")
label4.pack(pady=5)
text_vvod4 = my_interface.Entry(window, width=20)
text_vvod4.pack(pady=5)
text_vvod4.insert(0, "1")  


label5 = my_interface.Label(window, text=" D (сезонные диференциирование):")
label5.pack(pady=5)
text_vvod5 = my_interface.Entry(window, width=20)
text_vvod5.pack(pady=5)
text_vvod5.insert(0, "1")  


label6 = my_interface.Label(window, text=" Q (влияние ошибок сезонности):")
label6.pack(pady=5)
text_vvod6 = my_interface.Entry(window, width=20)
text_vvod6.pack(pady=5)
text_vvod6.insert(0, "1")  


label7 = my_interface.Label(window, text=" s (период сезонности):")
label7.pack(pady=5)
text_vvod7 = my_interface.Entry(window, width=20)
text_vvod7.pack(pady=5)
text_vvod7.insert(0, "12") 

# кнопка
button = my_interface.Button(
    window,
    text="запустить модель саримакс",
    command=pysk,
    bg="lightgreen"
)
button.pack(pady=10)

# поле для вывода результатов
output_text = my_interface.Text(window, height=8, width=50)
output_text.pack(pady=10)

window.mainloop()