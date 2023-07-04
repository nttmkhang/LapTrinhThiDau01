def power(a, b):
    t = 1
    for i in range(1, b + 1):
        t = t * a
    return t