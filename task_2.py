name = 'Shchepeleva Irina Aleksandrovna'
name_str = ""
for i in name:
    name_str += i + '_'
name_upper = name_str.upper()
print(name_upper)

upper_code = []
for symbol in name_upper:
    print(ord(symbol), end="; ")
    upper_code.append(ord(symbol))
print()



name_lower = name_str.lower()
print(name_lower)

lower_code = []
for symbol in name_lower:
    print(ord(symbol), end="; ")
    lower_code.append(ord(symbol))
print()

codes = lower_code + upper_code
print(max(codes))
print(min(codes))
