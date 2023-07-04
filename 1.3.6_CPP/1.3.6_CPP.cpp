string BinaryToHexa(const string& n)
{
    string binary = n;
    while (binary.size() % 4 != 0)
        binary = '0' + binary;

    string hex;
    for (int i = 0; i < binary.size(); i += 4)
    {
        string group = binary.substr(i, 4);
        int index = BinaryToDecimal(group);
        hex += toChar(index);
    }
    return hex;
}
