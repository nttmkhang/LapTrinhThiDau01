int compareBigNum(BigNum x, BigNum y)
{
	while (x.size() < y.size()) x = '0' + x;
	while (x.size() > y.size()) y = '0' + y;
	if (x > y)
		return 1;
	if (x < y)
		return -1;
	return 0;}