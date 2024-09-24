try:
    line = int(input("Строк на странице: "))
    letters = int(input("Символов в строке: "))
    page = int(input("Кол-во листов: "))
    alfabet = int(input("Символов в алфавите: "))
    bit = 0

except:
    print("Введите число")

def degree(line, letters, page, alfabet):
    for i in range(1, 1000):
        if 2**i >= alfabet:
            bit = i
            break

    print(f'{page * line * letters * bit * 2 * 8} Бит')
    print(f'{page * line * letters * bit * 2 / 1024} КБ')

degree(line, letters, page, alfabet)