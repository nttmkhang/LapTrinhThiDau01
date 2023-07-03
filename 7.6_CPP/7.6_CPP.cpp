#include <iostream>
#include <string>
using namespace std;
typedef string BigNum;

char toChar(int n) {
	char Letter[] = { '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F' };
	return Letter[n];
}

int toNumber(char c)
{
	if (c == '0')
		return 0;
	if (c == '1')
		return 1;
	if (c == '2')
		return 2;
	if (c == '3')
		return 3;
	if (c == '4')
		return 4;
	if (c == '5')
		return 5;
	if (c == '6')
		return 6;
	if (c == '7')
		return 7;
	if (c == '8')
		return 8;
	if (c == '9')
		return 9;
	if (c == 'A')
		return 10;
	if (c == 'B')
		return 11;
	if (c == 'C')
		return 12;
	if (c == 'D')
		return 13;
	if (c == 'E')
		return 14;
	return 15;
}

BigNum mulBigNum(BigNum x, long y) {
	long carry = 0;
	string temp = "";
	for (int i = x.size() - 1; i >= 0; --i) {
		int xx = toNumber(x[i]);
		long ss = xx * y + carry;
		temp = toChar(ss % 10) + temp;
		carry = ss / 10;
	}
	if (carry > 0) {
		temp = to_string(carry) + temp;
	}
	return temp;
}