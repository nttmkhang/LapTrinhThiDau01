BigNum addBigNum(BigNum x, BigNum y)
{
	while (x.size() < y.size()) x = '0' + x;
	while (x.size() > y.size()) y = '0' + y;

	int carry = 0;
	BigNum temp = "";
	for (int i = x.size() - 1; i >= 0; i--)
	{
		int xx = toNumber(x[i]);
		int yy = toNumber(y[i]);
		int ss = xx + yy + carry;
		temp = toChar(ss % 10) + temp;
		carry = ss / 10;
	}
	if (carry > 0)
		temp = "1" + temp;
	return temp;
}