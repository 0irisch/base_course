import numpy as np
import task_1 as t1


h = 100
a = 45
b = 35

V = ((t1.g * h * np.tan(b)**2)/(2 * np.cos(a)**2*(1 - np.tan(b)*np.tan(a))))*0.5
print(V)


T = 200000
E = 300

N = (2/(3.14)*0.5) * ((t1.H)*0.5)*((t1.k * T)**3/2) * ((E**E)/(t1.k * T)) * (E**T/2)
print(N)