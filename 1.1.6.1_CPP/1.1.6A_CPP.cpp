void XuatAscii()
{
    for (char c = '0'; c <= '9'; c++)
        cout << "\n" << c << " " << int(c);

    for (char c = 'A'; c <= 'Z'; c++)
        cout << "\n" << c << " " << int(c);

    for (char c = 'a'; c <= 'z'; c++)
        cout << "\n" << c << " " << int(c);
}
