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

string HexaToBinary_1(string n)
{
    string temp;
    for (int i = 0; i < n.size(); i++)
    {
        int index = toNumber(n[i]);
        string group = DecimalToBinary(index);
        while (group.size() < 4)
            group = '0' + group;
        temp = temp + group;
    }
    while (temp.size() > 1 && temp[0] == '0')
        temp.erase(0, 1);
    return temp;
}