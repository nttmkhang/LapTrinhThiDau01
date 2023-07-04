def compareBigNum(x, y):
    while len(x) < len(y):
        x = '0' + x
    while len(x) > len(y):
        y = '0' + y
    if x > y:
        return 1
    if x < y:
        return -1
    return 0
