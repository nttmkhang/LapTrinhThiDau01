def DecimalToBinary(n):
    temp = ""
    while n > 0:
        if n % 2 != 0:
            temp = '1' + temp
        else:
            temp = '0' + temp
        n //= 2
    return temp

def main():
    n = int(input("Nhap n (n <= 10^9): "))
    print("Bieu dien so thap phan ")
    print(n, "o he co so 2 la: ")
    print(DecimalToBinary(n))
    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()
