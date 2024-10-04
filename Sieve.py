primes, check = [], []

def sieve(N: int):
    
    global check
    global primes 

    check = [False] * (N + 1)
    primes.clear()

    for i in range(2, N + 1):
        if not check[i]:
            primes.append(i)
        
        for p in primes:
            if i * p > N:
                break
            check[i * p] = True
            if i % p == 0:
                break
