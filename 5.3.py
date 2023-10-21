def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    # Вычисляем P(not A) - вероятность несобытия A
    p_not_a = 1 - p_a

    # Вычисляем полную вероятность P(B)
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)

    # Вычисляем P(A|B) - условную вероятность A при условии B
    p_a_given_b = (p_b_given_a * p_a) / p_b

    return p_a_given_b


# Пример использования функции
p_a = 5/12  # Априорная вероятность события A
p_b_given_a = 4/11  # Условная вероятность события B при условии A
p_b_given_not_a = 5/11  # Условная вероятность события B при условии не A

result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
print(f"Условная вероятность A при условии B: {result}")
