#include <iostream>
using namespace std;

long long uscln_2(long long a, long long b)
{
	a = abs(a);
	b = abs(b);
	while (a != 0 && b != 0)
	{
		if (a > b)
			a = a % b;
		else
			b = b % a;
	}
	return a + b;
}