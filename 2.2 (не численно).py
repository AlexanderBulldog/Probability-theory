# На каждой грани правильного додекаэдра написаны числа от 1 до 12
# (игральный додекаэдр). Бросаются 3 додекаэдра на плоскость и считается
# сумма значений на гранях, лежащих на плоскости. Выписать 5 самых
# вероятных сумм и их вероятности.

# Решение с помощью теории вероятности (не численно) 
from itertools import product

# Все возможные значения на гранях додекаэдра
values = list(range(1, 13))

# Все возможные комбинации для бросков трех додекаэдров
combinations = list(product(values, repeat=3))

# Создадим словарь для подсчета количества каждой суммы
sum_counts = {}

# Подсчитываем количество каждой суммы
for combo in combinations:
    total_sum = sum(combo)
    if total_sum in sum_counts:
        sum_counts[total_sum] += 1
    else:
        sum_counts[total_sum] = 1

# Сортируем суммы по вероятности и выводим 5 самых вероятных
sorted_sums = sorted(sum_counts.items(), key=lambda x: x[1], reverse=True)
top_5_sums = sorted_sums[:5]

# Вычисляем вероятности для каждой суммы
total_combinations = len(combinations)
probabilities = [(sum_val, count / total_combinations) for sum_val, count in top_5_sums]

# Выводим 5 самых вероятных сумм и их вероятности
for sum_val, probability in probabilities:
    print(f"Сумма: {sum_val}, Вероятность: {probability:.4f}")
