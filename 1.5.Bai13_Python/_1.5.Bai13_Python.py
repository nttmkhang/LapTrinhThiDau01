
def intToRoman(n):
    temp = ''
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i = 12
    while (n > 0):
        div = n // num[i]
        while(div > 0):
            temp = temp + sym[i]
            div = div - 1
        n = n % num[i]
        i = i - 1
    return temp