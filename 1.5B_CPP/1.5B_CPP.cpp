#include <iostream>
using namespace std;

bool isPalindrome(int n)
{
	if (n < 0)
		return false;
	int nn = n;
	int dn = 0;
	while (nn)
	{
		if (dn > INT_MAX / 10)
			return false;
		dn = dn * 10 + nn % 10;
		nn /= 10;
	}
	return (dn == n);
}