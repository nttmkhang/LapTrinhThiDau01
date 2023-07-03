def XuatAscii():
    for c in range(ord('0'), ord('9') + 1):
        print("\n", chr(c), " ", c)
    for c in range(ord('A'), ord('Z') + 1):
        print("\n", chr(c), " ", c)
    for c in range(ord('a'), ord('z') + 1):
        print("\n", chr(c), " ", c)