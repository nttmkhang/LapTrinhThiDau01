
#include <iostream>
using namespace std;

long long TongChan(long long n)
{
	long long s = 0;
	for (long long i = 2; i <= 2 * n; i += 2)
		s = s + i;
	return s;
}