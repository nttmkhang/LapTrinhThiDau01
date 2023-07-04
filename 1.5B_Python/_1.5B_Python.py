def isPalindrome(n):
    if n < 0:
        return False
    nn = n
    dn = 0
    while (nn):
        if dn > (2**31 - 1) // 10:
            return False
        dn = dn * 10 + nn % 10
        nn //= 10
    return (dn == n)
