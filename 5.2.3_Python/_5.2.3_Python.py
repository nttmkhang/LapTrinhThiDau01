def binomialCoeff(n, k):
    if k > n - k:
        k = n - k  # C(n,k) = C(n,n-k)

    temp = 1
    for i in range(k):
        temp *= (n - i)
        temp = temp / (i + 1)
    return temp

def Catalan(n):
    return binomialCoeff(2 * n, n) / (n + 1)
