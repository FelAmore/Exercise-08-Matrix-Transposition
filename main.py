m = eval(input('Enter a matrix: '))
c = []
for i in range(len(m[0])):
    r = []
    for k in range(len(m)):
        r.append(m[k][i])
    c.append(r)
print(c)