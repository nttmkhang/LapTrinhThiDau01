long long sumDivisors_2(long long n)
{
	long long T = 1;
	long long p = 2;
	while (n > 1)
	{
		long long count = 0;
		long long power = 1;
		while (n % p == 0)
		{
			power *= p;
			count++;
			n /= p;
		}
		T = T * (power * p - 1) / (p - 1);
		p++;
	}
	return T;
}