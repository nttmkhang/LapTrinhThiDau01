long long sumDivisors_3(long long n)
{
	long long T = 1;
	long long p = 2;
	while (n > 1 && p * p <= n)
	{
		long long count = 0;
		long long power = 1;
		while (n % p == 0)
		{
			power *= p;
			count++;
			n /= p;
		}
		if (count > 0)
			T = T * (power * p - 1) / (p - 1);
		p++;
	}
	if (n > 1)
		T = T * (n * n - 1) / (n - 1);
	return T;
}