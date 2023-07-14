//cai tien lan 1

long long GiaiThua(long long n)
{
	long long T = 1;
	for (long long i = 1; i <= n; i++)
		T = T * i;
	return T;
}

long long Catalan(long long n)
{
	long long a = GiaiThua(2 * n);
	long long b = GiaiThua(n);
	long long c = GiaiThua(n + 1);
	return a / b / c;
}