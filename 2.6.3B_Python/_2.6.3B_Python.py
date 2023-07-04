
def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Muc 2.6.3, cai tien lan 1

def Eratosthenes(n):
    isprime = [True] * (n + 1)
    isprime[0] = False
    isprime[1] = False
    
    for p in range(2, n + 1):
        if isprime[p] == True:
            for i in range(p * p, n + 1, p):
                isprime[i] = False
    
    prime = []
    for p in range(2, n + 1):
        if isprime[p] == True:
            prime.append(p)
    
    return prime

def main() :
    n = Nhap()
    prime = Eratosthenes(n)
    print("Cac so nguyen to be hon n: ")
    print(prime)
   

if __name__ == "__main__" :
    main()
