float LuyThua(float x, long n)
{
	float t = 1;
	for (int i = 1; i <= n; i++)
		t = t * x;
	return t;
}