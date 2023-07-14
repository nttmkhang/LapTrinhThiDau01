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

def outVector(a):
    temp = ""
    i = 0
    while i < len(a):
        temp = temp + " " + str(a[i])
        i += 1
    return temp

def main():
    n = int(input("Nhap n (n <= 10^9): "))

    print("\nCac so nguyen to nho hon bang ", n, "la: ", outVector(findPrime(n)))
    
    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()
