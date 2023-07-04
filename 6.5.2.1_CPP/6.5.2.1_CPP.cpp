#include <iostream>
using namespace std;

long long TongBinhPhuong(long long n)
{
	long long s = 0;
	for (long long i = 1; i <= n; i++)
		s = s + i * i;
	return s;
}