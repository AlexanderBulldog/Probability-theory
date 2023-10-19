# Задача 2.6. В таблице выписаны простые числа от 1 до 1000. Событие A — сумма
#цифр простого числа кратна 5. Событие B — простое число начинается с
#1. Событие C — простое число двухзначное. Найти вероятность события
#(A∆C) \ B.

# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Функция для вычисления суммы цифр числа
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# Находим все простые числа от 1 до 1000
primes = [n for n in range(1, 1001) if is_prime(n)]

# Находим числа, удовлетворяющие событию A
event_A = [n for n in primes if digit_sum(n) % 5 == 0]

# Находим числа, удовлетворяющие событию B
event_B = [n for n in primes if str(n).startswith('1')]

# Находим числа, удовлетворяющие событию C (двузначные простые числа)
event_C = [n for n in primes if 10 <= n <= 99]

# Находим событие (A∆C)
event_A_delta_C = list(set(event_A).symmetric_difference(event_C))

# Находим событие ((A∆C) \ B)
result_event = list(set(event_A_delta_C) - set(event_B))

# Вычисляем вероятность ((A∆C) \ B)
total_primes = len(primes)
probability = len(result_event) / total_primes

print("Вероятность события ((A∆C) \ B) равна:", probability)
