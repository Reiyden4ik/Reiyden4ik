n = int(input())
k=0
while n!=1:
    if n%2!=0:
        n = n*3+1
        print(int(n))
        k = k+1
    else:
        n = n/2
        print(int(n))
        k = k+1
if n == 1:
    print('end')
    print(k)