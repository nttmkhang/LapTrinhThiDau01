#include <string>
using namespace std;

char toChar(int);

string DecimalToBinary_2(long long n)
{
	string temp;
	while (n > 0)
	{
		temp = toChar(n % 2) + temp;
		n /= 2;
	}
	return temp;}char toChar(int n)
{
	char Letter[] = { '0','1','2','3','4','5',
	'6','7','8','9','A','B','C','D','E','F' };
	return Letter[n];
}