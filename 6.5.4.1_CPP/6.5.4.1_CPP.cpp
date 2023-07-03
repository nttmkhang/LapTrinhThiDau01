long long TongLe(long long n)
{
	long long s = 0;
	for (long long i = 1; i <= 2 * n + 1; i += 2)
		s = s + i;
	return s;}