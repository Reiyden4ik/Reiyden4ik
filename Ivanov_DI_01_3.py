#1
a = float(input('Введите число, стоимость 1 кг конфет: '))
for i in range(1, 11):
  print(a*i)
#2
ar = []
n = int(input())
for i in range(n): 
  x = int(input())
  ar.append(x)
ar.append(0) 

d = 0
r = 0
a = len(ar)
while a > 0:
  d += ar[a - 1]
  r += 1
  a -= 1
print(i, c)
#3
r = 0
a = [1, '2', 3, 4, '5']
for i in a :
  i = int(i)
  r +=i
print(r)
#4

#1Hw
k = 0
n = int(input())
if n < 100:
  for i in range(1, n+1):
    k = k + i**3
print(k)

#2Hw
for i in range(1, 10):
  for j in range(1, 10):
    print(i, '*', j, '=', i*j, sep='')

