import math
a = float(input("Введите страший коэффициент а "))
b = float(input("Введите коэффициент x "))
c = float(input("Введите свободный член "))

D = b*b-4*a*c

if a == b == c == 0:
  print('x ∈ R, D = 0')

if a == b == 0 and c!=0:
  print('Корней нет, D = 0 ')

if a == 0 and b!=0 and c!=0:
  print('x = ', -c/b)
  print("D = ", b*b)

if a!=0 and b == c == 0:
  print('x = 0, D = 0')

if a==0 and b!=0 and c==0:
  print('x = 0, D = ', D = b*b)

if a!=0 and b!=0 and c==0:
  print('x1 = 0, x2 = ', -b/a)

if a!=0 and b!=0 and c!=0:
  if D < 0:
    print('Корней нет')
  if D == 0:
    x = -b/2*a
    print('Корень уравнения x = ', x)
    print("Дискриминант равен = ", D)
  if D > 0:
    x = (-b + math.sqrt(D))/2*a
    y = (-b - math.sqrt(D))/2*a
    print('Корни уравнения x1, x2 соответственно равны ', x, y)
    print("Дискриминант равен = ", D)
