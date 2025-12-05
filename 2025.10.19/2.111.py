from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np

from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(script_dir / 'boston.csv', comment='#')

# >>> data.shape
# (506, 14)

# отобранные зависимые переменные
effect_vars = ['CRIM', 'NOX', 'RM', 'AGE', 'TAX','PTRATIO']
# целевая переменная
target_var = ['MEDV']

# маска для фильтрации значений
mask = data['MEDV'] != 50

x = data.loc[mask, effect_vars]
y = data.loc[mask, target_var]

# >>> x.shape
# (490, 6)
# >>> y.shape
# (490, 1)


# формирование обучающей и тестовой подвыборок
test_rate = 0.20
i = int(x.shape[0]*(1-test_rate))

x_train, x_test = x.iloc[:i, :], x.iloc[i:, :]
y_train, y_test = y.iloc[:i, :], y.iloc[i:, :]

# >>> x_train.shape, y_train.shape
# ((441, 6), (441, 1))
# >>>
# >>> x_test.shape, y_test.shape
# ((49, 6), (49, 1))


class CompositePolyTransformer(BaseEstimator, TransformerMixin):
    """Кастомный преобразователь по вашему рецепту: (линейная_комбинация)^2 + (линейная_комбинация)^3 + ..."""
    
    def __init__(self, degrees=[2, 3, 4]):
        self.degrees = degrees
        self.linear_model = None
        
    def fit(self, X, y=None):
        # Обучаем линейную модель для получения коэффициентов
        self.linear_model = LinearRegression()
        self.linear_model.fit(X, y)
        return self
        
    def transform(self, X):
        # Вычисляем линейную комбинацию: a1*x1 + a2*x2 + ... + b
        linear_output = self.linear_model.predict(X).flatten()
        
        # Создаем полиномиальные признаки по вашему рецепту
        poly_features = []
        for degree in self.degrees:
            poly_features.append(linear_output ** degree)
            
        return np.column_stack(poly_features)

# Создаем модель по вашему рецепту
composite_model = Pipeline([
    ('composite_poly', CompositePolyTransformer(degrees=[2, 3, 4])),
    ('final_linear', LinearRegression())
])

# обучение модели
composite_model.fit(x_train, y_train.values.ravel())

# тестирование модели
y_pred = composite_model.predict(x_test)

# >>> y_pred.shape
# (49,)

# метрики:
# среднеквадратичная ошибка
rmse = (((y_test.values - y_pred.reshape(-1, 1))**2).sum() / len(y_test))**0.5
# коэффициент детерминации
r2 = 1 - ((y_test.values - y_pred.reshape(-1, 1))**2).sum() / (((y_test.values - y_test.values.mean())**2).sum())
# скорректированный коэффициент детерминации
r2_adj = 1 - (1 - r2)*(x_test.shape[0] - 1) / (x_test.shape[0] - len(composite_model.named_steps['composite_poly'].degrees) - 1)

print('=== ВАША КОМПОЗИТНАЯ МОДЕЛЬ ===')
print(f'RMSE = {rmse:.1f}\nR2 = {r2:.0%}\nR2 (adjusted) = {r2_adj:.0%}')

# Для сравнения - оригинальная линейная модель
original_model = LinearRegression()
original_model.fit(x_train, y_train)
y_pred_original = original_model.predict(x_test)

rmse_original = (((y_test - y_pred_original)**2).sum() / len(y_test))**0.5
r2_original = 1 - ((y_test - y_pred_original)**2).sum() / (((y_test - y_test.mean())**2).sum())
r2_adj_original = 1 - (1 - r2_original)*(x_test.shape[0] - 1) / (x_test.shape[0] - x_test.shape[1] - 1)

print('\n=== ОРИГИНАЛЬНАЯ ЛИНЕЙНАЯ МОДЕЛЬ ===')
print(f'RMSE = {rmse_original.iloc[0]:.1f}\nR2 = {r2_original.iloc[0]:.0%}\nR2 (adjusted) = {r2_adj_original.iloc[0]:.0%}')

# Выведем информацию о модели
composite_transformer = composite_model.named_steps['composite_poly']
final_linear = composite_model.named_steps['final_linear']

print(f'\n=== СТРУКТУРА МОДЕЛИ ===')
print(f'Первая линейная комбинация коэффициенты: {composite_transformer.linear_model.coef_}')
print(f'Первая линейная комбинация свободный член: {composite_transformer.linear_model.intercept_}')
print(f'Финальные веса для полиномов: {final_linear.coef_}')
print(f'Финальный свободный член: {final_linear.intercept_}')