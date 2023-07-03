long long binomialCoeff(long long n, long long k)
{
	if (k > n - k)
		k = n - k; // C(n,k) = C(n,n-k)

	long long temp = 1;
	for (long long i = 0; i < k; ++i)
	{
		temp *= (n - i);
		temp /= (i + 1);
	}
	return temp;
}

long long Catalan(long long n)
{
	return binomialCoeff(2 * n, n) / (n + 1);
}