#На грани правильного додекаэдра написали первые буквы названий
#месяцев. Сколько раз нужно бросить додекаэдр, чтобы с вероятностью
#0,99 выпала хотя бы 1 раз буква А?

n = 1
probability = (10/12)**n
while probability > 0.01:
    n += 1
    probability = (10/12)**n
print ("Миниальное количество бросков:", n, f"Шанс выпадения при {n} бросках", 1 - probability)