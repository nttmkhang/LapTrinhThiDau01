#include <iostream>
#include <unordered_map>
using namespace std;

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
    if (c == 'A' || c == 'a')
        return 10;
    if (c == 'B' || c == 'b')
        return 11;
    if (c == 'C' || c == 'c')
        return 12;
    if (c == 'D' || c == 'd')
        return 13;
    if (c == 'E' || c == 'e')
        return 14;
    return 15;
}

string DecimalToBinary(long long n)
{
    string temp;
    while (n > 0)
    {
        if (n % 2 != 0)
            temp = '1' + temp;
        else
            temp = '0' + temp;
        n = n / 2;
    }
    return temp;
}

string HexaToBinary_2(string n)
{
    string group[] = { "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111" };
    string temp;
    for (int i = 0; i < n.size(); i++)
    {
        int index = toNumber(n[i]);
        temp = temp + group[index];
    }
    while (temp.size() > 1 && temp[0] == '0')
        temp.erase(0, 1);
    return temp;
}