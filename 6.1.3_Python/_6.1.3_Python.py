def mulEgypt(a, b):
    t = 0
    while(b >= 1):
        if(b & 1):
            t = t + a
        b >>= 1
        a <<= 1
    return t