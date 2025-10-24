a = int(input())
b = 1
c = 1
j = []
j.append(b)
j.append(c)
for i in range(a):
    s = b + c
    j.append(s)
    b = c
    c = s
print(j)