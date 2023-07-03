#include <iostream>
#include <vector>
using namespace std;

vector<long long> Eratosthenes(long long n)
{
	vector<bool> isprime(n + 1, true);
	isprime[0] = false;
	isprime[1] = false;
	for (long long p = 2; p <= n; p++)
		if (isprime[p] == true)
			for (int i = 2 * p; i <= n; i += p)
				isprime[i] = false;
	vector<long long> prime;
	for (long long p = 2; p <= n; p++)
		if (isprime[p] == true)
			prime.push_back(p);
	return prime;
}