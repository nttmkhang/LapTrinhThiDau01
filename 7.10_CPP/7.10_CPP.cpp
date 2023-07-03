BigNum divBigNum(BigNum x, BigNum y)
{
	BigNum kY[11];
	kY[0] = "0";
	for (int k = 1; k <= 10; k++)
		kY[k] = addBigNum(kY[k - 1], y);

	BigNum temp = "";
	BigNum hold = "";
	for (int i = 0; i < x.size(); i++)
	{
		hold = hold + x[i];
		int k = 0;
		while (compareBigNum(hold, kY[k + 1]) != -1)
			k++;
		temp = temp + toChar(k);
		hold = subBigNum(hold, kY[k]);

	}
	while (temp.size() > 1 && temp[0] == '0')
		temp.erase(0, 1);
	return temp;
}