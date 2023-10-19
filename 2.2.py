import random
import matplotlib.pyplot as plt

def roll_dodecahedron():
    return [random.randint(1, 12) for _ in range(3)]

def simulate_rolls(num_simulations):
    sums = {}
    for _ in range(num_simulations):
        result = sum(roll_dodecahedron())
        if result in sums:
            sums[result] += 1
        else:
            sums[result] = 1

    return sums

num_simulations = 1000000
sums = simulate_rolls(num_simulations)

# Сортировка сумм по вероятности
sorted_sums = sorted(sums.items(), key=lambda x: x[1], reverse=True)

# Вывести 5 самых вероятных сумм и их вероятности
print("5 самых вероятных сумм и их вероятности:")
for i, (result, count) in enumerate(sorted_sums[:5], start=1):
    probability = count / num_simulations
    print(f"{i}. Сумма: {result}, Вероятность: {probability:.4f}")

# Визуализация результатов
results, counts = zip(*sorted_sums)
normalized_counts = [count / num_simulations for count in counts]  # Нормализация значений
plt.bar(results, normalized_counts)
plt.xlabel('Сумма')
plt.ylabel('Вероятность')
plt.title('Распределение сумм после броска додекаэдров')
plt.show()
