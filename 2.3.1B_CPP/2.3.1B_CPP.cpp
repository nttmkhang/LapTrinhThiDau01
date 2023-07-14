bool ktNguyenTo(long long n)
{
	int dem = 0;
	for (long long i = 1; i <= n; i++)
		if (n % i == 0)
			dem++;
	return (dem == 2);
}