import sys
recursion_limit = sys.getrecursionlimit()
print(recursion_limit)
sys.setrecursionlimit(1000000)


memo = {}

def nCr(n,r):
    note = str([n,r])
    if note in memo:
        return memo[note]
    if (r == 0) or (r==n):
        return 1
    memo[note] = nCr(n-1, r-1) + nCr(n-1,r)
    return memo[note]

print(nCr(9,5))