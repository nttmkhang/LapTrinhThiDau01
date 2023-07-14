long long sumDivisors_1(long long n)
{
	long long s = 0;
	for (long long i = 1; i <= n; i++)
		if (n % i == 0)
			s = s + i;
	return s;
}