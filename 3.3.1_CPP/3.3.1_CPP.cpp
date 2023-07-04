long long countDivisors_1(long long n)
{
	long long count = 0;
	for (long long i = 1; i <= n; i++)
		if (n % i == 0)
			count++;
	return count;}