#include <iostream>
#include <string>
using namespace std;
typedef string BigNum;

int toNumber(char);
char toChar(int);

int compareBigNum(BigNum, BigNum);
BigNum addBigNum(BigNum, BigNum);
BigNum subBigNum(BigNum, BigNum);
BigNum mulBigNum(BigNum, long);
BigNum divBigNum(BigNum, BigNum);

BigNum BigFactorial(long);
BigNum BigCatalan(long);

int main()
{
	long n;
	cout << "Nhap n: ";
	cin >> n;

	cout << "So hang catalan " << n;
	cout << "! : " << BigCatalan(n);

	cout << "\n\n\nKet thuc!!!!";
	return 1;
}