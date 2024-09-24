temp = int(input("Введите температуру(целым числом): "))
precip = bool(input("Есть осадки? (0/1): "))
wind = bool(input("Есть ветер? (0/1): "))
temp_class = None

if temp > 30: temp_class = "very_high"
elif temp in range(20, 31): temp_class = "high"
elif temp in range(0, 20): temp_class = "so_low"
elif temp in range(-20, 0): temp_class = "low"
else: temp_class = "very_low"

if temp_class == "very_high":
    if precip:
        if wind: print("Жарко, ветренно, идёт дождь. Взять зонтик, одеться в закрытую одежду.")
        else: print("Жарко, идёт дождь.")
    else:
        if wind: print("Жарко, ветренно. Одеваться в закрытую одежду одежду")
        else: print("Жарко.")
elif temp_class == "high":
    if precip:
        if wind: print("Тепло, ветренно, идёт дождь. ")
        else: print("Тепло, идёт дождь.")
    else:
        if wind: print("Тепло, ветренно.")
        else: print("Тепло")
elif temp_class == "so_low":
    if precip:
        if wind: print("Прохладно, ветренно, идёт дождь")
        else: print("Прохладно, идёт дождь")
    else:
        if wind: print("Прохладно, ветренно")
        else: print("Прохладно")
elif temp_class == "low":
    if precip:
        if wind: print("Холодно, ветренно, идёт снег.")
        else: print("Холодно, идёт снег.")
    else:
        if wind: print("Холодно, ветренно.")
        else: print("Холодно.")
elif temp_class == "very_low":
    if precip:
        if wind: print("Очень холодно, ветренно, идёт снег.")
        else: print("Очень холодно, идёт снег.")
    else:
        if wind: print("Очень холодно, ветренно.")
        else: print("Очень холодно.")
