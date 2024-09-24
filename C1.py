kb = int(input("Введите число КБ: "))

mb, byte, bit = kb // 1024, kb * 1024, kb * 8192

print(f'МБ-{mb}, Байты-{byte}, Бит-{bit}')