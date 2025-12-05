from matplotlib import pyplot as plt
from pandas import Series
import tkinter as my_interface
from tkinter import ttk

from ts_init import births, passengers, online, script_dir



def my_funk():

    alpha1 = float(spisok1.get()) 
    alpha = alpha1

    births_expsm = [births.iloc[0, 0]]

    for i in range(1, len(births.index)):
        births_expsm.append(alpha * births.iloc[i, 0] + (1 - alpha) * births_expsm[i-1])

    births_expsm = Series(
        births_expsm,
        index=births.index, 
        name=f'exp_smooth_{alpha}'
    )

    fig = plt.figure(figsize=(15, 6))
    axs = fig.subplots()

    axs.plot(births.index, births.iloc[:, 0].values)
    axs.plot(births_expsm.index, births_expsm.values)
    axs.set(title=f'alpha = {alpha}')

    fig.savefig(script_dir / f'ts_births_expsm_alpfa{alpha}.png')
    plt.close(fig)



    

    passengers_expsm = [passengers.iloc[0, 0]]

    for i in range(1, len(passengers.index)):
        passengers_expsm.append(alpha * passengers.iloc[i, 0] + (1 - alpha) * passengers_expsm[i-1])

    passengers_expsm = Series(
        passengers_expsm,
        index=passengers.index, 
        name=f'exp_smooth_{alpha}'
    )

    fig = plt.figure(figsize=(15, 6))
    axs = fig.subplots()

    axs.plot(passengers.index, passengers.iloc[:, 0].values)
    axs.plot(passengers_expsm.index, passengers_expsm.values)
    axs.set(title=f'alpha = {alpha}')

    fig.savefig(script_dir / f'ts_passengers_expsm_alpfa{alpha}.png')
    plt.close(fig)




    online_expsm = [online.iloc[0, 0]]

    for i in range(1, len(online.index)):
        online_expsm.append(alpha * online.iloc[i, 0] + (1 - alpha) * online_expsm[i-1])

    online_expsm = Series(
        online_expsm,
        index=online.index, 
        name=f'exp_smooth_{alpha}'
    )

    fig = plt.figure(figsize=(15, 6))
    axs = fig.subplots()

    axs.plot(online.index, online.iloc[:, 0].values)
    axs.plot(online_expsm.index, online_expsm.values)
    axs.set(title=f'alpha = {alpha}')

    fig.savefig(script_dir / f'ts_online_expsm_alpfa{alpha}.png')
    plt.close(fig)










# гавное окно
window = my_interface.Tk()
window.title("экспоненциальное сглаживание")
window.geometry("600x500")

search_button = my_interface.Button(
    window, 
    text="применить экспоненциальное сглаживание", 
    # вот теперь вызываем функцию при нажатии, но работает как то странно 
    # не сразу понял что должно вызываться без аргументов,
    # предполагаю в более сложно ситуации надо к кнопке отдельно привязывать аргументы
    # https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button  
    command=my_funk,
    bg="lightblue"
)


# варинты количества фильмов
spisok1 = ttk.Combobox(window, values=["0.2", "0.4", "0.6", "0.8"])
spisok1.pack(pady=5)
spisok1.set("0.2")

# обьект кнопки
search_button.pack(pady=10)


# главный цикл визуализации, без него почти сразу окно закрывается
window.mainloop()