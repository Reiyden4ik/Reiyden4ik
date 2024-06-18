def sieve_of_eratosthenes(n):
    # Создаем список, где все элементы изначально равны True
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Итерируемся от 2 до sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        # Если i - простое число, то помечаем как составные все его кратные
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Возвращаем список простых чисел
    return [p for p in range(2, n + 1) if sieve[p]]

# Пример использования
n = 1000
primes = sieve_of_eratosthenes(n)
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]