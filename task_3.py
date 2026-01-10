
def count_func():
    a = int(input('От:'))
    b = int(input('До:'))
    N = int(input('Колво точек:'))
    step = (b - a) / (N + 1)
    results = []
    for i in range(1, N + 1 ):
        x = (a + i) * step
        y = x**2
        results.append((x, y))
    return results
print(count_func())
