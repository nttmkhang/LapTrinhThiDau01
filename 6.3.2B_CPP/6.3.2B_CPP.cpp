long long power(long long a, long long b)
{
	if (b == 0)
		return 1;
	return a * power(a, b - 1);
}