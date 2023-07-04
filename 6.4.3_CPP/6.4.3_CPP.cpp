long long powerModulo(long long a, long long b, long long M)
{
	if (b == 0)
		return 1LL;
	long long t = powerModulo(a, b / 2LL, M) % M;
	t = mulEgyptModulo(t, t, M);
	if (b % 2 == 0)
		return t;
	return mulEgyptModulo(t, a, M);}