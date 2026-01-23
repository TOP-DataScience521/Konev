# работа с массивами и математикой
import numpy as np
# для датафреймов
import pandas as pd
# работа с путями файловых системы
from pathlib import Path
# для поиска модулей питона
from sys import path
# будем с помощью этго делить на обучающие и тестовые выборки
from sklearn.model_selection import train_test_split
# видел такую для стандартизации
# почему стандартизация а не нормализация, вычитал что для релу лучше стандартизация
# но это не точно( 
from sklearn.preprocessing import StandardScaler

# импортируем именно такую линейную модель под бостон,
# по пути узнал такую модель как Functional API много входов и выходов, какието мули модели
# Subclassing эту не совсем понял, но видимо какаято гибкая модель для тонкой личной настройки,
from tensorflow.keras import Sequential, Input

# полносвязаные слои
from tensorflow.keras.layers import Dense
# оптимизатор адам для обучения сети, у адама есть скорость и момент,
# с одной стороны адам ускоряется если градиенты в одном направлении, с другой стороны
# при больших градиентах уменаешь леринг райте-шаг обучения, очень интересно
from tensorflow.keras.optimizers import Adam

# возьмем для использования среднеквадратичную ошибку
from tensorflow.keras.losses import MeanSquaredError

# ну и например среднюю абсолютную ошибку
from tensorflow.keras.metrics import MeanAbsoluteError

script_dir = Path(path[0])
boston_path = script_dir / 'boston.csv'

# отобранные влияющие переменные
effect_vars = ['LSTAT', 'RM', 'PTRATIO', 'TAX', 'INDUS']
# целевая переменная
target_var = ['MEDV']

# загрузка данных
df = pd.read_csv(boston_path, comment='#')

# разделение на влияющие и целевую переменную
X = df[effect_vars].values
y = df[target_var].values.ravel()

# стандартизация данных
scaler_X = StandardScaler()
scaler_y = StandardScaler()

# вычисляем среднее и преобразуем
X_scaled = scaler_X.fit_transform(X)
# тут уже знакомое для меня требование 2д массива
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

# разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42
)

# создаем модельку
model = Sequential(
    [
        Input(shape=(5,)),# вход на 5 признаков
        Dense(units=64, activation='relu', name='hidden1'),# 1 слой 
        Dense(units=32, activation='relu', name='hidden2'),# 2 слой  
        Dense(units=1, activation='linear', name='output'),# выход, пока 1 нейрон для регресии
    ], 
    name='boston123'
)

print()
model.summary()

# настройка обучения сети, как учебный план обучения
model.compile(
    loss=MeanSquaredError(),   # функция потерь MSE 
    
    # базовый шаг обучения от которого будет отталкиваться адам при адаптировании
    optimizer=Adam(learning_rate=0.001), 
    
    metrics=[
        MeanAbsoluteError(name='mae'), # метрика, средняя абсолютная ошибка
    ]
)


# настройка обучения сети, более детальное проведение обучение
fit_result = model.fit(
    x=X_train,
    y=y_train,
    epochs=200,
    batch_size=32,
    verbose=1,
    validation_split=0.1,
)


# тестирование обучение модели
print()
test1_result = model.evaluate(
    x=X_test,
    y=y_test,
    verbose=2, # такой тип вывод только метрики
)

# предсказания на тестовых данных в стандартизированном виде
predictions_scaled = model.predict(X_test, verbose=1)

# обратное преобразование к исходному масштабу
predictions = scaler_y.inverse_transform(predictions_scaled)
y_test_original = scaler_y.inverse_transform(y_test.reshape(-1, 1))



#Epoch 200/200
#12/12 [==============================] - 0s 4ms/step - loss: 0.0640 - mae: 0.1849 - val_loss: 0.2832 - val_mae: 0.3294
#
#4/4 - 0s - loss: 0.1660 - mae: 0.2415 - 27ms/epoch - 7ms/step
#4/4 [==============================] - 0s 999us/step