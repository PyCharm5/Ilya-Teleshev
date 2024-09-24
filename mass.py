mass = str.split(input())
numb = []

for el in mass:
    numb.append(ord(el))
for i in range(min(numb), max(numb)):
    if i in numb:
        continue
    else:
        print(chr(i))


print(numb)