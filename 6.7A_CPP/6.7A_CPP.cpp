#include <iostream>
using namespace std;

long long Tong(int n)
{
	long long s = 1;
	for (int i = 1; i <= n; i++)
		if (i % 2 != 0)
			s = s - (3 * i - 1) + (3 * i) - (3 * i + 1);
		else
			s = s + (3 * i - 1) - (3 * i) + (3 * i + 1);
	return s;
}