#include <iostream>

int Reverse(int n)
{
	int dn = 0;
	while (n)
	{
		if (dn > INT_MAX / 10 || dn < INT_MIN / 10)
			return 0;
		dn = dn * 10 + n % 10;
		n /= 10;
	}
	return dn;
}