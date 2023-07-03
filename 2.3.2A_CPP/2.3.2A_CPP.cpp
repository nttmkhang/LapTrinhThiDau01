bool ktNguyenTo(long long n)
{
	if (n <= 1)
		return false;
	for (long long i = 2; i <= n - 1; i++)
		if (n % i == 0)
			return false;
	return true;
}