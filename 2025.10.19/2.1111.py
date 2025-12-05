from pandas import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np

from pathlib import Path
from sys import path

script_dir = Path(path[0])
data = read_csv(script_dir / 'boston.csv', comment='#')

effect_vars = ['CRIM', 'NOX', 'RM', 'AGE', 'TAX','PTRATIO']
target_var = ['MEDV']

mask = data['MEDV'] != 50
x = data.loc[mask, effect_vars]
y = data.loc[mask, target_var]

test_rate = 0.20
i = int(x.shape[0]*(1-test_rate))
x_train, x_test = x.iloc[:i, :], x.iloc[i:, :]
y_train, y_test = y.iloc[:i, :], y.iloc[i:, :]

class TrueAdvancedCompositePolyTransformer(BaseEstimator, TransformerMixin):
    """Правильная реализация с разными весами для каждой степени"""
    
    def __init__(self, degrees=[2, 3, 4]):
        self.degrees = degrees
        self.linear_models = {}
        self.final_linear = LinearRegression()
        
    def fit(self, X, y=None):
        # Создаем случайные веса для каждой линейной комбинации
        np.random.seed(42)
        for degree in self.degrees:
            # Создаем случайные коэффициенты для каждой степени
            model = LinearRegression()
            
            # Создаем псевдо-целевые переменные с разными весами
            random_weights = np.random.randn(X.shape[1])
            pseudo_y = X @ random_weights + np.random.normal(0, 0.1, X.shape[0])
            
            model.fit(X, pseudo_y)
            self.linear_models[degree] = model
            
        # Трансформируем данные и обучаем финальную линейную модель
        X_transformed = self.transform(X)
        self.final_linear.fit(X_transformed, y)
        return self
        
    def transform(self, X):
        poly_features = []
        for degree in self.degrees:
            linear_output = self.linear_models[degree].predict(X)
            poly_features.append(linear_output ** degree)
        return np.column_stack(poly_features)
    
    def predict(self, X):
        X_transformed = self.transform(X)
        return self.final_linear.predict(X_transformed)

# Тестируем правильную реализацию
print('=== ТЕСТИРУЕМ РАЗНЫЕ РЕАЛИЗАЦИИ ===')

# 1. Простая линейная модель (базлайн)
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
y_pred_linear = linear_model.predict(x_test)

rmse_linear = (((y_test.values - y_pred_linear)**2).sum() / len(y_test))**0.5
r2_linear = 1 - ((y_test.values - y_pred_linear)**2).sum() / (((y_test.values - y_test.values.mean())**2).sum())

print('\n=== ПРОСТАЯ ЛИНЕЙНАЯ МОДЕЛЬ ===')
print(f'RMSE = {rmse_linear:.1f}')
print(f'R2 = {r2_linear:.0%}')

# 2. Оригинальная композитная модель (одна линейная комбинация)
class CompositePolyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, degrees=[2, 3, 4]):
        self.degrees = degrees
        self.linear_model = LinearRegression()
        
    def fit(self, X, y=None):
        self.linear_model.fit(X, y)
        return self
        
    def transform(self, X):
        linear_output = self.linear_model.predict(X)
        poly_features = []
        for degree in self.degrees:
            poly_features.append(linear_output ** degree)
        return np.column_stack(poly_features)

composite_model = Pipeline([
    ('composite_poly', CompositePolyTransformer(degrees=[2, 3, 4])),
    ('final_linear', LinearRegression())
])
composite_model.fit(x_train, y_train.values.ravel())
y_pred_composite = composite_model.predict(x_test)

rmse_composite = (((y_test.values - y_pred_composite.reshape(-1, 1))**2).sum() / len(y_test))**0.5
r2_composite = 1 - ((y_test.values - y_pred_composite.reshape(-1, 1))**2).sum() / (((y_test.values - y_test.values.mean())**2).sum())

print('\n=== ОРИГИНАЛЬНАЯ КОМПОЗИТНАЯ МОДЕЛЬ ===')
print(f'RMSE = {rmse_composite:.1f}')
print(f'R2 = {r2_composite:.0%}')

# 3. Усовершенствованная модель (разные линейные комбинации)
advanced_model = TrueAdvancedCompositePolyTransformer(degrees=[2, 3, 4])
advanced_model.fit(x_train, y_train.values.ravel())
y_pred_advanced = advanced_model.predict(x_test)

rmse_advanced = (((y_test.values - y_pred_advanced.reshape(-1, 1))**2).sum() / len(y_test))**0.5
r2_advanced = 1 - ((y_test.values - y_pred_advanced.reshape(-1, 1))**2).sum() / (((y_test.values - y_test.values.mean())**2).sum())

print('\n=== УСОВЕРШЕНСТВОВАННАЯ КОМПОЗИТНАЯ МОДЕЛЬ ===')
print(f'RMSE = {rmse_advanced:.1f}')
print(f'R2 = {r2_advanced:.0%}')

# 4. Полиномиальные признаки (для сравнения)
from sklearn.preprocessing import PolynomialFeatures

poly_model = Pipeline([
    ('poly', PolynomialFeatures(degree=4, include_bias=False)),
    ('linear', LinearRegression())
])
poly_model.fit(x_train, y_train.values.ravel())
y_pred_poly = poly_model.predict(x_test)

rmse_poly = (((y_test.values - y_pred_poly.reshape(-1, 1))**2).sum() / len(y_test))**0.5
r2_poly = 1 - ((y_test.values - y_pred_poly.reshape(-1, 1))**2).sum() / (((y_test.values - y_test.values.mean())**2).sum())

print('\n=== ПОЛИНОМИАЛЬНАЯ РЕГРЕССИЯ (degree=4) ===')
print(f'RMSE = {rmse_poly:.1f}')
print(f'R2 = {r2_poly:.0%}')

# Сравнение улучшений
print('\n=== СРАВНЕНИЕ УЛУЧШЕНИЙ ===')
print(f'Оригинальная композитная vs Линейная:')
print(f'  Улучшение R²: {((r2_composite - r2_linear) / r2_linear * 100):+.1f}%')
print(f'  Улучшение RMSE: {((rmse_linear - rmse_composite) / rmse_linear * 100):+.1f}%')

print(f'\nУсовершенствованная vs Оригинальная композитная:')
print(f'  Улучшение R²: {((r2_advanced - r2_composite) / r2_composite * 100):+.1f}%')
print(f'  Улучшение RMSE: {((rmse_composite - rmse_advanced) / rmse_composite * 100):+.1f}%')

# Выведем коэффициенты для усовершенствованной модели
print('\n=== КОЭФФИЦИЕНТЫ УСОВЕРШЕНСТВОВАННОЙ МОДЕЛИ ===')
for degree in [2, 3, 4]:
    model = advanced_model.linear_models[degree]
    intercept = model.intercept_[0] if hasattr(model.intercept_, '__len__') else model.intercept_
    print(f'\nСтепень {degree}:')
    print(f'  Коэффициенты: {model.coef_}')
    print(f'  Свободный член: {intercept:.4f}')