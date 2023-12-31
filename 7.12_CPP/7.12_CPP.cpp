#include <iostream>
using namespace std;

typedef string BigNum;

int toNumber(char);
char toChar(int);
BigNum addBigNum(BigNum, BigNum);
BigNum BigFibonacci(long);

int main()
{
	long n;
	cout << "Nhap n: ";
	cin >> n;
	cout << "So hang fibo thu " << n << " : ";
	cout << BigFibonacci(n);
	cout << "\n\n\nKet thuc!!!!";
	return 1;
}

BigNum addBigNum(BigNum x, BigNum y) {
	while (x.size() < y.size()) {
		x = "0" + x;
	}
	while (y.size() < x.size()) {
		y = "0" + y;
	}
	int carry = 0;
	BigNum temp = "";
	for (int i = x.size() - 1; i >= 0; --i) {
		int xx = toNumber(x[i]);
		int yy = toNumber(y[i]);
		int ss = xx + yy + carry;
		temp = toChar(ss % 10) + temp;
		carry = ss / 10;
	}
	if (carry > 0) {
		temp = "1" + temp;
	}
	return temp;
}

BigNum BigFibonacci(long n)
{
	BigNum Ftt = "1";
	BigNum Ft = "1";
	long i = 2;
	BigNum Fhh = "1";
	while (i < n)
	{
		Fhh = addBigNum(Ft, Ftt);
		i++;
		Ftt = Ft;
		Ft = Fhh;
	}
	return Fhh;
}

char toChar(int n) {
	char Letter[] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F' };
	return Letter[n];
}

int toNumber(char c)
{
	if (c == '0')
		return 0;
	if (c == '1')
		return 1;
	if (c == '2')
		return 2;
	if (c == '3')
		return 3;
	if (c == '4')
		return 4;
	if (c == '5')
		return 5;
	if (c == '6')
		return 6;
	if (c == '7')
		return 7;
	if (c == '8')
		return 8;
	if (c == '9')
		return 9;
	if (c == 'A')
		return 10;
	if (c == 'B')
		return 11;
	if (c == 'C')
		return 12;
	if (c == 'D')
		return 13;
	if (c == 'E')
		return 14;
	return 15;
}