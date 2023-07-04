#include <iostream>
using namespace std;

char toChar(int);
string DecimalToBinary(long long);

int main()
{
	long long n;
	cout << "Nhap n (n <= 10^9): ";
	cin >> n;

	cout << "\nBieu dien so thap phan ";
	cout << n << " o he co so 2 la: ";
	cout << DecimalToBinary(n);

	cout << "\n\n\nKet thuc!!!!";
	return 1;}char toChar(int n)
{
	char Letter[] = { '0','1','2','3','4','5',
	'6','7','8','9','A','B','C','D','E','F' };
	return Letter[n];
}string DecimalToBinary_3(long long n)
{
	string temp;
	while (n)
	{
		if (n & 1)
			temp = '1' + temp;
		else
			temp = '0' + temp;
		n >>= 1;
	}
	return temp;
}