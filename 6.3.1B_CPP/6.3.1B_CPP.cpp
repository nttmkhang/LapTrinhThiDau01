long long power(long long a, long long b)
{
	long long t = 1;
	for (long long i = 1; i <= b; i++)
		t = t * a;
	return t;
}