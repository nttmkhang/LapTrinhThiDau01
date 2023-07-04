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

long long bscnn_1(long long a, long long b)
{
	return (a * b) / uscln(a, b);
}