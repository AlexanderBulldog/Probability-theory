from decimal import Decimal
import math

def binomial_probability(n, k, p):
    # Вычисляем биномиальный коэффициент C(n, k)
    binomial_coefficient = Decimal(math.comb(n, k))
    
    # Вычисляем вероятность по формуле Бернулли
    probability = binomial_coefficient * (Decimal(p) ** k) * ((Decimal(1) - Decimal(p)) ** (n - k))
    
    return probability

# Пример использования функции
n = 4  # Общее количество экспериментов
k = 2   # Количество успешных событий
p = Decimal("0.5")  # Вероятность успешного события в виде Decimal

result = binomial_probability(n, k, p)
print(f"Вероятность получить {k} успешных событий из {n} экспериментов: {1 - result}")
