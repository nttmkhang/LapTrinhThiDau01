#include <string>
using namespace std;

string DecimalToBinary_3(long long n)
{
	string temp;
	while (n)
	{
		if (n & 1)
			temp = '1' + temp;
		else
			temp = '0' + temp;
		n >>= 1;
	}
	return temp;
}