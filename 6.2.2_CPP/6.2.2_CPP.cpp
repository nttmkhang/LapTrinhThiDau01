long long mulEgyptModulo(long long a, long long b, long long M)
{
	if (b == 0)
		return 0;
	long long t = mulEgyptModulo(a, b / 2, M) % M;
	if (b % 2 != 0)
		return (t + t + a % M) % M;
	return (t + t) % M;
}