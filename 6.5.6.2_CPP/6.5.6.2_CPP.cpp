long long TongBaNhanh(long long n)
{
	if (n % 2 == 0)
		return (n / 2) * (3 * n + 1);
	return ((3 * n + 1) / 2) * n;
}