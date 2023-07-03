#include <iostream>
#include <string>
using namespace std;

string toChar(int n);
string DecimalToHexa(long long n);

int main()
{
	long long n;
	cout << "Nhap n (n <= 10^9): ";
	cin >> n;
	cout << "\nBieu dien so thap phan ";
	cout << n << " co he co so 16 la: ";
	cout << DecimalToHexa(n);
	cout << "\n\n\nKet thuc!!!!";
	return 1;
}

string toChar(int n) {
	string Letter[] = { "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F" };
	return Letter[n];
}

string DecimalToHexa(long long n)
{
	string temp;
	while (n > 0)
	{
		temp = toChar(n % 16) + temp;
		n = n / 16;
	}
	return temp;
}
