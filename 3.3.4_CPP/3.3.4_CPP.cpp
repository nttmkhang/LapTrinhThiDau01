#include <iostream>
#include <vector>
using namespace std;

long long countDivisors_4(long long n)
{
	vector<long long> minprime(n + 1);
	for (long long p = 0; p <= n; p++)
		minprime[p] = p;
	for (long long p = 2; p * p <= n; p++)
		if (minprime[p] == p)
			for (int i = p * p; i <= n; i += p)
				if (minprime[i] != i)
					minprime[i] = p;
	long long T = 1;
	while (n > 1)
	{
		long long minp = minprime[n];
		long long count = 0;
		while (n % minp == 0)
		{
			count++;
			n /= minp;
		}
		T = T * (count + 1);
	}
	return T;
}