a = int(input())
b = int(input())
if b == 0:
    print('нельзя делить')
elif a % b == 0:
    print('да', a / b)
else:
    print('нет', a / b)
