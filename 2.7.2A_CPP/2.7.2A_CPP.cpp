#include <vector>
using namespace std;

vector<long long> Factorization(long long n)
{
	vector<long long> factorprime;
	long long p = 2;
	while (n > 1 && p * p <= n)
	{
		while (n % p == 0)
		{
			factorprime.push_back(p);
			n /= p;
		}
		p++;
	}
	if (n > 1)
		factorprime.push_back(n);
	return factorprime;
}