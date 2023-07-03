import sys

def Reverse(n):
    dn = 0
    max = sys.maxsize
    while n > 0:
        if (dn > max / 10) or (dn < -(max / 10)):
            return 0
        dn = dn * 10 + n % 10
        n = int(n / 10)
    return dn