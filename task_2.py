
def sr_arif(*args):
    summa = 0
    for i in args:
         summa += i
    A = summa / len(args)
    return A

print(sr_arif(1,2,3))