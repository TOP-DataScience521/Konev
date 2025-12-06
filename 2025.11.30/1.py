from matplotlib import pyplot as plt
from pandas import Series
from statsmodels.tsa.seasonal import seasonal_decompose, STL

from ts_init import births, passengers, online, script_dir
import tkinter as my_interface
from tkinter import ttk

# time_series = trend + seasonal + residuals


def ts_decompose(time_series: Series, period: int):
    # вычисление тренда скользящим средним
    trend = Series([], name=f'{time_series.name or "ts"}_trend_ma_{period}')
    for i in range(0, len(time_series)-period+1):
        dt_index = time_series.index[i+period//2]
        trend.loc[dt_index] = time_series.iloc[i:i+period].mean()
    # вычисление сезонности посредством вычитания тренда и усреднения по периодам
    seasonal = time_series - trend
    for i in range(len(time_series.index)-period):
        subgroup = seasonal[i::period]
        seasonal.iloc[i] = subgroup.mean()
    seasonal.name = f'{time_series.name or "ts"}_seasonal_{period}'
    # вычисление остатков посредством вычитания тренда и сезонгости
    residuals = time_series - trend - seasonal
    residuals.name = f'{time_series.name or "ts"}_residuals'
    
    return trend, seasonal, residuals





def grafiki():

    a = int(text_vvod1.get())
    b = a
    p = a
    o = a





    data = (
        (births.iloc[:, 0], {'period': b}),
        (passengers.iloc[:, 0], {'period': p}),
        (online.iloc[:, 0], {'period': o}),
)
    for ts, options in data:
    # самостоятельное разложение на компоненты на основе скользящего среднего
        trend, seasonal, residuals = ts_decompose(ts, **options)
    
        fig = plt.figure(figsize=(10, 15))
        axs = fig.subplots(4, 1, sharex=True)
    
        axs[0].plot(ts.index, ts.values)
        axs[1].plot(trend.index, trend.values)
        axs[2].plot(seasonal.index, seasonal.values)
        axs[3].scatter(residuals.index, residuals.values)
    
        bottom, top = axs[0].get_ylim()
        ylim_delta = top - bottom
        for i in range(1, 4):
            bottom = axs[i].get_ylim()[0]
            axs[i].set(ylim=(bottom, bottom+ylim_delta))
    
        fig.savefig(script_dir / f'ts_{ts.name}_decompose_{a}.png')
    
    
    # разложение на компоненты на основе скользящего среднего с уточнением сезонности
        decomposed = seasonal_decompose(ts, **options)
        fig = decomposed.plot()
        fig.savefig(script_dir / f'ts_{ts.name}_decompose_statsmodels_{a}.png')
    
    
    # разложение на компоненты на основе регрессии
        decomposed = STL(ts, **options).fit()
        fig = decomposed.plot()
        fig.savefig(script_dir / f'ts_{ts.name}_decompose_STL_{a}.png')
    

# главное окно
window = my_interface.Tk()
window.title("период сезонности")
window.geometry("400x300")

# поле для ввода периода
label1 = my_interface.Label(window, text="введите период")
label1.pack(pady=5)
text_vvod1 = my_interface.Entry(window, width=20)
text_vvod1.pack(pady=5)
text_vvod1.insert(0, "1") 


 



# кнопка
button = my_interface.Button(
    window,
    text="запустить формирование графиков",
    command=grafiki,
    bg="lightblue"
)
button.pack(pady=10)


window.mainloop()