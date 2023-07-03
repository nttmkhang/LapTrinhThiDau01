#include <vector>
using namespace std;

vector<long long> Factorization(long long n)
{
	vector<long long> factorprime;
	long long p = 2;
	while (n > 1)
	{
		while (n % p == 0)
		{
			factorprime.push_back(p);
			n /= p;
		}
		p++;
	}
	return factorprime;
}