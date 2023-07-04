def uscln(a, b):
	a = abs(a);
	b = abs(b);
	while b > 0:
		a = a % b;
		a ,b = b, a
	return a

def bscnn_1(a, b):
    return (a * b) / uscln(a, b)

def Nhap():
	a = int(input("Nhap a: "))
	b = int(input("Nhap b: "))
	return a, b

def main():
	a, b = Nhap()
	print("Boi so chung nho nhat cua a va b la: ", bscnn_1(a, b))

if __name__ == "__main__":
	main()