import math

def Factorization(n):
    minprime = [0] * (n + 1)
    for p in range (0, n + 1):
        minprime[p] = p
    for p in range (2, int(math.sqrt(n))):
        if minprime[p] == p:
            for i in range (p * p, n + 1, p):
                if minprime[i] == i:
                    minprime[i] = p

    factorprime = []
    while n > 1:
        factorprime.append(minprime[n])
        n //= minprime[n]
    return factorprime

def Xuat(arr):
    for i in range(0, len(arr)):
        print(arr[i])

def main():
    n = int(input("Nhap n: "))
    factorprime = Factorization(n)
    Xuat(factorprime)

if __name__ == "__main__":
    main()
