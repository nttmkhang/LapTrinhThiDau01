def TongLe(n):
    s = 0
    for i in range(1, 2 * n + 2, 2):
        s = s + i
    return s
