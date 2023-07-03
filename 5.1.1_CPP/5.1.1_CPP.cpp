#include <vector>
using namespace std;

long long Fibonacci(long long n)
{
	vector<long long> fibo(n + 1);
	fibo[0] = 0;
	fibo[1] = 1;
	for (long long i = 2; i <= n; i++)
		fibo[i] = fibo[i - 1] + fibo[i - 2];
	return fibo[n];
}