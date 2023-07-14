def toChar(n):
    return chr(n)

def DecimalToBinary(n):
    temp = ""
    while n:
        if n & 1:
            temp = "1" + temp
        else:
            temp = "0" + temp
        n >>= 1
    return temp

def main():
    n = int(input("Nhap n (n <= 10^9): "))
    print("\nBieu dien so thap phan", n, "o he co so 2 la:", DecimalToBinary(n))
    print("\n\n\nKet thuc!!!!")

if __name__ == "__main__":
    main()
