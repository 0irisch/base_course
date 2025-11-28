g = 9.8
def my_func(m, h, V):
    Ep = m * g * h
    Ek = (m * V**2)/2
    A = Ep + Ek
    return Ep + Ek
print(A)