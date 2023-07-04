def mulEgyptModulo(a, b, M):
    if b == 0:
        return 0
    t = mulEgyptModulo(a, b // 2, M) % M
    if b % 2 != 0:
        return (t + t + a % M) % M
    return (t + t) % M

def main():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    M = int(input("Nhap M: "))
    print("a * b % M = ", mulEgyptModulo(a, b, M))

if __name__ == "__main__":
    main()