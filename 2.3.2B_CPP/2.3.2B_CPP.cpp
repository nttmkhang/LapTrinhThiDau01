bool ktNguyenTo(long long n)
{
	for (long long i = 2; i < n; i++)
		if (n % i == 0)
			return 0;
	return (n > 1);
}