import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Количество случайных точек для Монте-Карло
n_points = 10000

# Генерация случайных точек
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, b**2, n_points)  # Верхня межа значення функції - максимальне значення f(x)

# Вычисление точек под кривой
points_under_curve = np.sum(y_random < f(x_random))

# Площадь под кривой
area_monte_carlo = (b - a) * (b**2) * points_under_curve / n_points
print(f"\nПлощадь под кривой (Метод Монте-Карло): {area_monte_carlo}")

# Створення графіка для візуалізації
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Визуализация точек Монте-Карло
ax.scatter(x_random, y_random, s=1, color='blue', alpha=0.3, label='Точки Монте-Карло')
ax.fill_between(x, f(x), color='gray', alpha=0.3, label='Площадь под кривой')

# Налаштування графіка
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графік функції та інтеграл методом Монте-Карло')

plt.legend()
plt.grid()
plt.show()



# Результат інтегрування та оцінку абсолютної помилки
# Визначте функцію для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print(f"Аналитическое значение интеграла: {result} с погрешностью: {error}")