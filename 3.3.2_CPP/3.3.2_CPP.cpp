long long countDivisors_2(long long n)
{
	long long T = 1;
	long long p = 2;
	while (n > 1)
	{
		long long count = 0;
		while (n % p == 0)
		{
			count++;
			n /= p;
		}
		T = T * (count + 1);
		p++;
	}
	return T;}