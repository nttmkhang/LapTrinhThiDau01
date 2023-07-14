long long powerModulo(long long a, long long b, long long M)
{
	long long t = 1;
	a = a % M;
	while (b > 0)
	{
		if (b % 2 == 1)
			t = (t * a) % M;
		b = b / 2;
		a = (a * a) % M;
	}
	return t;
}