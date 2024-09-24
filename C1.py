type = input("Введите тип данных(гб, мб, кб): ")

try:
    num = int(input())
except:
    print("Введите число")
    exit()

if type == "гб":
    mb = num * 1024
    kb = mb * 1024
    byte = kb * 1024
    bit = byte * 8
    print(f'МБ - {mb},КБ - {kb},Байт - {byte},Бит - {bit}')
elif type == "мб":
    kb = num * 1024
    byte = kb * 1024
    bit = byte * 8
    print(f'КБ - {kb},Байт - {byte},Бит - {bit}')
else:
    mb = num // 1024
    byte = num * 1024
    bit = byte * 8
    print(f'МБ - {mb},Байт - {byte},Бит - {bit}')
