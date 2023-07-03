#include <iostream>
using namespace std;

long long mulEgypt(long long a, long long b)
{
	if (b == 0)
		return 0;
	long long t = mulEgypt(a, b / 2);
	if (b % 2 != 0)
		return t + t + a;
	return t + t;
}