long long TongLapPhuong(long long n)
{
	long long s = 0;
	for (long long i = 1; i <= n; i++)
		s = s + i * i * i;
	return s;
}