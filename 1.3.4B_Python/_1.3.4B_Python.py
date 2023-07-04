def HexaToDecimal(n):
    temp = 0
    for i in range(len(n)):
        temp *= 16
        temp += int(n[i], 16)
    return temp

def main():
    sHexa = input("Nhap chuoi thap luc phan: ")
    print("\nGia tri thap phan cua chuoi", sHexa, "la:", HexaToDecimal(sHexa))
    print("\n\n\nKet thuc!!!!")
if __name__ == "__main__":
    main()

