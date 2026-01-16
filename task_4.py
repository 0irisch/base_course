
def area(figure, *args):
    if figure == 'треугольник':
        s = args[0] * args[1] / 2
        print('Площадь равна:', s)
    elif figure == 'круг':
        s = 2 * 3.14 * args[0]
        print('Площадь равна:', s)
    elif figure == 'прямоугольник':
         s = args[0] * args[1]
         print('Площадь равна:', s)
    else:
        s = None
        print(s) 
    return s

trioales_square = area('треугольник', 8, 8 , 0, 7, 7)