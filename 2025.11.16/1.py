# вижу примерно такой план
# 1.выставляю настройки для основной модели
# 2. ставлю перехват на ввод фильма
# 3. подготовлюсь к поиску схожих фильмов
# 4. произвести поиск
# 5. сформировать результаты
# 








# давно хотел попрактиковаться в визуализации интерфейса
# попробую поработать с тикинтером или как там он правельно читается))

# вообще тут применяется сокращения для удобства, 
# но я пока оставлю более понятное мне выражение для тикинтера
import tkinter as my_interface

# более расширенные возможности библиотеки
# планирую использовать выпадающие списки для задания процессоров и около фильмов
# надеюсь избежать этим написание проверок по их правельному вводу 
from tkinter import ttk

# тут вроде все нормально
from sklearn.neighbors import NearestNeighbors

# это для импорта переменных с предидущего файла
from recommendation_init import *

# тут я попробую написать функцию 
# в которую заключу операции с recommendation_system
# я проюовал сначала написать интерфейс а потом писать функцию
# но почему то не сработало, вроде как нельзя вызвать функцию которая написана после ее вызова
# раньше я сначала функцию и писал, видимо поэтому упустил этот момент 
def my_recreational_movie_search_system():
    
    # буду использовать эту переменную для выпадающего списка по количеству похожих фильмов
    # метод get из библиотеки тикинтер нужен для вытаскивания значения из интерфейса, должно получиться
    number_of_similar_movies = int(spisok1.get()) 

    # эта переменная для определения нагрузки на процессора   
    CPU_load = spisok2.get()   
        
    # в перспективе идея по разгранечению нагрузки на процессора может быть полезной
    # предположу что в среднем все имеют не менее 4 процессоров
    # разграничу нагрузку по трем степеням, при проверке разницы не обнаружил
    if CPU_load == "все процессоры":
    # все процессоры        
        number_of_CPUs = -1
    elif CPU_load == "половина процессоров":
    # на всякий случай поставлю не два а все минус 2 процессора, надеюсь так и сработает        
        number_of_CPUs = -3
    else:  
    # один процессор        
        number_of_CPUs = 1    
    
       
    # 
    try:
       
        # в эту переменную получаю текст , метод strip() удалет пробелы с обеих сторон 
        name_movie_to_search = text_vvod.get().strip()

        
         # очень плохо работает поле вывода, его придется как то циклично чистить
        if not name_movie_to_search:
        
        # у тикинтера есть методы делит чтобы очистить многострочное поле, работает необычно    
        # 1.0 означает первый символ, хотя я предполагал что должно быть 0
        # my_interface.END так обозначаем конец строки    
            
            output_text.delete(1.0, my_interface.END)
            
            
            # тут вообще с 50-го раза сработало, очень странно работает
            # получается метод берет все перед концом строки, и если там пусто 
            # то выводит сообщение об ошибке            
            output_text.insert(my_interface.END, "ошибка: названия не введено")
            return
        
        # ищем фильм в базе данных,  нашел коечто для регистронезависимости case=False
        mask_search = movies_ref_filt['title'].str.contains(name_movie_to_search, case=False)
        search_results = movies_ref_filt.loc[mask_search]
        
        
        # использую метод empty для определения не пустой ли результат
        if search_results.empty:
        
        # тут все уже по старой схеме
            output_text.delete(1.0, my_interface.END)
            output_text.insert(my_interface.END, f"ошибка: Фильм '{name_movie_to_search}' не найден ")
            return
        
        # получаю индексы строк найденных фильмов и кладу в перменную первый индекс
        movie_index = search_results.index[0]
        
        # кладу в перменную всю строковую информацию по первой позиции
        movie_info = search_results.iloc[0]
        
        # вот теперь создаем модель
        model = NearestNeighbors(
        
        # количество соседей заданных в выпадающем списке
            n_neighbors=number_of_similar_movies,
            
        # применяем перебор    
            algorithm='brute',
        # косинусное растояние     
            metric='cosine',
        # нагрузка на процессора    
            n_jobs=number_of_CPUs
        )
        
        # обучаю модель и выполняю поиск
        # импортирую разряженную матрицу
        model.fit(movies_ratings_filt_csc)
        # теперь получаем вектор признаков для выбранного индекса фильма, 
        # попутно изменяем форму вектора 1 -1 и из одномерного массива делаем двумерный
        # я так понял метод kneighbors принимает именно двумерные массивыы
        vector_search = movies_ratings_filt_csc[movie_index].reshape(1, -1)
        
        # тут получаю результат поиска 
        result = model.kneighbors(vector_search)
        
        # вытягиваю название фильмов title и год выпуска
        result_text = f"похожие фильмы на: '{movie_info['title']}' ({movie_info['year']})\n"
        # 
        result_text += "=" * 50 + "\n\n"
        
        # теперь будем работать с результатом напрямую через result[0] и result[1]
        # начину с 1, чтобы пропустить сам фильм 0
        for i in range(1, len(result[0][0])):
        
        #  из результата 0 беру расстояние, из результата 1 беру индексы фильмов
        #  хочу использовать отдельно дистанцию для коекакой наглядности
            distance = result[0][0][i]  
            idx = result[1][0][i]       p
         
        # поиск фильмов, получаю фильмы из датафрейма по индексу         
            similar_movie = movies_ref_filt.iloc[idx]
            
        # текстовый результат , буду циклично выводить фильмы года и дистанцию    
            
            result_text += f"{i}. {similar_movie['title']} ({similar_movie['year']})\n"
            
        # вот зачем я вытащил из результата дистанцию, хочу паралельно видеть степень похожести
        # как я понял чем меньше угол между векторами тем больше их похожесть
        # интерпритрую эту схожесть в проценты
            result_text += f"   похожесть: {100*(1 - distance):.1f}%\n\n"
        
        # вывожу результат в мнострокое поле
        output_text.delete(1.0, my_interface.END)
        output_text.insert(my_interface.END, result_text)
     
     # вообще я не планировал так много блоков класть в перехват, но забылся
     # поэтому пусть будет такое околоуниверсальное исключение
    
    except Exception as e:
        output_text.delete(1.0, my_interface.END)
        output_text.insert(my_interface.END, f"серьезная ошибка связанная с {str(e)}")

# гавное окно
window = my_interface.Tk()
window.title("рекомендация фильмов")
window.geometry("600x500")

# первый выпадающий список - количество похожих фильмов
label1 = my_interface.Label(window, text="количество похожих фильмов:")
#метод для расположения списка, берем 5 отступов по вертикали
label1.pack(pady=5)
# варинты количества фильмов
spisok1 = ttk.Combobox(window, values=["5", "10", "20", "50"])
spisok1.pack(pady=5)
# нашел метод для выбора по умолчанию
spisok1.set("10") 

# второй выпадающий список - нагрузка на процессор
label2 = my_interface.Label(window, text="нагрузка на процессор:")
label2.pack(pady=5)

spisok2 = ttk.Combobox(window, values=["все процессоры", "половина процессоров", "один процессор"])
spisok2.pack(pady=5)
spisok2.set("все процессоры")  

# тут важное поле для ввода фильмов
text_label = my_interface.Label(window, text="введите название фильма:")
text_label.pack(pady=5)

# entery класс для создания однострокового поля, куда и буду вводить фильм
text_vvod = my_interface.Entry(window, width=50)
text_vvod.pack(pady=5)

# тут как то все долго не складывалось
# window располагает кнопку внутри основного окна
# 
search_button = my_interface.Button(
    window, 
    text="искать похожие фильмы", 
    # вот теперь вызываем функцию при нажатии, но работает как то странно 
    # не сразу понял что должно вызываться без аргументов,
    # предполагаю в более сложно ситуации надо к кнопке отдельно привязывать аргументы
    # https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Button  
    command=my_recreational_movie_search_system,
    bg="lightblue"
)

# обьект кнопки
search_button.pack(pady=10)

# помещу надпись в многострочное окно
output_label = my_interface.Label(window, text="результаты поиска:")
output_label.pack(pady=5)
# забыл сформировать само многострочное окно)))
output_text = my_interface.Text(window, height=15, width=70)
output_text.pack(pady=5)

# оказалось что я не предусмотрел прокрутку
# yview основной метод для вертикальной прокрутки
scrollbar = my_interface.Scrollbar(window, command=output_text.yview)
scrollbar.pack(side=my_interface.RIGHT, fill=my_interface.Y)
output_text.config(yscrollcommand=scrollbar.set)

# главный цикл визуализации, без него почти сразу окно закрывается
window.mainloop()