#№1
import math
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input())
z2 = int(input())
def f(x1, x2, y1, y2, z1, z2):
    p = [(x1, x2), (y1, y2), (z1, z2)]
    ma = float('inf')
    ir = None
    for p in p:
        a = math.atan2(p[1], p[0])
        if a < ma:
            ma = a
            ir = p
    return ir
print(f(x1, x2, y1, y2, z1, z2))

#№2
n = int(input())

def ipal(bs):
    return bs == bs[::-1]
def ip(numb):
    if numb < 2:
        return False
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False
    return True
def ppn(n):
    pp = []
    for numb in range(2, n + 1):
        bs = bin(numb)[2:]
        if ipal(bs) and ip(numb):
            pp.append(numb)
    return pp

res = ppn(n)
print(f" {n}  {res}")

#№3
a = float(input())
b = float(input())
R = float(input())
n = 0
def f(x,y): 
    if (x-a)**2+(y-b)**2<R**2: 
        return True 
    else: 
        return False 
p1 = float(input())
p2 = float(input())
if f(p1,p2): 
    print("Точка P лежит внутри окружности") 
    n+=1
else: 
    print("Точка P лежит не внутри окружности") 
f1 = float(input())
f2 = float(input())
if f(f1,f2): 
    print("Точка F лежит внутри окружности") 
    n+=1
else: 
    print("Точка F лежит не внутри окружности") 
l1 = float(input())
l2 = float(input())
if f(l1,l2): 
    print("Точка L лежит внутри окружности") 
    n+=1
else: 
    print("Точка L лежит не внутри окружности")
print('Всего точек пренадлежащих окружности:', n)
