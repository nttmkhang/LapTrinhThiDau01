long modBigNum(BigNum x, long y)
{
	long hold = 0;
	for (int i = 0; i < x.size(); i++)
	{
		hold = hold * 10 + toNumber(x[i]);
		hold = hold % y;
	}
	return hold;
}