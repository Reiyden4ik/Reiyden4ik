# №1
s = str(input())
k = 0
s = s.lower()
for i in s.split(' '):
  if i.strip()[0] == 'е':
    k+=1
print(k)

# №2
p = str(input())
p = p.replace(':', '%')
q = p.count('%')
print(q)
print(p)

# №3
r = str(input())
l = r.count('.')
r = r.replace('.', '')
print(r)
print(l)

# №4
c = [-5, -4, -3, 2, 1, -3, -2, -9, -8, -2]
for i in range(1, len(a)):
  if c[i-1]<0 and c[i]<0:
    print(c[i-1], c[i])

# №5
a = int(input())
a = [int(input()) for i in range(n)]
k = a.index(min(a))
print(min(a), k)

# №6
b = [0, 3, 16, 4, 35, 43, 2, 6]
for i in range(len(a)):
  if b[i]<15:
    k = b[i]*2
    print(k)

# № 1 Из домашней работы
s = str(input())
s = s.lower()
maxx=1
n=1
for i in range(len(s)-1):
    if s[i]=='н' and s[i+1]=='н':
        n+=1
        if c>maxx:
            maxx=c
    else:
        n=1
maxx = max(n, maxx)
print(maxx)
s = s.replace('.', '!')
print(s)
# № 2 Из домашней работы
s = str(input())
for i in range(len(s)):
    if s[i] == "(":
        while s[i+1]!=")":
            print(s[i+1])
            i+=1
# № 3 Из домашней работы
print(*[s for s in input().split() if s[0] == 'а' or s[-1] == 'я'])
