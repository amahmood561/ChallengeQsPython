def primes(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for x in range(2, int(n ** 0.5)):
        if is_prime[x]:
            for i in range(x ** 2, n, x):
                is_prime[i] = False
    for i in range(n):
        if is_prime[i]:
            yield i
