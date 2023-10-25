#№1

n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '')
    print()
print(max(a[0][2], a[1][2], a[2][2]))
print(max(a[1][0], a[1][1], a[1][2]))

#№2

m = int(input())
n = int(input())
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
print()
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
for i in range(m):
    for j in range(n):
        if a[i][j] > 0:
            a[i][j] = 1
        if a[i][j] < 0:
            a[i][j] = 0
for i in range(m):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()
  
#№3

n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()
sa = sum(a[0])
ms = True
cs = sum(a[j])
for i in range(n):
    if sum(a[i]) != sa:
        ms = False
        break
for j in range(n):
    if cs != sa:
        ms = False
        break
if ms:
    print("Магический квадрат")
else:
    print("Not магический квадрат")

#№4

n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end = '  ')
    print()
asim = True
for i in range(n):
    for j in range(i, n):
        if a[i][j] != a[j][i]:
            asim = False
            break
if asim:
    print("Матрица симметрична")
else:
    print("Матрица не симметрична")
