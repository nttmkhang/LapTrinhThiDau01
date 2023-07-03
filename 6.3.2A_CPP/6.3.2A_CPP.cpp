float LuyThua(float x, long n)
{
	if (n == 0)
		return 1;
	return x * LuyThua(x, n - 1);
}