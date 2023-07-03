#include <iostream>
using namespace std;

float LuyThua(float x, long n)
{
	if (n == 0)
		return 1;
	float t = LuyThua(x, n / 2);
	if (n % 2 == 0)
		return t * t;
	return t * t * x;
}

long long power(long long a, long long b)
{
	if (b == 0)
		return 1LL;
	long long t = power(a, b / 2);
	if (b % 2 == 0)
		return t * t;
	return t * t * a;
}
