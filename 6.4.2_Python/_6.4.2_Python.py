def powerModulo(a, b, M):
    t = 1
    a = a % M
    while b > 0:
        if b % 2 == 1:
            t = (t * a) % M
        b = b // 2
        a = (a * a) % M
    return t

def main():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    M = int(input("Nhap M: "))
    print("a * b % M = ", powerModulo(a, b, M))

if __name__ == "__main__":
    main()