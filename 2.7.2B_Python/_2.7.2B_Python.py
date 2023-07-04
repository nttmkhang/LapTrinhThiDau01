def outPowerVector(a):
    temp = ""
    i = 0
    while i < len(a):
        temp = temp + " " + str(a[i])
        count = 1
        while i + 1 < len(a) and a[i + 1] == a[i]:
            count += 1
            i += 1
        if count > 1:
            temp = temp + "^" + str(count)
        i += 1
    return temp
