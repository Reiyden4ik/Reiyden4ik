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

#1 Из домашнего задания
k = 0
n = int(input())
if n < 100:
  for i in range(1, n+1):
    k = k + i**3
print(k)

#2 Из домашнего задания
s1=int(input()
for i in range(1, s1+1):
     print(*range(i, i*s1+1, i), sep='\t')

#3 Задание про алфавит

i=0
alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(33):
    if i%6!=0:
        print('|', alf[i].upper(), alf[i], '|', sep='', end='')
    else:
        print('\n''--------------------')

#4 Задание про прямоугольник
n = int(input())
m = int(input())
print("@"*m)
for i in range(n-2):
    print("@"+" "*(m-2)+"@")
print("@"*m)
