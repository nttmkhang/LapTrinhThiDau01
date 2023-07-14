def isPrime(n):
    dem = 0
    for i in range (1, n + 1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        return True
    return False

def findPrime(n):
    prime = []
    for p in range (2, n + 1):
        if isPrime(p):
            prime.append(p)
    return prime
