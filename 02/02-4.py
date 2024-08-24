import sys
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
sys.setrecursionlimit(1000000)


memo = {}

def nCr(n,r):
    result = 1
    for i in range(1,r+1):
        result = result * (n-i+1)/i
    return result

print(nCr(9,5))