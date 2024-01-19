#1
s = str(input())
k=0
s = s.lower()
for i in s.split(' '):
  if i.strip()[0] == 'е':
    k+=1
print(k)

#2
s = str(input())
s = s.replace(':', '%')
q = s.count('%')
print(q)
print(s)

#3
s = str(input())
q = s.count('.')
s = s.replace('.', '')
print(s)
print(q)

#4
a = [-5, -4, -3, 2, 1, -3, -2, -9, -8, -2]
for i in range(1, len(a)):
  if a[i-1]<0 and a[i]<0:
    print(a[i-1], a[i])

#5
n = int(input())
a = [int(input()) for i in range(n)]
k = a.index(min(a))
print(min(a), k)

#6
a = [0, 3, 16, 4, 35, 43, 2, 6]
for i in range(len(a)):
  if a[i]<15:
    k = a[i]*2
    print(k)

#1 Д/з
s = str(input())
s = s.lower()
mx=1
c=1
for i in range(len(s)-1):
    if s[i]=='н' and s[i+1]=='н':
        c+=1
        if c>mx:
            mx=c
    else:
        c=1
mx = max(c, mx)
print(mx)
s = s.replace('.', '!')
print(s)

#2 Д/з
s = str(input())
for i in range(len(s)):
    if s[i] == "(":
        while s[i+1]!=")":
            print(s[i+1])
            i+=1
#3 Д/з
print(*[s for s in input().split() if s[0] == 'а' or s[-1] == 'я'])
