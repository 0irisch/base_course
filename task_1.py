h = int(input('Введите высоту:'))
V = int(input('Введите скорость:'))
m = int(input('Введите массу:'))
g = 9.8

def mech_energy():
    E = (m+(V**2))/2 + m*g*h
    return E
print('С задаваемыми значениями:', mech_energy())


def mech_energy(h, V, m, g):
    E = (m+(V**2))/2 + m*g*h
    return E

print('С обязательными значениями:', mech_energy(1, 4, 6, 8))




d = {'m':10, 'h':10,'V':10,'g':9.8,}
def mech_energy():
    E = (m+(V**2))/2 + m*g*h
    return E
print('Со словарем:', mech_energy())