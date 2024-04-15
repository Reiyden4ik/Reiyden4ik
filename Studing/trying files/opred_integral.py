import math

def F(u):
    return 1/(1+u)**(K-M+2)

def f(u):
    return 1/((1+u))**2

def G(y, m, prev_lim):
    if m == M:
        res = F(y)
    else:
        res =  0
        u = prev_lim
        while u < y:
            res += G(y-u, m+1, u)*f(u)*du
            u += du
    return (math.factorial(K)/math.factorial(K-M))*res

K = 4
M = 2
du = 0.01
print(G(2, 1, 0))