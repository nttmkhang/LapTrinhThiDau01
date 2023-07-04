BigNum divBigNum(BigNum x, long y)
{
	BigNum temp = "";
	long hold = 0;
	long ss = 0;
	for (int i = 0; i < x.size(); i++)
	{
		hold = hold * 10 + toNumber(x[i]);
		ss = hold / y;
		temp = temp + toChar(ss);
		hold = hold % y;
	}
	while (temp.size() > 1 && temp[0] == '0')
		temp.erase(0, 1);
	return temp;}