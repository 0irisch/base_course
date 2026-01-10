figure = input('Name:')

d = {'треугольник': "t_calc", 'круг': "c_calc", 'прямоугольник': "r_calc"}
if figure == 'треугольник':
    h = int(input('Введите высоту:'))
    a = int(input('Введите основание:'))
    def t_calc():
        s = h * a / 2
        return s
    print('Площадь равна:', t_calc())

elif figure == 'круг':
    R = int(input('Введите радиус:'))
    def c_calc():
        s = 2 * 3.14 * R
        return s
    print('Площадь равна:', c_calc())

elif figure == 'прямоугольник':
    h = int(input('Введите высоту:'))
    a = int(input('Введите основание:'))
    def r_calc():
        s = h * a 
        return s
    print('Площадь равна:', r_calc())