import scipy.integrate
import math

def li(n):
    return scipy.integrate.quad(lambda t: 1 / math.log(t), 0, n)[0]
def count_primes(n):
    is_prime = [True] * n
    count = 0
    for i in range(2, n):
        if is_prime[i]:
            count += 1
            print(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    print("Count of prime numbers:", count)
    print("Li function estimate:", li(n))
count_primes(100)