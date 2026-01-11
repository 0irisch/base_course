name = 'Shchepeleva Irina Aleksandrovna'
name_str = ""
for i in name:
    name_str += i + '_'
name_upper = name_str.upper()
print(name_upper)

for symbol in name_upper:
    print(ord(symbol), end="; ")
print()



name_lower = name_str.lower()
print(name_lower)

name_upper_spisok = ""
for symbol in name_upper_spisok:
    print(ord(symbol), end="; ")
print(name_upper_spisok)

