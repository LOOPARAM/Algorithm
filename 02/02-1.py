def nPr(n,r):
    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    return result

print(nPr(4,2))