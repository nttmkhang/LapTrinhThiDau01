#include <iostream>
using namespace std;

long long uscln_3(long long a, long long b)
{
	a = abs(a);
	b = abs(b);
	while (a != 0 && b != 0)
	{
		a = a % b;
		swap(a, b);
	}
	return a + b;
}