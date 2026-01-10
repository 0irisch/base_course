

def func_stepen():
    a = int(input('Число:'))
    n = int(input('Степень:'))
    result = 1
    for i in range(n):
        result *= a
    return result
print(func_stepen('Результат:'))