def power(a, b):
    t = 1
    while(b > 0):
        if(b % 2 != 0):
            t = t * a
        b = b // 2
        a = a * a
    return t
