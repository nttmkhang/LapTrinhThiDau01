
def Nhap() :
    n = int(input("Nhap n: "))
    return n;

# Muc 5.1.3

def Fibonancci(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return Fibonancci(n - 1) + Fibonancci(n - 2)

def main() :
    n = Nhap()
    a = Fibonancci(n)
    print("So Fibonacci thu n:", a)
   
if __name__ == "__main__" :
    main()