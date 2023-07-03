long long BinaryToDecimal(const string& n)
{
    string reversed = n;
    reverse(reversed.begin(), reversed.end());

    long long decimal = 0;
    long long twopower = 1;
    for (char c : reversed)
    {
        if (c == '1')
            decimal += twopower;
        twopower *= 2;
    }
    return decimal;
}