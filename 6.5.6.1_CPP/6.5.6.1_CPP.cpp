long long TongBa(long long n)
{
	long long s = 0;
	for (long long i = 2; i <= 3 * n - 1; i += 3)
		s = s + i;
	return s;
}