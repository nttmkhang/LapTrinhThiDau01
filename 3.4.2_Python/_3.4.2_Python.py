def sumDivisors_2(n):
    T = 1
    p = 2
    while n > 1:
        count = 0
        power = 1
        while n % p == 0:
            power *= p
            count += 1
            n /= p
        T = T * (power * p - 1) / (p - 1)
        p += 1
    return T

def main():
    n = int(input("Nhap n: "))
    print("Tong cac uoc so cua n la: ", sumDivisors_2(n))


if __name__ == "__main__":
    main()