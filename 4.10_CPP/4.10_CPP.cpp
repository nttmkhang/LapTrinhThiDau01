#include <iostream>
using namespace std;

long ToHop(int n, int k)
{
	if (k > n - k)
		k = n - k; // C(n, k) = C(n, n-k)

	long temp = 1;
	for (int i = 0; i < k; i++)
	{
		temp *= (n - i);
		temp /= (i + 1);
	}
	return temp;
}

int main()
{
	int n;
	cin >> n;
	int k;
	cin >> k;

	cout << ToHop(n, k);
	return 1;
}