#include <iostream>
#include <vector>
using namespace std;

vector<long long> Factorization(long long n)
{
	vector<long long> minprime(n + 1);
	for (long long p = 0; p <= n; p++)
		minprime[p] = p;
	for (long long p = 2; p * p <= n; p++)
		if (minprime[p] == p)
			for (int i = p * p; i <= n; i += p)
				if (minprime[i] == i)
					minprime[i] = p;

	vector<long long> factorprime;
	while (n > 1)
	{
		factorprime.push_back(minprime[n]);
		n /= minprime[n];
	}
	return factorprime;
}