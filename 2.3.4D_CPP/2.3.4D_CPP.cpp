#include <iostream>
using namespace std;

bool isPrime(long long);

int main()
{
	long long n;
	cout << "Nhap n: ";
	cin >> n;

	if (isPrime(n))
		cout << n << " la so nguyen to!!!";
	else
		cout << n << " khong la so nguyen to!!!";

	cout << "\n\n\nKet thuc!!!!";
	return 1;
}

bool isPrime(long long n)
{
	if (n <= 1)
		return false;
	if (n == 2)
		return true;
	if (n == 3)
		return true;
	if (n % 2 == 0)
		return false;
	if (n % 3 == 0)
		return false;
	for (long long i = 5; i * i <= n; i += 6)
		if ((n % i == 0) || (n % (i + 2) == 0))
			return false;
	return true;
}