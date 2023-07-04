#include <string>
#include <iostream>
using namespace std;

typedef string BigNum;

BigNum BigFactorial(long n)
{
	BigNum T = "1";
	for (long i = 1; i <= n; i++)
		T = mulBigNum(T, i);
	return T;
