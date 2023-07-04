def ToHop(n, k):
    if k > n - k:
        k = n - k

    temp = 1
    for i in range (0, k):
        temp *= (n - i)
        temp /= int(i + 1)
    return temp

def main():
    n = int(input())
    k = int(input())
    print(ToHop(n, k))

if __name__ == "__main__":
    main()
