import math

def Eratosthenes(n):
    isprime = [True] * (n + 1)
    isprime[0] = False
    isprime[1] = False
    for p in range (2, int(math.sqrt(n + 1))):
        if(isprime[p] == True):
            for i in range (p * p, n + 1, p):
                isprime[i] = False
    prime = []
    for p in range (0, n + 1):
        if(isprime[p] == True):
            prime.append(p)
    return prime

def Xuat(prime):
    for i in range (0, len(prime)):
        print(prime[i])

def main():
    n = int(input("Nhap n: "))
    prime = Eratosthenes(n)
    Xuat(prime)

if __name__ == "__main__":
    main()