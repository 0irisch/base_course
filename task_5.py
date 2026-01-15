name = 'Shchepeleva Irina Aleksandrovna'
upper_spisok = 0
name_upper = name.upper()
print(name_upper)

for symbol in name_upper:
    print(ord(symbol), end="; ")
    upper_spisok += ord(symbol)
print()



name_lower = name.lower()
print(name_lower)
lower__spisok = 0

for symbol in name_lower:
    print(ord(symbol), end="; ")
    lower__spisok += ord(symbol)
print()

summa = upper_spisok + lower__spisok
print(summa)
