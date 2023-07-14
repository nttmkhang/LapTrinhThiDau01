#include <iostream>
using namespace std;

long long uscln(long long a, long long b)
{
	a = abs(a);
	b = abs(b);
	while (b > 0)
	{
		a = a % b;
		swap(a, b);
	}
	return a;
}