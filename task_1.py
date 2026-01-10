h = int(input('Введите высоту:'))
V = int(input('Введите скорость:'))
m = int(input('Введите массу:'))
g = 9.8

def mech_energy():
    E = (m+(V**2))/2 + m*g*h
    return E
print('С задаваемыми значениями:', mech_energy())




h = 10
V = 10
m = 10
g = 9.8

def mech_energy():
    E = (m+(V**2))/2 + m*g*h
    return E
print('С обязательными значениями:', mech_energy())




d = {'m':10, 'h':10,'V':10,'g':9.8,}
def mech_energy():
    E = (m+(V**2))/2 + m*g*h
    return E
print('Со словарем:', mech_energy())