#include <iostream>
using namespace std;

long long Tong(int n)
{
	long long s = 0;
	for (int i = 1; i <= 3 * n + 1; i++)
		if (i % 2 != 0)
			s = s + i;
		else
			s = s - i;
	return s;
}