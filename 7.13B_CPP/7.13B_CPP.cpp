#include <iostream>
#include <string>
using namespace std;
typedef string BigNum;

int toNumber(char);
char toChar(int);

BigNum mulBigNum(BigNum, long);
BigNum BigFactorial(long);

int main()
{
	long n;
	cout << "Nhap n: ";
	cin >> n;

	cout << "So hang fibo " << n << " : ";
	cout << BigFactorial(n);

	cout << "\n\n\nKet thuc!!!!";
	return 1;
}