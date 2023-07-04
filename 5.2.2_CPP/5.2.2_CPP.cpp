#include <vector>
using namespace std;

long long Catalan(long long n)
{
	vector<long long> Cata(n + 1);
	Cata[0] = Cata[1] = 1;
	for (long long k = 2; k <= n; k++)
	{
		Cata[k] = 0;
		for (int i = 0; i < k; i++)
			Cata[k] += Cata[i] * Cata[k - i - 1];
	}
	return Cata[n];}