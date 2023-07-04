BigNum Catalan(long n)
{
	BigNum a = BigFactorial(2 * n);
	BigNum b = BigFactorial(n);
	BigNum c = BigFactorial(n + 1);
	return divBigNum(divBigNum(a, b), c);
}