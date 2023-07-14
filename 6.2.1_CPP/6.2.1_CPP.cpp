long long mulEgyptModulo(long long a,
	long long b, long long M)
{
	long long t = 0;
	while (b >= 1)
	{
		if (b % 2 != 0)
			t = (t % M + a % M) % M;
		b = b / 2;
		a = a * 2;
	}
	return t;
}