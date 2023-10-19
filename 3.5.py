# Задача 3.5. Предположим, что все забыли свои дни рождения. Найти вероятность
# того, что дни рождения 12 человек придутся на разные месяцы?

group_members = 12
summ_birthday = 1
for i in range (1, 12):
    birthday_probability = i/group_members
    summ_birthday *= birthday_probability
print (summ_birthday*100) 